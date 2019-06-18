var assert = require('assert');
const { getAlertRequest, twoDigits } = require('./service.js')

describe('Basic Mocha String Test', function () {

// test mysql request string
 it('should return the desired sql request', function () {
        assert.equal(getAlertRequest('a_field'), `SELECT ar.id, u.\`number\` as unit_number, a.\`number\` as automat_number, 
    \`name\` as unit_name, \`location\` as unit_location, 
    \`type\` as automate_type, DATE_FORMAT(record_date, '%d-%m-%Y %k:%i') as date_recording, 
    a_field as \`level\`, 
    (SELECT max_value FROM critical_level WHERE \`name\`='a_field' limit 1) as critical_level_max,
    (SELECT min_value FROM critical_level WHERE \`name\`='a_field' limit 1) as critical_level_min
    FROM automate_recording  ar
    left join automate a on ar.automate_id = a.id
    left join unit_recording ur on ur.id = ar.unit_recording_id
    left join unit u on u.id = ur.unit_id
    WHERE a_field > (SELECT max_value FROM critical_level WHERE \`name\`='a_field' limit 1) 
        OR a_field < (SELECT min_value FROM critical_level WHERE \`name\`='a_field' limit 1)
    ORDER BY date_recording DESC;`);
    });


//  it('should return first charachter of the string', function () {
//         const date = new Date('2017-03-25T00:00:00')

//         Date.prototype.toMysqlFormat = function() {
//             return this.getUTCFullYear() + "-" + twoDigits(1 + this.getUTCMonth()) + "-" + twoDigits(this.getUTCDate()) + " " + twoDigits(this.getUTCHours()) + ":" + twoDigits(this.getUTCMinutes()) + ":" + twoDigits(this.getUTCSeconds());
//         };
//         assert.equal(date.toMysqlFormat(), '2017-03-25 00:00:00');
//     });
});