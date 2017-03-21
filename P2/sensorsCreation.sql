/*
sqlite3 sensors.bd < sensorsCreation.sql >out.txt
*/
DROP TABLE IF EXISTS sensors;
DROP TABLE IF EXISTS calib_temp;
DROP TABLE IF EXISTS calib_light;

CREATE TABLE IF NOT EXISTS sensors (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 result_time  DATETIME,
 epoch INT,
 nodeid INT,
 light INT,
 temp INT,
 voltage INT) ;


INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 09:10:18',639,1,555,26,400);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 10:20:10',653,1,556,12,420);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 10:30:11',683,1,557,38,430);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 11:33:15',712,1,558,15,433);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 11:40:23',715,1,560,0,512);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 12:42:28',725,1,562,27,323);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES (DATETIME('now'),727,1,555,20,401);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES (DATETIME('now'),729,1,566,12,333);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES (DATETIME('now'),732,1,568,13,0);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 09:10:18',639,2,555,0,325);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 10:20:10',653,2,556,5,386);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 10:30:11',683,2,557,10,402);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 11:33:15',712,2,558,11,415);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 11:40:23',715,2,560,12,411);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 12:42:28',725,2,562,13,450);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES (DATETIME('now'),727,2,564,14,300);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES (DATETIME('now'),729,2,566,15,400);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES (DATETIME('now'),734,2,568,16,408);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 09:10:18',639,3,555,-2,418);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 10:20:10',653,3,556,0,300);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 10:30:11',683,3,557,2,0);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 11:33:15',712,3,558,4,420);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 11:40:23',715,3,560,10,478);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES ('2015-03-05 12:42:28',725,3,562,12,499);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES (DATETIME('now'),727,3,564,13,501);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES (DATETIME('now'),729,3,566,14,512);
INSERT INTO sensors (result_time,epoch,nodeid,light,temp,voltage) VALUES (DATETIME('now'),729,3,568,15,534);


CREATE TABLE calib_temp as select temp, avg(temp)+temp as calib from sensors group by temp;
CREATE TABLE calib_light as select light, avg(light)+light as calib from sensors group by light;

.mode column
.header on

.print "\n Exercici 1:\n"
select id, result_time from sensors where light > 550;

.print "\n Exercici 2:\n---CAP SENSOR TE DADES DAQUESTES HORES, POSEM DESDE LES 11 FINS LES 12---\n"
select avg(light) from sensors where nodeid=1 and time(result_time) between "11:00:00" and "12:00:00";

.print "\n Exercici 3:\n"
select avg(light), avg(temp) from sensors where voltage < 418 and time(result_time) between "09:00:00" and "12:00:00";

.print "\n Exercici 4:\n"
/*
select temp from sensors where nodeid = 2 group by strftime("%H", result_time) having time(result_time) between "08:00:00" and "12:00:00";
.print "\n"*/
select calib from calib_temp where temp in
      (select temp from sensors where nodeid = 2 and time(result_time) between "08:00:00" and "12:00:00" group by (result_time));

.print "\n Exercici 5:\n"
/*
taula de dades entrants a la hora concreta pels sensors 1 i 2.
select result_time, min(epoch) as epoch1, max(epoch) as epoch2 from sensors
                          where nodeid = 1 or nodeid = 2 group by result_time;
.print "\n"*/
select result_time, epoch1, epoch2, epoch2 - epoch1 as computation from
        (select result_time, min(epoch) as epoch1, max(epoch) as epoch2 from sensors
                where nodeid = 1 or nodeid = 2 group by result_time) where epoch2 - epoch1 >= 1;

.print "\n Exercici 6:\n"
select epoch from(select epoch, count(nodeid) as n from sensors group by epoch) where n != 3;
