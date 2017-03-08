/*sqlite> .header on
sqlite> .mode column*/

CREATE TABLE PK(
   PLACE 		INTEGER UNIQUE 			NOT NULL, /*autoincrement automatic */
   NP			CHAR(7)	PRIMARY KEY		NOT NULL,
   COLOR		INT     NOT NULL,
   BRAND		CHAR(10),
   DATA			CHAR(19)
   );



INSERT INTO PK (PLACE,NP,COLOR,BRAND, DATA) 
VALUES (23 , '1234ASD', 'Red','Opel', strftime('%s', 'now'));

INSERT INTO PK (PLACE,NP,COLOR,BRAND, DATA) 
VALUES (0 , '1234ASQ', 'Red', 'Ferrari', strftime('%s','now'));

INSERT INTO PK (PLACE,NP,COLOR,BRAND, DATA) 
VALUES (2 , '1234ASE', 'Blue', 'Tata', strftime('%s','now'));

INSERT INTO PK (PLACE,NP,COLOR,BRAND, DATA) 
VALUES (3 , '1234ASU', 'Blue', 'Toyota', strftime('%s','now'));

INSERT INTO PK (PLACE,NP,COLOR,BRAND, DATA) 
VALUES (1 , '1234ASI', 'Black', 'Opel', strftime('%s','now'));

INSERT INTO PK (PLACE,NP,COLOR,BRAND, DATA) 
VALUES (6 , '1234ASK', 'White', 'Renault', strftime('%s','now'));

INSERT INTO PK (PLACE,NP,COLOR,BRAND, DATA) 
VALUES (25 , '1234ASL', 'White', 'Honda', strftime('%s','now'));

INSERT INTO PK (PLACE,NP,COLOR,BRAND, DATA) 
VALUES (22 , '1234ASB', 'Blue', 'Honda', strftime('%s','now'));


/*RETORNA SEGONS*/
select strftime('%s','now')-DATA from PK where PLACE = '0';

/*Retorna els dies*/
select (strftime('%s','now')-DATA)/3600/24 from PK where PLACE = '0';