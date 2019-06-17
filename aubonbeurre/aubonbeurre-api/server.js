let express = require('express')
let mysql = require('sync-mysql');
const cors = require('cors')

function getAlertRequest(field){
    return `SELECT ar.id, u.\`number\` as unit_number, a.\`number\` as automat_number, 
    \`name\` as unit_name, \`location\` as unit_location, 
    \`type\` as automate_type, DATE_FORMAT(record_date, '%d-%m-%Y %k:%i') as date_recording, 
    `+field+` as \`level\`, 
    (SELECT max_value FROM critical_level WHERE \`name\`='`+field+`' limit 1) as critical_level_max,
    (SELECT min_value FROM critical_level WHERE \`name\`='`+field+`' limit 1) as critical_level_min
    FROM automate_recording  ar
    left join automate a on ar.automate_id = a.id
    left join unit_recording ur on ur.id = ar.unit_recording_id
    left join unit u on u.id = ur.unit_id
    WHERE `+field+` > (SELECT max_value FROM critical_level WHERE \`name\`='`+field+`' limit 1) 
        OR `+field+` < (SELECT min_value FROM critical_level WHERE \`name\`='`+field+`' limit 1)
    ORDER BY date_recording DESC;`
} 

// Launch server

let app = express()
app.use(cors()) // enable CORS
let port = process.env.PORT || 3009



// params mysql server connection

let connection = new mysql({
  host     : 'vps691279.ovh.net',
  user     : 'corentin.dupont',
  password : 'dupont.corentin',
  port: 3306,
  database: 'au_bon_beurre',
});

// Middlewares
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

/**
 * CUSTOM METHODS
 */

// Used for the toMysqlFormat date protoype function
function twoDigits(d) {
    if(0 <= d && d < 10) return "0" + d.toString();
    if(-10 < d && d < 0) return "-0" + (-1*d).toString();
    return d.toString();
}

// add a function to date object to be able to compare js date with mysql date
Date.prototype.toMysqlFormat = function() {
    return toMysqlFormat(this)
};

function toMysqlFormat(date) {
    return date.getUTCFullYear() + "-" + twoDigits(1 + date.getUTCMonth()) + "-" + twoDigits(date.getUTCDate()) + " " + twoDigits(date.getUTCHours()) + ":" + twoDigits(date.getUTCMinutes()) + ":" + twoDigits(date.getUTCSeconds());
}

// Routes

app.get('/', function (req, res) {
    res.send('/complete-unit-recording/:number')
})

app.get('/complete-unit-recording/:number', async (req, res) => {
    console.log('[GET] - complete unit recording');

    try {
        // Get corresponding unit
        const unitNumber = req.params.number;

        const unit = connection.query(`SELECT * FROM unit WHERE number=${unitNumber}`)[0];
        console.log(`[complete unit recording] - unit - ${JSON.stringify(unit)}`)

        if (!unit) throw new Error(`[complete unit recording] - ERROR - no unit found for number ${unitNumber}`)

        // Get unit records
        const min_record_date = new Date((new Date()).getTime() - 1000 * 60 * 60);

        const getUnitRecordings_REQUEST = `SELECT * FROM unit_recording WHERE unit_id=${unit.id} AND record_date>'${min_record_date.toMysqlFormat()}'`
        console.log(`[complete unit recording] - try to execute query - ${getUnitRecordings_REQUEST} `)

        const unit_recordings = connection.query(getUnitRecordings_REQUEST);

        console.log(`[complete unit recording] - unit recordings - ${unit_recordings.length}`)

        if (!unit_recordings.length) {
            res.send([])
            throw new Error(`[complete unit recording] - ERROR - no unit recordings found.`)
        }
        // Get unit automates
        const getAutomates_REQUEST = `SELECT * FROM automate WHERE unit_id=${unit.id}`
        console.log(`[complete unit recording] - try to execute query - ${getAutomates_REQUEST} `)

        const unit_automates = connection.query(getAutomates_REQUEST)
        console.log(`[complete unit recording] - unit automates - ${unit_automates.length}`)
        
        // Get automate records
        const unit_recording_ids = unit_recordings.map( el => el.id );
        const unit_automate_ids = unit_automates.map( el => el.id );

        const getAutomateRecords_REQUEST = `
            SELECT * FROM automate_recording WHERE 
            unit_recording_id IN (${unit_recording_ids.join(',')})
            AND automate_id IN (${unit_automate_ids.join(',')})
        `
        console.log(`[complete unit recording] - try to execute query - ${getAutomateRecords_REQUEST} `)

        const unit_automates_records = connection.query(getAutomateRecords_REQUEST)
        console.log(`[complete unit recording] - unit automate records - ${unit_automates_records.length}`)

        // group by automate
        const complete_unit_recording = unit_automates.map( automate => {
            const records = unit_automates_records.filter( unit_automate_record => unit_automate_record.automate_id === automate.id);
            return {...automate, records}
        })        
        res.send(complete_unit_recording);

    } catch (error) {
        res.send("Error ", error)
    }
    
      
}) 

app.get('/alertes/:field',  async (req, res) => {
    const field = req.params.field;
    let datas = connection.query(getAlertRequest(field));
    res.send(datas);
})

app.get('/alertes-types', async (req, res) => {
    
    let datas = connection.query('select `name` from critical_level group by `name`');
    res.send(datas);
})

app.listen(port, function () {
    console.log(`Au_bon_beurre Api app listening on port ${port} !`)
})

module.exports = { getAlertRequest, twoDigits }


 