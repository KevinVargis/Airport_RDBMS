DROP DATABASE IF EXISTS DNA_PROJECT;

CREATE DATABASE DNA_PROJECT;

USE DNA_PROJECT;


CREATE TABLE EMPLOYEE (
    EMPLOYEE_ID VARCHAR(50) NOT NULL,
    GENDER VARCHAR(50) ,
    FIRST_NAME VARCHAR(50) NOT NULL,
    SECOND_NAME VARCHAR(50) NOT NULL,
    ROLE VARCHAR(50) NOT NULL ,
    PRIMARY KEY (EMPLOYEE_ID)
);

ALTER TABLE EMPLOYEE ALTER GENDER SET DEFAULT'OTHER';

CREATE TABLE MEAL_PACKAGE (
    EMPLOYEE_ID VARCHAR(50) NOT NULL,
    CLASS VARCHAR(50) NOT NULL CHECK (CLASS='ECONOMY'OR CLASS='LUXURY'),
    TYPE VARCHAR(50) NOT NULL CHECK (TYPE='VEG'OR TYPE='NON-VEG'),
     MEAL_NO INT NOT NULL,
     PRIMARY KEY (EMPLOYEE_ID, MEAL_NO),
     FOREIGN KEY (EMPLOYEE_ID) REFERENCES EMPLOYEE(EMPLOYEE_ID));

CREATE TABLE PASSENGER (
    PASSPORT_ID VARCHAR(50) NOT NULL ,
    TICKET_NUMBER VARCHAR(50) NOT NULL,
    GENDER VARCHAR(50) DEFAULT'OTHER',
    FIRST_NAME VARCHAR(50) NOT NULL,
    LAST_NAME VARCHAR(50) NOT NULL,
    DOB DATE NOT NULL ,
    AGE_GROUP VARCHAR(50) ,
    PRIMARY KEY (PASSPORT_ID),
    UNIQUE (TICKET_NUMBER)
);

CREATE TABLE FLIGHT(
    FLIGHT_NO VARCHAR(50) NOT NULL,
    AIRLINE VARCHAR(30) NOT NULL,
    DESTINATION VARCHAR(30) NOT NULL,
    DATE DATE NOT NULL,
    SLOT INT NOT NULL,
    ARRIVAL_OR_TAKE_OFF_LOCATION VARCHAR(50) NOT NULL,
    BOARDING_TIME TIMESTAMP NOT NULL,
    PRIMARY KEY (FLIGHT_NO)
);

CREATE TABLE AIRLINE_EMPLOYEE(
    A_EMPLOYEE_ID VARCHAR(50) NOT NULL,
    FIRST_NAME VARCHAR(50) NOT NULL,
    LAST_NAME VARCHAR(50) NOT NULL,
    POSITION VARCHAR(50) NOT NULL,
    AIRLINE VARCHAR(50) NOT NULL,
    PRIMARY KEY (A_EMPLOYEE_ID)
);

CREATE TABLE LUGGAGE_BAG(
    PASSPORT_ID VARCHAR(50) NOT NULL,
    BAG_NO INT NOT NULL,
    LENTGH INT NOT NULL,
    BREADTH INT NOT NULL,
    HEIGHT INT NOT NULL,
    PRIMARY KEY(PASSPORT_ID,BAG_NO),
    FOREIGN KEY (PASSPORT_ID) REFERENCES PASSENGER(PASSPORT_ID)
);

CREATE TABLE FLIES_ON(
    FLIGHT_NO VARCHAR(50) NOT NULL,
    PASSPORT_ID VARCHAR(50) NOT NULL,
    PRIMARY KEY(PASSPORT_ID),
    FOREIGN KEY(FLIGHT_NO) REFERENCES FLIGHT(FLIGHT_NO),
    FOREIGN KEY(PASSPORT_ID) REFERENCES PASSENGER(PASSPORT_ID)
);

CREATE TABLE WORKS_ON(
    FLIGHT_NO VARCHAR(50) NOT NULL,
    A_EMPLOYEE_ID VARCHAR(50) NOT NULL,
    PRIMARY KEY(FLIGHT_NO,A_EMPLOYEE_ID),
    FOREIGN KEY(FLIGHT_NO) REFERENCES FLIGHT(FLIGHT_NO),
    FOREIGN KEY(A_EMPLOYEE_ID) REFERENCES AIRLINE_EMPLOYEE(A_EMPLOYEE_ID)
);

CREATE TABLE SUPPLIES_TO(
    PASSPORT_ID VARCHAR(50) NOT NULL,
    MEAL_NO INT NOT NULL,
    EMPLOYEE_ID VARCHAR(50) NOT NULL,
    PRIMARY KEY(PASSPORT_ID,MEAL_NO,EMPLOYEE_ID),
    FOREIGN KEY(PASSPORT_ID) REFERENCES PASSENGER(PASSPORT_ID),
    FOREIGN KEY(EMPLOYEE_ID,MEAL_NO) REFERENCES MEAL_PACKAGE (EMPLOYEE_ID,MEAL_NO)
);

CREATE TABLE SUPPLIES_TO_ON(
    PASSPORT_ID VARCHAR(50) NOT NULL,
    MEAL_NO INT NOT NULL,
    EMPLOYEE_ID VARCHAR(50) NOT NULL,
    A_EMPLOYEE_ID VARCHAR(50) NOT NULL,
    PRIMARY KEY(PASSPORT_ID,MEAL_NO,EMPLOYEE_ID,A_EMPLOYEE_ID),
    FOREIGN KEY(PASSPORT_ID) REFERENCES PASSENGER(PASSPORT_ID),
    FOREIGN KEY(EMPLOYEE_ID,MEAL_NO) REFERENCES MEAL_PACKAGE (EMPLOYEE_ID,MEAL_NO),
    FOREIGN KEY(A_EMPLOYEE_ID) REFERENCES AIRLINE_EMPLOYEE(A_EMPLOYEE_ID)
);

INSERT INTO `FLIGHT` VALUES ('03ef71a3','Emirates','Mumbai','2020-10-13','4','Hyderabad','2020-10-13 16:44:19'),
('1cf08c9a','Singapore Airlines','Bangalore','2021-07-21','3','Hyderabad','2021-07-21 07:07:21'),
('24c4b570','Qatar Airways','Hyderabad','2020-10-04','4','Kochi','2020-10-04 16:17:12'),
('99cbb790','Emirates','Hyderabad','2020-03-02','4','Bangalore','2020-03-02 11:01:57'),
('b9963d94','Etihad Airways','Hyderabad','2020-06-10','4','Kolkata','2020-06-10 06:37:30'); 

INSERT INTO `PASSENGER` VALUES ('05327c8e99','F8E4043A71','FEMALE','Jazmyn','Swaniawski','2019-09-13',NULL),
('12a39376f9','111F9D28A8','FEMALE','Paris','Kemmer','1971-07-31',NULL),
('15a3bcfea6','50A1ACBE01','FEMALE','Bernardo','Brekke','1986-03-25',NULL),
('17a3eaf2bb','4F4390FAF0','FEMALE','Sheridan','Schiller','1988-12-30',NULL),
('1b79f06bac','1D4EB59F2A','MALE','Glennie','Lynch','1978-04-14',NULL),
('226b48eb08','8A82D9F111','MALE','Triston','Schamberger','1971-04-20',NULL),
('228c0423e9','7D98AFCB7D','MALE','Kayden','Bergstrom','2008-05-15',NULL),
('297b758db3','1169D9E3F5','MALE','Paolo','Cassin','2008-05-11',NULL),
('2cee74327e','E4D1D7BCFA','MALE','Jeanne','Swift','1979-04-09',NULL),
('39b3e643e1','8255EBA2F9','FEMALE','Austin','Ledner','2013-06-22',NULL),
('443e33c16d','8774C572BD','FEMALE','Ferne','Mohr','1975-11-17',NULL),
('451d9c2d52','7D1D4EB59F','MALE','Raven','White','2007-11-01',NULL),
('48d75f43da','52BEAF8925','FEMALE','Laury','Cummerata','1993-06-13',NULL),
('4c9d42e19d','E0D529F3C9','FEMALE','Willa','Hudson','2010-12-13',NULL),
('4cb0435bc9','DB275C4778','FEMALE','Toy','Robel','1996-12-02',NULL),
('4cf27yj8i6','8A25ADBEB1','MALE','Julien','Kulas','1994-10-04',NULL),
('542a9095bb','2ABE5528EA','MALE','Shaun','Considine','1984-05-29',NULL),
('578c2878d8','D9F111252F','MALE','Delphine','Gleichner','1989-05-20',NULL),
('57c2316d8d','0FAF0934F4','FEMALE','Yolanda','Cormier','2012-10-24',NULL),
('5b62a08f59','EAB0C950A1','FEMALE','Geovany','Rowe','2004-08-27',NULL),
('5c21dc7d7f','C950A1ACBE','FEMALE','Wyman','Hintz','1988-01-31',NULL),
('5c9ca8eb5a','F252111F9D','FEMALE','Shanny','Spencer','2005-05-07',NULL),
('68f5a4806c','F95BE4D1D7','MALE','Melissa','Wisozk','1998-01-20',NULL),
('6a77722d20','5BE4D1D7BC','FEMALE','Carlie','Kshlerin','1993-01-06',NULL),
('6aeb4d4593','4EB59F2ABE','FEMALE','Christina','Fisher','1990-06-12',NULL),
('7e13193f14','6520C5DCFB','FEMALE','Lelah','Hansen','2008-03-24',NULL),
('7f5c301248','AE8255EBA2','MALE','Alisha','Grant','1985-02-22',NULL),
('8aab74b7c7','8C01F25211','MALE','Damian','Botsford','1990-06-03',NULL),
('8e97d85d57','5298FAEB25','FEMALE','Maya','Littel','2000-06-26',NULL),
('91c56a1d66','3892463456','MALE','Zane','Brekke','2011-07-14',NULL),
('9487c15ed7','EBCA1A059C','MALE','Ernie','Maggio','1983-03-30',NULL),
('9654ce4f15','638C01F252','MALE','Arlo','Sanford','1988-04-27',NULL),
('993051fd35','AFCB7D1D4E','MALE','Anjali','Towne','1981-01-16',NULL),
('a7ca41a2d6','55EBA2F95B','MALE','Barbara','Leuschke','2001-02-15',NULL),
('a92c30f941','9F2ABE5528','FEMALE','Trevor','Altenwerth','2001-11-29',NULL),
('a97e5823a1','52111F9D28','MALE','Raymond','Upton','1981-04-09',NULL),
('aa2d787a48','059C0BAE82','FEMALE','Dane','Streich','2014-07-08',NULL),
('b040b60513','5528EAB0C9','FEMALE','Brian','Harvey','2003-10-17',NULL),
('b64e99bca8','AE11CECF9F','MALE','Loraine','Steuber','1980-11-23',NULL),
('bca569d273','011252111F','MALE','Era','Graham','1985-09-22',NULL),
('c331b9a8cc','BE01638C01','FEMALE','Jeffry','Cremin','2015-12-12',NULL),
('d038ce3b46','D1D7BCFA89','FEMALE','Nannie','Thompson','2013-12-17',NULL),
('d7366f2f90','98AFCB7D1D','FEMALE','Maureen','Legros','1986-07-06',NULL),
('d76d80edc1','1BEBDA52A8','MALE','Murl','Schiller','1991-05-28',NULL),
('de40bbacd1','0E93F93526','MALE','Kathleen','Terry','2000-09-28',NULL),
('ec08456883','B0C950A1AC','FEMALE','Gretchen','Moen','1981-04-08',NULL),
('edbd0e0ccb','18AC3E7343','FEMALE','Camren','Sanford','1986-09-18',NULL),
('f116b3e9c3','A1ACBE0163','FEMALE','Herman','Kautzer','1983-05-09',NULL),
('f2cb645477','EBA2F95BE4','FEMALE','Annetta','Schamberger','2016-07-01',NULL),
('fdb05bc7c1','C83610EBCA','FEMALE','Arjun','Walker','2001-12-27',NULL),
('02d22777a6','BE5528EAB0','MALE','Henriette','Pfeffer','2008-07-14',NULL),
('062225365c','9C0BAE8255','MALE','Forest','Wiza','2007-04-09',NULL),
('09f2f6637d','62539F39E0','MALE','Dixie','Shields','1971-12-24',NULL),
('0a4fa8d024','BCFA89D724','FEMALE','Emie','Hermiston','2017-06-15',NULL),
('1c7cb50bdf','B59F2ABE55','FEMALE','Gene','Dickens','1994-12-20',NULL),
('1cde08d67d','10EBCA1A05','MALE','Jennings','Langworth','1977-09-10',NULL),
('1dcabb04ed','A2F95BE4D1','MALE','Suzanne','Dicki','2008-05-06',NULL),
('1e346e3b93','1F9D28A842','FEMALE','Delmer','Zemlak','2018-07-31',NULL),
('25d2c9d154','9D28A8427D','MALE','Gussie','Walter','1982-06-20',NULL),
('31506b040b','5F3E9D9611','MALE','Wayne','Stamm','2013-11-24',NULL),
('3c9e3b611f','BFCD5C0256','MALE','Fannie','Friesen','1990-03-19',NULL),
('3ca0816e84','28EAB0C950','FEMALE','Bud','Brekke','1985-05-26',NULL),
('41f39131e7','2F10C83610','MALE','Amya','Ebert','2004-08-14',NULL),
('48e6180ac3','9C3F925D0E','FEMALE','Joanny','Dach','1978-04-22',NULL),
('51f4ec4569','248A82D9F1','FEMALE','Emmett','Bayer','1998-08-28',NULL),
('53df150399','0BAE8255EB','FEMALE','Richie','Pacocha','2005-09-28',NULL),
('64b3ec830d','28A8427D98','FEMALE','Josiane','Gutkowski','2016-11-21',NULL),
('66d1a65c19','427D98AFCB','FEMALE','Raquel','Sanford','1980-09-15',NULL),
('6aefcb3a51','CA1A059C0B','MALE','Monique','Jacobi','1980-02-11',NULL),
('6d2a14ac7a','ACBE01638C','MALE','Duncan','Schmeler','1981-05-31',NULL),
('7de51c7849','D7BCFA89D7','MALE','Denis','Thiel','1972-10-01',NULL),
('80be84b622','17A3404E8F','FEMALE','Ashly','Koch','1992-06-15',NULL),
('842103c5f7','10C83610EB','FEMALE','Kory','Huel','1987-03-24',NULL),
('84a787d2aa','252F10C836','FEMALE','Eldred','Mayer','2014-06-09',NULL),
('8d8782c875','A8427D98AF','MALE','Jordyn','Sipes','1980-09-01',NULL),
('95f80a26b5','11252F10C8','MALE','Peggie','Swaniawski','1976-03-05',NULL),
('986ad32c7e','3610EBCA1A','FEMALE','Alivia','Glover','1970-11-30',NULL),
('9cb5340bc4','89D7248A82','MALE','Megane','Howell','2011-07-19',NULL),
('9e3240c822','D7248A82D9','FEMALE','Andres','Zieme','2004-11-12',NULL),
('9f67393a21','01638C01F2','MALE','Ivah','Ferry','2005-04-09',NULL),
('a5be8ac9c5','F111252110','FEMALE','Richard','Langosh','1994-04-01',NULL),
('bcc0e0dbde','F9FCEC11EA','MALE','Jeanette','Kohler','2001-01-07',NULL),
('c6084a5f86','F016890C51','MALE','Gilda','Romaguera','1989-04-21',NULL),
('cc8a9b133c','3437E3CA81','FEMALE','Shaun','Gutkowski','1984-08-08',NULL),
('d8d6132c75','15C098610F','FEMALE','Annalise','Rippin','2000-05-19',NULL),
('d91e24d9c4','82D9F11125','FEMALE','Cathryn','Hettinger','2007-05-07',NULL),
('f7d7cd12c5','CB7D1D4EB5','MALE','Geovany','Littel','1976-08-19',NULL),
('f950348212','6543642983','FEMALE','Tamara','Hodkiewicz','1980-06-23',NULL); 




INSERT INTO `FLIES_ON` VALUES ('03ef71a3','05327c8e99'),
('99cbb790','12a39376f9'),
('1cf08c9a','15a3bcfea6'),
('24c4b570','17a3eaf2bb'),
('03ef71a3','226b48eb08'),
('03ef71a3','228c0423e9'),
('1cf08c9a','297b758db3'),
('1cf08c9a','2cee74327e'),
('03ef71a3','39b3e643e1'),
('1cf08c9a','443e33c16d'),
('24c4b570','451d9c2d52'),
('03ef71a3','48d75f43da'),
('b9963d94','4c9d42e19d'),
('b9963d94','4cb0435bc9'),
('99cbb790','4cf27yj8i6'),
('24c4b570','542a9095bb'),
('99cbb790','578c2878d8'),
('24c4b570','57c2316d8d'),
('99cbb790','5b62a08f59'),
('1cf08c9a','5c21dc7d7f'),
('03ef71a3','5c9ca8eb5a'),
('1cf08c9a','68f5a4806c'),
('1cf08c9a','6a77722d20'),
('24c4b570','6aeb4d4593'),
('1cf08c9a','7e13193f14'),
('b9963d94','7f5c301248'),
('1cf08c9a','8aab74b7c7'),
('03ef71a3','8e97d85d57'),
('03ef71a3','91c56a1d66'),
('03ef71a3','9487c15ed7'),
('24c4b570','9654ce4f15'),
('24c4b570','993051fd35'),
('24c4b570','a7ca41a2d6'),
('99cbb790','a92c30f941'),
('24c4b570','a97e5823a1'),
('03ef71a3','b040b60513'),
('99cbb790','b64e99bca8'),
('1cf08c9a','bca569d273'),
('b9963d94','c331b9a8cc'),
('03ef71a3','d038ce3b46'),
('24c4b570','d7366f2f90'),
('b9963d94','d76d80edc1'),
('24c4b570','de40bbacd1'),
('99cbb790','ec08456883'),
('1cf08c9a','edbd0e0ccb'),
('03ef71a3','f116b3e9c3'),
('24c4b570','f2cb645477'),
('03ef71a3','fdb05bc7c1'),
('1cf08c9a','02d22777a6'),
('99cbb790','062225365c'),
('24c4b570','09f2f6637d'),
('24c4b570','0a4fa8d024'),
('1cf08c9a','1b79f06bac'),
('03ef71a3','1c7cb50bdf'),
('b9963d94','1cde08d67d'),
('b9963d94','1dcabb04ed'),
('03ef71a3','1e346e3b93'),
('b9963d94','25d2c9d154'),
('99cbb790','31506b040b'),
('b9963d94','3c9e3b611f'),
('1cf08c9a','3ca0816e84'),
('b9963d94','41f39131e7'),
('03ef71a3','48e6180ac3'),
('99cbb790','51f4ec4569'),
('b9963d94','53df150399'),
('1cf08c9a','64b3ec830d'),
('1cf08c9a','66d1a65c19'),
('b9963d94','6aefcb3a51'),
('03ef71a3','6d2a14ac7a'),
('1cf08c9a','7de51c7849'),
('1cf08c9a','80be84b622'),
('1cf08c9a','842103c5f7'),
('03ef71a3','84a787d2aa'),
('1cf08c9a','8d8782c875'),
('99cbb790','95f80a26b5'),
('1cf08c9a','986ad32c7e'),
('24c4b570','9cb5340bc4'),
('03ef71a3','9e3240c822'),
('b9963d94','9f67393a21'),
('b9963d94','a5be8ac9c5'),
('99cbb790','bcc0e0dbde'),
('24c4b570','c6084a5f86'),
('03ef71a3','cc8a9b133c'),
('b9963d94','d8d6132c75'),
('b9963d94','d91e24d9c4'),
('99cbb790','f7d7cd12c5'),
('03ef71a3','f950348212'),
('03ef71a3','aa2d787a48'); 
