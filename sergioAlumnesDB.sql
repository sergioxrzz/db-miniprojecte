CREATE DATABASE IF NOT EXISTS sergioAlumnesDB;
USE sergioAlumnesDB;

CREATE TABLE IF NOT EXISTS alumnes (
	dni VARCHAR(9),
	nom VARCHAR(20) NOT NULL, 
    edat INT(3) NOT NULL,
		PRIMARY KEY(dni)
);

CREATE TABLE IF NOT EXISTS adreçes (
    cp INT(5),
    localitat VARCHAR(25),
    carrer VARCHAR(25) NOT NULL,
    vivenda INT(3) NOT NULL,
    propietari VARCHAR(9), -- FK alumnes.dni
		PRIMARY KEY(cp),
        FOREIGN KEY (propietari) REFERENCES alumnes (dni)
);

CREATE TABLE IF NOT EXISTS cicles (
	cicle VARCHAR(35),
	curs INT(2),
    alumne varchar(9), -- FK alumnes.dni
		PRIMARY KEY(cicle),
        FOREIGN KEY (alumne) REFERENCES alumnes(dni)
);