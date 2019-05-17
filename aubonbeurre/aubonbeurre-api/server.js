let express = require('express')
let mysql = require('sync-mysql');


// Launch server

let app = express()
let port = process.env.PORT || 3009

app.listen(port, function () {
    console.log(`Example app listening on port ${port} !`)
})

// params mysql server connection

let connection = new mysql({
  host     : 'dany-corbineau.ddns.net',
  user     : 'corentin.dupont',
  password : 'dupont.corentin',
  port: 8001,
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
    return this.getUTCFullYear() + "-" + twoDigits(1 + this.getUTCMonth()) + "-" + twoDigits(this.getUTCDate()) + " " + twoDigits(this.getUTCHours()) + ":" + twoDigits(this.getUTCMinutes()) + ":" + twoDigits(this.getUTCSeconds());
};

// Routes

app.get('/', function (req, res) {
    res.send('Hello World!')
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

        const getUnitRecordings_REQUEST = `SELECT * FROM unit_recording WHERE id=${unit.id} AND record_date>'${min_record_date.toMysqlFormat()}'`
        console.log(`[complete unit recording] - try to execute query - ${getUnitRecordings_REQUEST} `)

        const unit_recordings = connection.query(getUnitRecordings_REQUEST);

        console.log(`[complete unit recording] - unit recordings - ${unit_recordings}`)

        if (!unit_recordings.length) {
            res.send([])
            throw new Error(`[complete unit recording] - ERROR - no unit recordings found.`)
        }
        // Get unit automates
        const getAutomates_REQUEST = `SELECT * FROM automate WHERE unit_id=${unit.id}`
        console.log(`[complete unit recording] - try to execute query - ${getAutomates_REQUEST} `)

        const unit_automates = connection.query(getAutomates_REQUEST)
        console.log(`[complete unit recording] - unit automates - ${unit_automates}`)
        
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
        console.log(`[complete unit recording] - unit automate records - ${unit_automates_records}`)

        // group by automate
        const complete_unit_recording = unit_automates.map( automate => {
            const records = unit_automates_records.filter( unit_automate_record => unit_automate_record.automate_id === automate.id);
            return {...automate, records}
        })        

    } catch (error) {
        console.error(error)
    }
    
    res.send(complete_unit_recording);
      
}) 



 