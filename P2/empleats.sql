PRAGMA FOREIGN_KEY=ON;

DROP TABLE IF EXISTS FEINA;
DROP TABLE IF EXISTS EMPLEAT;
DROP TABLE IF EXISTS EMPRESA;
DROP TABLE IF EXISTS MANAGER;

CREATE TABLE EMPLEAT (
    ID_EMPLEAT int(3) PRIMARY KEY,
    CARRER varchar(20) not null,
    CIUTAT  varchar(20) not null
);
CREATE TABLE FEINA (
    ID_EMPLEAT INT(3) not null PRIMARY KEY,
    ID_EMPRESA VARCHAR(3) not null,
    SALARI INT(10) not null,
    /*FOREIGN KEY (ID_EMPRESA) REFERENCES EMPRESA(ID_EMPRESA),*/
    FOREIGN KEY (ID_EMPLEAT) REFERENCES EMPLEAT(ID_EMPLEAT)
);
CREATE TABLE EMPRESA(
  ID_EMPRESA VARCHAR(16) PRIMARY KEY,
  CIUTAT varchar(16),
  foreign key (ID_EMPRESA) references FEINA(ID_EMPRESA)
);

CREATE TABLE MANAGER(
  ID_EMPLEAT int(3) PRIMARY KEY,
  ID_EMPLEAT_COORDINADOR int(3) not null,
  foreign key (ID_EMPLEAT) REFERENCES EMPLEAT(ID_EMPLEAT),
  foreign key (ID_EMPLEAT_COORDINADOR) references EMPLEAT(ID_EMPLEAT)
);
INSERT INTO EMPLEAT VALUES(1,"Pio","Murcia");
INSERT INTO EMPLEAT VALUES(2,"As","Madrid");
INSERT INTO EMPLEAT VALUES(3,"Z","Barcelona");
INSERT INTO EMPLEAT VALUES(4,"Barcelona","Murcia");
INSERT INTO EMPLEAT VALUES(5,"A","Madrid");
INSERT INTO EMPLEAT VALUES(6,"B","Terrasa");
INSERT INTO EMPLEAT VALUES(7,"C","Mataro");
INSERT INTO EMPLEAT VALUES(8,"E","Manresa");
INSERT INTO EMPLEAT VALUES(22,"F","Badalona");

INSERT INTO FEINA VALUES(1,"Bank Newton",1000);
INSERT INTO FEINA VALUES(2,"A",2000);
INSERT INTO FEINA VALUES(3,"B",1500);
INSERT INTO FEINA VALUES(4,"Bank Newton",1100);
INSERT INTO FEINA VALUES(5,"A",750);
INSERT INTO FEINA VALUES(6,"C",750);
INSERT INTO FEINA VALUES(7,"B",750);
INSERT INTO FEINA VALUES(8,"C",750);
INSERT INTO FEINA VALUES(22,"B",750);

INSERT INTO EMPRESA VALUES("Bank Newton", "Murcia" ) ;
INSERT INTO EMPRESA VALUES("A", "Madrid" );
INSERT INTO EMPRESA VALUES("B", "Barcelona" );
INSERT INTO EMPRESA VALUES("C","Manresa");

INSERT INTO MANAGER VALUES(1, 4);
INSERT INTO MANAGER VALUES(2, 5);
INSERT INTO MANAGER VALUES(3, 3);
INSERT INTO MANAGER VALUES(4, 4);
INSERT INTO MANAGER VALUES(5, 5);
INSERT INTO MANAGER VALUES(6, 6);
INSERT INTO MANAGER VALUES(7, 3);
INSERT INTO MANAGER VALUES(8, 6);
INSERT INTO MANAGER VALUES(22, 3);
.header on
.mode column
.print  "\nexercisi 1: \n"
select  ID_EMPLEAT , CIUTAT from  EMPLEAT  where ID_EMPLEAT in(select ID_EMPLEAT from FEINA  where ID_EMPRESA = "Bank Newton" ) ;

.print  "\nExercisi 2 : \n"
select  ID_EMPLEAT , CIUTAT from  EMPLEAT  where ID_EMPLEAT in(select ID_EMPLEAT from FEINA  where ID_EMPRESA = "Bank Newton" and salari > 1000 );

.print  "\nExercisi 3 : \n";
select ID_EMPLEAT from FEINA where ID_EMPRESA != 'Bank Newton';

.print  "\nExercisi 4 "
select  ID_EMPLEAT from  FEINA where  SALARI > (select max(SALARI)  from FEINA where ID_EMPRESA='Bank Newton');

.print  "\nExercisi 5"
select ID_EMPRESA,COUNT(*) AS NUM_EMPLEATS from FEINA group by (ID_EMPRESA) ORDER by NUM_EMPLEATS DESC limit 1;

.print  "\NEercisi 6:"
UPDATE EMPLEAT set CIUTAT='Barcelona' where ID_EMPLEAT=22;
select * from empleat;

.print  "\n Exercisi 7"
update feina set salari=salari*1.10 where id_empleat in (select ID_EMPLEAT_COORDINADOR from manager);
select * from feina;

select ID_EMPLEAT from EMPLEAT where CIUTAT in (select CIUTAT from EMPRESA where EMPRESA.CIUTAT = EMPLEAT.CIUTAT);

.print "\n Exercisi 9"
select ID_EMPLEAT from empleat where ciutat in
    (select ciutat from empleat where ID_EMPLEAT in
        (select ID_EMPLEAT_COORDINADOR from manager))and ID_EMPLEAT not in
            (select ID_EMPLEAT_COORDINADOR from manager);

.print "\n Exercisi 10"
delete from feina where id_empresa='Bank Newton';

select * from feina;
