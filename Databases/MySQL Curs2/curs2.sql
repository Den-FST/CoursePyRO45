-- creare baza de date
CREATE DATABASE curs2;

-- comanda pentru a folosi o anumita baza de date
-- pentru a comenta cod punem 2 liniute "--" sau " /* */"
USE curs2;

-- stergerea unei baze de date
DROP DATABASE curs2;

CREATE TABLE produs (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    denumire VARCHAR(100) NOT NULL,
    pret DECIMAL(8,2) NOT NULL,
    disponibil BOOLEAN NOT NULL
    #PRIMARY KEY(id)
);

SELECT * FROM produs;

#categorie(id, nume)
CREATE TABLE categorie (
	id INT PRIMARY KEY auto_increment NOT NULL,
    nume varchar(100) NOT NULL
);

-- pentru a modifica structura unei tabele
ALTER TABLE produs
ADD COLUMN id_categorie TINYINT AFTER denumire;

-- modificare tip coloana
ALTER TABLE produs
MODIFY COLUMN id_categorie INT;

-- adaugare FK
ALTER TABLE produs
ADD CONSTRAINT categorie_fk
FOREIGN KEY (id_categorie) REFERENCES categorie(id);

CREATE TABLE client (
	id INT(7) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nume VARCHAR(50) NOT NULL,
    data_nastere DATE
);

CREATE TABLE comanda (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    data_comanda DATE NOT NULL,
    status_comanda ENUM('noua', 'procesare', 'livrata', 'anulata') NOT NULL,
    id_client INT(7),
    FOREIGN KEY (id_client) REFERENCES client(id)
);
-- 0 row(s) affected, 1 warning(s): 1681 Integer display width is deprecated and will be removed in a future release.

CREATE TABLE factura (
	id_comanda INT NOT NULL,
    id_produs INT NOT NULL,
    FOREIGN KEY (id_comanda) REFERENCES comanda(id),
    foreign key (id_produs) references produs(id),
    PRIMARY KEY(id_comanda ASC, id_produs ASC) #ordonare crescatoare
);







