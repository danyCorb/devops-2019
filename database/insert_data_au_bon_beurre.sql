use au_bon_beurre;

insert into unit values (null, 'Alpha', 1, 'Sector1');
insert into unit values (null, 'Beta', 2, 'Sector2');
insert into unit values (null, 'Gamme', 3, 'Sector3');
insert into unit values (null, 'Zeta', 4, 'Sector1');
insert into unit values (null, 'Omega', 5, 'Sector2');
insert into unit values (null, 'Phy', 6, 'Sector3');
insert into unit values (null, 'Chi', 8, 'Sector1');

insert into automate values (null, 0x0000BA20, 1, 1);
insert into automate values (null, 0x0000BA20, 1, 2);
insert into automate values (null, 0x0000BA21, 1, 3);
insert into automate values (null, 0x0000BA21, 1, 4);
insert into automate values (null, 0x0000BA22, 1, 5);

insert into automate values (null, 0x0000BA23, 2, 1);
insert into automate values (null, 0x0000BA24, 2, 2);
insert into automate values (null, 0x0000BA25, 2, 3);
insert into automate values (null, 0x0000BA26, 2, 4);
insert into automate values (null, 0x0000BA21, 2, 5);
insert into automate values (null, 0x0000BA28, 2, 6);
insert into automate values (null, 0x0000BA22, 2, 7);

insert into automate values (null, 0x0000BA29, 3, 1);
insert into automate values (null, 0x0000BA2A, 3, 2);
insert into automate values (null, 0x0000BA2B, 3, 3);
insert into automate values (null, 0x0000BA2C, 3, 4);
insert into automate values (null, 0x0000BA2D, 3, 5);
insert into automate values (null, 0x0000BA2E, 3, 6);

insert into automate values (null, 0x0000BA23, 4, 1);
insert into automate values (null, 0x0000BA24, 4, 2);
insert into automate values (null, 0x0000BA25, 4, 3);
insert into automate values (null, 0x0000BA26, 4, 4);
insert into automate values (null, 0x0000BA21, 4, 5);
insert into automate values (null, 0x0000BA28, 4, 6);
insert into automate values (null, 0x0000BA22, 4, 7);
insert into automate values (null, 0x0000BA28, 4, 8);
insert into automate values (null, 0x0000BA22, 4, 9);

insert into automate values (null, 0x0000BA20, 5, 1);
insert into automate values (null, 0x0000BA20, 5, 2);
insert into automate values (null, 0x0000BA21, 5, 3);
insert into automate values (null, 0x0000BA21, 5, 4);
insert into automate values (null, 0x0000BA22, 5, 5);

insert into automate values (null, 0x0000BA23, 6, 1);
insert into automate values (null, 0x0000BA24, 6, 2);
insert into automate values (null, 0x0000BA25, 6, 3);
insert into automate values (null, 0x0000BA26, 6, 4);
insert into automate values (null, 0x0000BA21, 6, 5);
insert into automate values (null, 0x0000BA28, 6, 6);
insert into automate values (null, 0x0000BA22, 6, 7);

insert into automate values (null, 0x0000BA29, 7, 1);
insert into automate values (null, 0x0000BA2A, 7, 2);
insert into automate values (null, 0x0000BA2B, 7, 3);
insert into automate values (null, 0x0000BA2C, 7, 4);
insert into automate values (null, 0x0000BA2D, 7, 5);
insert into automate values (null, 0x0000BA2E, 7, 6);

insert into critical_level (id, `name`, min_val, max_val) values (null, "tank_temperature", 2.5, 4.0);
insert into critical_level (id, `name`, min_val, max_val) values (null, "external_temperature", 8, 14);
insert into critical_level (id, `name`, min_val, max_val) values (null, "milk_tank_weight", 3512, 4607);
insert into critical_level (id, `name`, min_val, max_val) values (null, "ph_measurement", 6.8, 7.2);
insert into critical_level (id, `name`, min_val, max_val) values (null, "k_pos_measurement", 35, 47);
insert into critical_level (id, `name`, min_val, max_val) values (null, "na_cl_concentration", 1.0, 1.7);
insert into critical_level (id, `name`, min_val, max_val) values (null, "salmonella_level", 17, 37);
insert into critical_level (id, `name`, min_val, max_val) values (null, "e_coli_level", 35, 49);
insert into critical_level (id, `name`, min_val, max_val) values (null, "listeria_level", 28, 54);