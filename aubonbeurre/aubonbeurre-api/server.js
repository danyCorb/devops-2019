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

// Routes

app.get('/', function (req, res) {
    res.send('Hello World!')
})

app.get('/complete-unit-recording/:number', async (req, res) => {
    console.log('[GET] - complete unit recording');

    try {
        // Get corresponding unit
        const unitNumber = req.params.number;

        const unit = connection.query(`SELECT * FROM unit WHERE number=${unitNumber}`);
        console.log(`[complete unit recording] - unit - ${unit}`)

        if (!unit) throw new Exception(`[complete unit recording] - ERROR - no unit found for number ${unitNumber}`)

        // Get unit records
        const min_record_date = new Date(Date.now().getTime() - 1000 * 60 * 60);
        const unit_recordings = connection.query(`SELECT * FROM unit_recording WHERE id=${unit.id} AND recordDate > ${min_record_date}`);
        console.log(`[complete unit recording] - unit recordings - ${unit_recordings}`)

        // Get unit automates
        const unit_automates = connection.query(`SELECT * FROM automate WHERE unit_id=${unit.id}`)
        console.log(`[complete unit recording] - unit automates - ${unit_automates}`)
        
        // Get automate records
        const unit_recording_ids = unit_recordings.map( el => el.id );
        const unit_automate_ids = unit_automates.map( el => el.id );

        const unit_automates_records = connection.query(`
            SELECT * FROM automate_recording WHERE 
            unit_recording_id IN (${unit_recording_ids.join(',')})
            AND automate_id IN (${unit_automate_ids.join(',')})
        `)
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
 