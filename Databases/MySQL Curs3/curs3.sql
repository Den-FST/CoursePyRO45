-- 1. Selectam blocul de cod/ tot query-ul si apasam pe primul fulger
-- 2. Mergem pe linia unui query/ in interiorul unui bloc de cod si selectam al doilea fulger
CREATE DATABASE firma;

USE firma;

-- creare tabele
CREATE TABLE departament (
	id TINYINT(2) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    denumire VARCHAR(50) NOT NULL,
    acronim VARCHAR(4)
);

CREATE TABLE angajat (
	id TINYINT NOT NULL auto_increment primary KEY,
    nume VARCHAR(50) NOT NULL,
    prenume VARCHAR(50) NOT NULL,
    data_angajare DATE NOT NULL,
    data_demisie DATE,
    salariu INT(5) NOT NULL DEFAULT 3000,
    id_departament TINYINT(2) NOT NULL,
    FOREIGN KEY (id_departament) REFERENCES departament(id)
);

-- inseram valori folosind comanda INSERT INTO
-- prima varianta de insert, inserand in ordinea in care am creat coloanele din tabela (vezi mai sus sau in schemas)
INSERT INTO departament
VALUES (NULL, 'Development', 'DEV');

-- afisarea valorilor din tabela departament
SELECT * FROM departament;

-- a doua varianta de insert, unde vom specifica ordinea in care sa se insereze datele
INSERT INTO departament(acronim, denumire)
VALUES
('HR', 'Human Resources'),
('QA', 'Quality Assurance'),
('ACC', 'Accounting');

SELECT * FROM departament;

-- a treia metoda de inserare a datelor folosind optiunea SET
INSERT INTO departament
SET denumire = 'Operations', acronim = 'OPS';

INSERT INTO departament
VALUES
(NULL, 'Research&Development', 'R&D'),
(NULL, 'Finance', 'FN');

# adaugare de valori NULL sau valori default
INSERT INTO departament VALUES();

-- SET SQL_SAFE_UPDATES = 1;

SELECT * FROM departament;

-- stergerea tuturor datelor din tabela - auto increment ramane la valoare "urmatoare"
DELETE FROM departament;
-- Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.  To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.

DELETE FROM departament
WHERE id = 3;

INSERT INTO departament
VALUES (NULL, 'Development', 'DEV');

-- stergerea si recrearea tabelei
TRUNCATE departament;
-- Error Code: 1701. Cannot truncate a table referenced in a foreign key constraint (`firma`.`angajat`, CONSTRAINT `angajat_ibfk_1`)

-- stergerea FK-ului din tabela folosind optiunea ALTER
ALTER TABLE angajat
DROP FOREIGN KEY angajat_ibfk_1;

-- SQL SERVER
# ALTER TABLE angajat
# DROP CONSTRAINT angajat_ibfk_1;

ALTER TABLE angajat
ADD constraint angajat_ibfk_1
FOREIGN KEY (id_departament) references departament(id);

SELECT * FROM departament;

-- putem seta de la ce valoare sa inceapa auto_increment
ALTER TABLE departament AUTO_INCREMENT = 1000;

INSERT INTO angajat
VALUES
(NULL, 'Popa', 'Matei', '20190315', NULL, 4500, 3),
(NULL, 'Rusu', 'Dan', '2018-05-23', NULL, 5000, 7),
(NULL, 'Popa', 'Tania', '2019-08-06', NULL, 4600, 3),
(NULL, 'Nistor', 'Andrei', '2019-07-14', NULL, 6000, 1),
(NULL, 'Dinu', 'Bogdan', '2019-08-02', NULL, 4600, 2),
(NULL, 'Voicu', 'Ana', '2018-04-12', NULL, 5000, 1),
(NULL, 'Florescu', 'Gina', '20181108', NULL, 4300, 5);

SELECT * FROM angajat;

# un angajat si-a dat demisia astazi
# dupa nume si prenume

-- SET SQL_SAFE_UPDATES = 1;
-- set sql_safe_updates = 0;

# prima metoda de update a unei informatii intr-o tabela, folosind nume si prenume sau orice altceva in afara de id
# este necesar sa folosim SET SQL_SAFE_UPDATES = 0;
UPDATE angajat
SET data_demisie = CURDATE()
WHERE nume='Popa' AND prenume='Matei';
-- Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.  To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.

# a doua metoda de update a datei in tabela angajat, folosind unul dintre formatele de data, si folosind id-ul persoanei alese
UPDATE angajat
SET data_demisie = '2020-11-03'
WHERE id = 1;

SELECT * FROM angajat;

UPDATE angajat
SET data_demisie = '20201104'
WHERE id = 1;

# salariile din departamentele 1 si 2 s-au majorat cu 10%
# prima metoda
UPDATE angajat
SET salariu = salariu * 1.1
WHERE id_departament = 1 OR id_departament = 2;

# a doua metoda
UPDATE angajat
SET salariu = salariu * 1.1
# dept 1 sau 7
WHERE id_departament IN (1, 7);

# majorarea salariului cu 500 ron pentru angajatii din departamentul 1, cu salariul < 6000
# avem 2 conditii, una pentru departament, una pentru salariu < 6000
UPDATE angajat 
SET salariu = salariu + 500
WHERE id_departament = 1 AND salariu < 6000;

# majorarea salariului angajatilor din departamentele intre 1 si 7
UPDATE angajat
set salariu = salariu * 1.1
where id_departament BETWEEN 1 AND 7;

# statistici pe tabela angajat: salariu minim, mediu, maxim
SELECT 
MIN(salariu) AS salariu_minim, # cuvantul cheie AS poate fi omis - este un keyword pentru alias
MAX(salariu) AS salariu_maxim,
AVG(salariu) AS salariu_mediu
FROM angajat;

# nume, prenume, salariu pt angajatii cu salariu peste 5000 lei
SELECT id, nume, prenume, id_departament, salariu as salariu_curent
FROM angajat
WHERE salariu > 5000;

# cati angajati au salariu peste 5000
SELECT COUNT(*)  nr_angajati  # pot pune un alias si fara keyword-ul AS
FROM angajat
WHERE salariu > 5000;

select * from angajat;

# cati angajati si-au dat demisia
SELECT COUNT(*)
FROM angajat
WHERE data_demisie IS NOT NULL;

# angajatii curenti
SELECT nume, prenume, id_departament
FROM angajat
WHERE data_demisie IS NULL;

# angajatii din dept 1 si 3
SELECT * FROM angajat
where id_departament in (1, 3);

SELECT * FROM angajat
WHERE id_departament = 1 OR id_departament =3;

# angajatii din dept 1 si 3 in ordine descrescatoare dupa nume (ordonati descrescator dupa nume)
SELECT * FROM angajat
where id_departament in (1, 3)
ORDER BY nume DESC;

# angajatii din dept 1 si 3 in ordine descrescatoare dupa nume si dept (ordonati descrescator dupa nume si dept)
SELECT * FROM angajat
where id_departament in (1, 3)
ORDER BY id_departament, nume DESC;

/*SELECT *
FROM <tabela>
WHERE <conditie>
ORDER BY <conditie>;*/

# afisam angajatii din departamentele cu id-uri cuprinse intre 1 si 5
SELECT * FROM angajat
WHERE id_departament BETWEEN 1 AND 5;

# angajatii cu salariu intre 4000 si 6000
SELECT * FROM angajat
WHERE salariu BETWEEN 4000 AND 6000;

# angajatii din departamentele 1, 2, 3
SELECT * FROM angajat
where id_departament IN (1, 2, 3);

# care departamente au angajati
SELECT DISTINCT id_departament AS id_dep # folosim DISTINCT pentru a nu afisa valori duplicate
FROM angajat
WHERE data_demisie IS NULL
ORDER BY id_dep;

select * from angajat;

# % - wildcard = 0 sau oricate caractere
# toti angajatii al caror nume incepe cu litera p
SELECT *
FROM angajat
WHERE nume LIKE 'p%';

# toti angajatii care au litera n in nume
SELECT *
FROM angajat
WHERE nume LIKE '%n%';

# persoanele care au demisionat anul acesta
SELECT *
FROM angajat
WHERE YEAR(data_demisie) = YEAR(CURDATE());

# persoanele angajate in 2019
SELECT *
FROM angajat
WHERE YEAR(data_angajare) = 2019;

# angajatul cu cea mai mare vechime
# 1. toti angajatii sortati ascendent dupa data_angagare
SELECT *
FROM angajat
WHERE data_demisie IS NULL
ORDER BY data_angajare;

# 2. iau doar primul angajat din query-ul de mai sus
SELECT *
FROM angajat
WHERE data_demisie IS NULL
ORDER BY data_angajare
LIMIT 1;

# al doilea cel mai vechi angajat
# limit n, m - sar peste primele n rezultate, si afisez pe urmatoarele m
SELECT *
FROM angajat
WHERE data_demisie IS NULL
ORDER BY data_angajare
LIMIT 1,1;

# al treilea cel mai vechi angajat
SELECT *
FROM angajat
WHERE data_demisie IS NULL
ORDER BY data_angajare
LIMIT 2,1;









