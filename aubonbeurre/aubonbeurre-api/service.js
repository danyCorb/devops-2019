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

// Used for the toMysqlFormat date protoype function
function twoDigits(d) {
    if(0 <= d && d < 10) return "0" + d.toString();
    if(-10 < d && d < 0) return "-0" + (-1*d).toString();
    return d.toString();
}

module.exports = { getAlertRequest, twoDigits }