CREATE TABLE USUARIS(
  email varchar(32) PRIMARY KEY,
  nom varchar(16) NOT NULL,
  cognom varchar(24) NOT NULL,
  poblacio varchar(24) NOT NULL,
  dataNaixement date,
  pwd varchar(16) NOT NULL
);

CREATE TABLE AMISTATS(
  email1 varchar(32),
  email2 varchar(32),
  estat varchar(10),
  PRIMARY KEY (email1, email2)
);

INSERT INTO USUARIS VALUES ('peregarcia@upc.edu', 'Pere', 'Garcia', 'Manresa', '2017-01-01', '2017');
INSERT INTO USUARIS VALUES ('adriiauguets@gmail.com', 'Adria', 'Auguets', 'Castellgali', '1995-01-01','0000');
INSERT INTO USUARIS VALUES ('pavelmacu@gmail.com', 'Pavel', 'Macutela', 'Tremp', '1876-12-25','0000');
INSERT INTO USUARIS VALUES ('Bases@Manresa.cat', 'Bases', 'Manresa', 'Manresa', '1892-03-25','1234');
INSERT INTO USUARIS VALUES ('bolibic@gmail.com', 'Boli', 'Bic', 'Paris', '1798-01-15','0000');
INSERT INTO USUARIS VALUES ('PepeF@gmail.com', 'Pepe', 'F', 'Desconegut', '2012-10-03','0000');
INSERT INTO USUARIS VALUES ('senyorAlbet@gmail.com','Joan', 'Albets', 'Manresa', '1975-03-03','0123');
INSERT INTO USUARIS VALUES ('algu@gmail.com','Desconegut','Secret', 'Manresa', '1002-01-19', 'xvii');
INSERT INTO USUARIS VALUES ('EnricPrat@catalunya.cat', 'Enric', 'PratdelaRiba', 'Castellterçol', '1870-11-29', '4321');
INSERT INTO USUARIS VALUES ('ja@gmail.com','Jordi','Alba', 'HospitaletDeLlobregat', '1989-03-01', '0000');
INSERT INTO USUARIS VALUES ('AVilella@gmail.com','Ana','Vilella', 'Vielha', '1989-03-01', '0000');



INSERT INTO AMISTATS VALUES ('EnricPrat@catalunya.cat', 'peregarcia@upc.edu', 'Acceptada');
INSERT INTO AMISTATS VALUES ('EnricPrat@catalunya.cat', 'ja@upc.edu', 'Acceptada');
INSERT INTO AMISTATS VALUES ('peregarcia@upc.edu', 'Bases@Manresa.cat', 'Acceptada');
INSERT INTO AMISTATS VALUES ('EnricPrat@catalunya.cat', 'Bases@Manresa.cat', 'Acceptada');
INSERT INTO AMISTATS VALUES ('adriiauguets@gmail.com', 'pavelmacu@gmail.com', 'Acceptada');
INSERT INTO AMISTATS VALUES ('adriiauguets@gmail.com', 'ja@gmail.com', 'Acceptada');
INSERT INTO AMISTATS VALUES ('adriiauguets@gmail.com', 'peregarcia@upc.edu', 'Acceptada');
INSERT INTO AMISTATS VALUES ('adriiauguets@gmail.com', 'bolibic@gmail.com', 'Pendent');
INSERT INTO AMISTATS VALUES ('pavelmacu@gmail.com', 'PepeF@gmail.com', 'Rebutjada');
INSERT INTO AMISTATS VALUES ('pavelmacu@gmail.com', 'peregarcia@upc.edu', 'Rebutjada');
INSERT INTO AMISTATS VALUES ('Algu@gmail.cat', 'senyorAlbet@gmail.com', 'Acceptada');

/* -Retorna els Usuaris de manresa.
 * sqlite> select email, nom, cognom, poblacio, dataNaixement from usuaris where poblacio == 'Manresa';
 *
 * -Retorna els Albets
 * select email from usuaris where cognom == 'Albets';
 *
 * -els amics que tenen pere Garcia
 * (no va)select nom, cognom from usuaris where email in(select email2 from amistats where email1=(select email from usuaris where nom == 'Pere' and cognom == 'Garcia')) or email in(select email1 from amistats where email2 = (select email from usuaris where nom == 'Pere' and cognom == 'Garcia));
 * (va pero no crec que sigui el que demanen) select nom, cognom from usuaris where email in(select email1 from amistats where email2=(select email from usuaris where nom == 'Pere' and cognom == 'Garcia'));
 *
 * -Amics del Pere que no son del Alba
 *  sqlite> select email from usuaris where email in(select email1 from amistats where email2=(select email from usuaris wh'Pere' and cognom='Garcia')) EXCEPT select email from usuaris where email in (select email1 from amistats where email2=(select email from usuaris where nom='Jordi' and cognom='Alba'));
 *
 * -Recompte de rebutjats
 * sqlite> select COUNT(*) from amistats where estat='Rebutjada';
 *
 * -Amics d'algu que viuen a manresa (algu = adria auguets)
 * sqlite> select nom, cognom from usuaris where email in(select email2 from amistats where email1=(select email from usuaris where nom='Adria' and cognom='Auguets') and poblacio='Manresa');
 *
 *- Nombre de Rebutjats
 * sqlite3> select nom, cognom, COUNT(*) from usuaris where email in(select email1 from amistats where estat='Rebutjada');
 *
 * - No amics de la nova registrada
 * sqlite> select nom, cognom from usuaris where email in(select email1 from amistats where email2!=(select email from usuaris where nom='Ana' and cognom='Vilella'));
 */
