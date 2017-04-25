PRAGMA foreign_key = ON;
DROP TABLE IF EXISTS DEPARTAMENTS;
DROP TABLE IF EXISTS EMPLEATS;
DROP TABLE IF EXISTS CLIENTS;
DROP TABLE IF EXISTS COMANDES;
DROP TABLE IF EXISTS DETALL;
DROP TABLE IF EXISTS PRODUCTES;

CREATE TABLE IF NOT EXISTS DEPARTAMENTS(
  dep     int(2),
  depnom  text,
  loc     text,
  PRIMARY KEY (dep)
);

INSERT INTO DEPARTAMENTS VALUES (01, 'PRODUCCIO', 'MANRESA');
INSERT INTO DEPARTAMENTS VALUES (02, 'MKT', 'LLEIDA');
INSERT INTO DEPARTAMENTS VALUES (03, 'VENDES', 'GIRONA');
INSERT INTO DEPARTAMENTS VALUES (04, 'RRHH', 'BARCELONA');
INSERT INTO DEPARTAMENTS VALUES (20, 'LOGISTICA', 'BARCELONA');


CREATE TABLE IF NOT EXISTS EMPLEATS(
  codi int,
  cognom text not null,
  ofici text,
  alta date,
  salari int,
  comisio int,
  cap int,
  dep int(2) not null,
  PRIMARY KEY (codi),
  FOREIGN KEY (dep) REFERENCES DEPARTAMENTS(dep),
  FOREIGN KEY (cap) REFERENCES EMPLEATS(codi)
);

INSERT INTO EMPLEATS VALUES (1,'MAS','VENEDOR','1970-02-20', 10000,10000,10,01);
INSERT INTO EMPLEATS VALUES (10,'SAM','CAP','1910-02-02', 1000000,100000,NULL,01);
INSERT INTO EMPLEATS VALUES (2,'JOPSEPHO','VENEDOR','1972-02-02', 230000,100000,10,01);
INSERT INTO EMPLEATS VALUES (3,'NEGRO','COMPRADOR','1980-02-02', 50000,100000,10,02);
INSERT INTO EMPLEATS VALUES (4,'BLANCO','VENEDOR','1986-02-02', 400000,100000,20,02);
INSERT INTO EMPLEATS VALUES (5,'GIL','VENEDOR','1999-02-02', 450000,100000,20,03);
INSERT INTO EMPLEATS VALUES (20,'CACATUA','DIRECTOR','1987-02-02', 99900000,100000,NULL,03);
INSERT INTO EMPLEATS VALUES (6,'ESTIARTE','VIGILANT','1979-02-02', 10,100000,20,04);
INSERT INTO EMPLEATS VALUES (7,'CASADO','COMPRADOR','1990-02-02', 20000,100000,20,04);
INSERT INTO EMPLEATS VALUES (8,'SALA','VIGILANT','1988-02-02', 1,100000,20,04);
INSERT INTO EMPLEATS VALUES (9,'PEPER','VENEDOR','1900-02-02', 1000,100000,20,20);
INSERT INTO EMPLEATS VALUES (12,'PEP','COMPRADOR','1998-02-02', 1000,100000,20,20);
INSERT INTO EMPLEATS VALUES (11,'PEPE','DIRECTOR','1997-02-02', 1000,100000,NULL,02);

CREATE TABLE IF NOT EXISTS CLIENTS(
  codi int,
  nom text,
  addr text,
  ciutat text,
  cp int(5),
  telf int(9),
  limcredit int,
  representant int,
  observacions text,
  FOREIGN KEY (representant) REFERENCES EMPLEATS(codi)
);

INSERT INTO CLIENTS VALUES (100, 'JAMES', 'calle falsa 123', 'Springfield', 12345, 123456789, 1000 ,1, 'ASDASDF');
INSERT INTO CLIENTS VALUES (100, 'PEPE', 'calle falsa 123', 'Springfield', 12345, 123456789, 1000 ,10, 'ASDASDF');
INSERT INTO CLIENTS VALUES (100, 'CRISTIANO', 'calle falsa 123', 'Springfield', 12345, 123456789, 1000 ,2, 'ASDASDF');
INSERT INTO CLIENTS VALUES (100, 'BALE', 'calle falsa 123', 'Springfield', 12345, 123456789, 1000 ,5, 'ASDASDF');
INSERT INTO CLIENTS VALUES (100, 'RAMOS', 'calle falsa 123', 'Springfield', 12345, 123456789, 1000 ,8, 'ASDASDF');

CREATE TABLE IF NOT EXISTS COMANDES(
  codi int PRIMARY KEY,
  data date,
  tipus int,
  client int,
  data_tramesa date,
  total int,
  FOREIGN KEY (client) REFERENCES clients(codi)
);
INSERT INTO COMANDES VALUES (610, '2016-09-07', 1, 100, '2017-01-08', 100);


CREATE TABLE IF NOT EXISTS DETALL(
  codi int PRIMARY KEY,
  quantitat int,
  preu int,
  import int,
  FOREIGN KEY (codi) REFERENCES COMANDES(codi)
);

INSERT INTO DETALL VALUES (610, 10, 100890, 58);

CREATE TABLE IF NOT EXISTS PRODUCTES(
  codi int,
  descripcio text
);

.header on
.mode column

.print "\n1. Mostrar els empleats (codi i cognom) juntament amb el codi i nom del departament al qual pertanyen."
SELECT e.codi, e.cognom, d.dep, d.depnom FROM EMPLEATS e INNER JOIN DEPARTAMENTS d ON e.dep = d.dep;

.print "\n2. Mostrar tots els departaments (codi i descripció) acompanyats del salari més alt dels seus empleats"
SELECT d.dep as Departament, d.depnom as Nom, e.salari FROM DEPARTAMENTS d INNER JOIN EMPLEATS e ON d.dep = e.dep
        GROUP BY d.dep ORDER BY e.salari DESC;

.print "\n3. Mostrar, en l’esquema empresa, tots els empleats acompanyats dels clients de qui són representants."
SELECT e.cognom as empleat, c.nom as client FROM EMPLEATS e LEFT JOIN CLIENTS c ON e.codi = c.representant;

.print "\n4. Mostrar tots els clients acompanyats de l’empleat que tenen com a representant."
SELECT c.nom as client, e.cognom as empleat FROM CLIENTS c LEFT JOIN EMPLEATS e ON e.codi = c.representant;

.print "\n5. Exercici 1(repetit)"

.print "\n6. Exercici 2(repetit)"

.print "\n7. Mostrar els empleats de cada departament que tenen un salari major que el salari mitjà del mateix departament."
SELECT e.dep, e.cognom, e.salari FROM EMPLEATS e INNER JOIN (SELECT d.dep, AVG(e.salari) AS salari
    FROM EMPLEATS e INNER JOIN DEPARTAMENTS d ON e.dep = d.dep GROUP BY d.dep)
          e_avg ON e.dep = e_avg.dep AND e.salari > e_avg.salari;


.print "\n8. Mostrar els empleats que tenen el mateix ofici que l’ofici que té l’empleat de cognom SALA."
SELECT * FROM EMPLEATS WHERE ofici = (SELECT ofici FROM EMPLEATS WHERE cognom = "SALA");

.print "\n9. Mostrar els noms i oficis dels empleats del departament 20 la feina dels quals coincideixi amb la d’algun empleat del departament de ’VENDES’."
SELECT e1.cognom, e1.ofici
    FROM EMPLEATS e1 INNER JOIN EMPLEATS e2 ON e1.ofici = e2.ofici
                INNER JOIN DEPARTAMENTS d ON e2.dep = d.dep
    WHERE e1.dep = 20 AND d.depnom = "VENDES" GROUP BY(e1.ofici);

.print "\n10. Mostrar els empleats que efectuin la mateixa feina que NEGRO o que tinguin un salari igual o superior al de GIL."
SELECT DISTINCT e1.*
  FROM EMPLEATS e1 INNER JOIN EMPLEATS e2 ON (e1.ofici = e2.ofici AND e2.cognom = "NEGRO") OR
                    e1.salari >= (SELECT salari FROM EMPLEATS WHERE cognom = "GIL")
                            ORDER BY e1.codi ASC;
.print "\n11. Mostrar els empleats (codi, cognom i nom del departament) de l’empresa que tenen el rang de director i ordenats pel cognom."
SELECT e.codi, e.cognom, d.depnom FROM EMPLEATS e LEFT JOIN DEPARTAMENTS d ON e.dep = d.dep WHERE ofici = "DIRECTOR" ORDER BY e.cognom ASC;

.print "\n12. Mostrar l’import global que cada departament assumeix anualment en concepte de nòmina dels empleats i ordenat descendentment per l’import global."
SELECT dep as Departament, SUM(salari) as Salari_Global FROM EMPLEATS GROUP BY dep ORDER BY SUM(salari) ASC;

.print "\n13. Mostrar els departaments ordenats ascendentment per l’antiguitat dels empleats."
SELECT d.depnom from DEPARTAMENTS d INNER JOIN EMPLEATS e where e.dep = d.dep GROUP BY d.depnom ORDER BY e.alta DESC;
