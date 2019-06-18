use au_bon_beurre;

-- create tables
SET FOREIGN_KEY_CHECKS=0;

drop table if exists site;
create table site (
	id int(11) not null primary key auto_increment,
    `name` varchar(255) not null
);

drop table if exists automate;
create table automate (
	id int(11) not null primary key auto_increment,
    `type` int(8) not null,
    unit_id int(11) not null,
    `number` int(8) not null,
    foreign key (unit_id) references unit(id)
);

drop table if exists automate_recording;
create table automate_recording (
	id int(11) not null primary key auto_increment,
    
    unit_recording_id int(11) not null,
    foreign key (unit_recording_id) references unit_recording(id),
    automate_id int(11) not null,
    foreign key (automate_id) references automate(id),
    
    tank_temperature float not null,
    external_temperature float not null,
    milk_tank_weight float not null,
    final_product_weight float not null,
    ph_measurement float not null,
    k_pos_measurement int not null,
    na_cl_concentration float not null,
    salmonella_level int not null,
    e_coli_level int not null,
    listeria_level int not null
);


drop table if exists unit;
create table unit (
    id int(11) not null primary key auto_increment,
    `name` varchar(255) not null,    
    `number` int(1) not null,
    location enum('Sector1', 'Sector2', 'Sector3')
);

drop table if exists unit_recording;
create table unit_recording (
    id int(11) not null primary key auto_increment,
    record_date DATETIME not null,
    unit_id int(11) not null,
    foreign key (unit_id) references unit(id)
);


drop table if exists critical_level;
create table critical_level (
	id int(11) not null primary key auto_increment,
    `name` varchar(255) not null,
    max_value float,
    min_value float
);

drop table if exists critical_level_changement;
create table critical_level_changement (
	id int(11) not null primary key auto_increment,
    
    old_critical_level_id int(11) not null,
    foreign key (old_critical_level_id) references critical_level(id),
    
    new_critical_level_id int(11) not null,
    foreign key (new_critical_level_id) references critical_level(id),
    
    `date` date not null
);

drop table if exists automate_recording_insert_error;
create table automate_recording_insert_error (
	id int(11) not null primary key auto_increment,
    automate_id int(11) not null,
    foreign key (automate_id) references automate(id),
    field_name varchar(255) not null,
    field_bad_value float not null,
    `date` datetime not null
);

SET FOREIGN_KEY_CHECKS=1;
