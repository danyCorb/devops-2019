USE au_bon_beurre;

-- create delegate administrator 
DROP USER IF EXISTS 'delegate_administrator'@'%';
CREATE USER 'delegate_administrator'@'%' IDENTIFIED BY 'delAdmPass44';

GRANT ALL PRIVILEGES ON au_bon_beurre TO 'delegate_administrator'@'%';
GRANT ALL PRIVILEGES ON au_bon_beurre.* to 'delegate_administrator'@'%';

-- create docker concentrator
DROP USER IF EXISTS 'docker_concentrator'@'%';
CREATE USER 'docker_concentrator'@'%' IDENTIFIED BY 'docConPass44';

GRANT SELECT, INSERT ON au_bon_beurre.* TO 'docker_concentrator'@'%';

-- create data vision
DROP USER IF EXISTS 'data_vision'@'%';
CREATE USER 'data_vision'@'%' IDENTIFIED BY 'datVisPass44';

GRANT SELECT ON au_bon_beurre.* TO 'data_vision'@'%';

FLUSH PRIVILEGES;