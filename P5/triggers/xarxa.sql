drop table if exists usuaris;
drop table if exists amistats;
drop table if exists preferencies;
drop table if exists amicsPotencial;

create table usuaris(
    ID int primary key,
    nom text,
    grau int);
create table amistats(
    ID1 int,
    ID2 int,
    primary key (ID1,ID2),
    FOREIGN KEY (ID1) REFERENCES usuaris(ID),
    FOREIGN KEY (ID2) REFERENCES usuaris(ID));
create table preferencies(
    ID1 int,
    ID2 int,
    primary key (ID1,ID2),
    FOREIGN KEY (ID1) REFERENCES usuaris(ID),
    FOREIGN KEY (ID2) REFERENCES usuaris(ID));
create table amicsPotencial(
    ID1 int,
    ID2 int ,
    grau INT,
    PRIMARY KEY(ID1,ID2),
    FOREIGN KEY (ID1) REFERENCES usuaris(ID),
    FOREIGN KEY (ID2) REFERENCES usuaris(ID));

insert into usuaris values (1510, 'Jordan', 9);
insert into usuaris values (1689, 'Gabriel', 9);
insert into usuaris values (1381, 'Tiffany', 9);
insert into usuaris values (1709, 'Cassandra', 9);
insert into usuaris values (1101, 'Haley', 10);
insert into usuaris values (1782, 'Andrew', 10);
insert into usuaris values (1468, 'Kris', 10);
insert into usuaris values (1641, 'Brittany', 10);
insert into usuaris values (1247, 'Alexis', 11);
insert into usuaris values (1316, 'Austin', 11);
insert into usuaris values (1911, 'Gabriel', 11);
insert into usuaris values (1501, 'Jessica', 11);
insert into usuaris values (1304, 'Jordan', 12);
insert into usuaris values (1025, 'John', 12);
insert into usuaris values (1934, 'Kyle', 12);
insert into usuaris values (1661, 'Logan', NULL );
insert into usuaris values (666,'Satan',22);

insert into amistats values (1510, 1381);
insert into amistats values (1510, 1689);
insert into amistats values (1689, 1709);
insert into amistats values (1381, 1247);
insert into amistats values (1709, 1247);
insert into amistats values (1689, 1782);
insert into amistats values (1782, 1468);
insert into amistats values (1782, 1316);
insert into amistats values (1782, 1304);
insert into amistats values (1468, 1101);
insert into amistats values (1468, 1641);
insert into amistats values (1101, 1641);
insert into amistats values (1247, 1911);
insert into amistats values (1247, 1501);
insert into amistats values (1911, 1501);
insert into amistats values (1501, 1934);
insert into amistats values (1316, 1934);
insert into amistats values (1934, 1304);
insert into amistats values (1304, 1661);
insert into amistats values (1661, 1025);
insert into amistats select ID2, ID1 from amistats;

insert into preferencies values(1689, 1709);
insert into preferencies values(1709, 1689);
insert into preferencies values(1782, 1709);
insert into preferencies values(1911, 1247);
insert into preferencies values(1247, 1468);
insert into preferencies values(1641, 1468);
insert into preferencies values(1316, 1304);
insert into preferencies values(1501, 1934);
insert into preferencies values(1934, 1501);
insert into preferencies values(1025, 1101);

/*Tasca 1*/
create trigger potencial AFTER insert on usuaris
begin
INSERT INTO amicsPotencial SELECT new.ID,ID,grau from usuaris where grau=new.grau;
END;

/*Tasca 2*/
create trigger graUsuaris AFTER insert on usuaris
when new.grau < 9 or new.grau > 12
begin
	UPDATE usuaris set grau = NULL where ID=new.ID;
end;

create trigger graUsuaris1 AFTER insert on usuaris
when new.grau is NULL
begin
	UPDATE usuaris set grau=9 where ID=new.ID;
end;
/*tasca 3*/
/*Te un petit error, no creus? a la linia 104.
 *
 * create trigger relacio_simetrica1 BEFORE delete on amistats
 * begin
 * delete from amistats where (ID1=old.ID2 and old.ID2 and ID2 = old.ID1 );
 * end;
 */
create trigger selacio_simetrica1 BEFORE delete on amistats
  begin
    delete from amistats where (ID1=old.ID2 and ID2 = old.ID1);
  end;

create trigger relacio_simetrica AFTER insert on amistats
begin
	INSERT into amistats values (new.ID2,new.ID1);
end;

/*Tasca4*/

create trigger elimina_graduats after update of grau on usuaris for each row
when (new.grau >= 12)
begin
	delete from preferencies where (ID1 in (SELECT ID FROM usuaris where ID = new.id))or
                                 (ID2 in (select ID from usuaris where ID = new.id));
	delete from amistats where (ID1 in (select ID from usuaris where ID = new.id)) or
                             (ID2 in (select ID from usuaris where ID = new.id));
      	delete from usuaris where ID = new.id;
end;
/*
create trigger incrementa after update on usuaris
begin
	delete from  usuaris where ID=new.ID;
end;
create trigger increment_amics after update on usuaris
begin
	update usuaris set grau=new.grau where grau=new.grau -1 and  ID in (select ID2 from amistats where ID1=new.ID);
end;
*/
