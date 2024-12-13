
CREATE DATABASE STUDENT;
USE STUDENT;

CREATE TABLE CREDENTIALS (
    username VARCHAR(50) PRIMARY KEY NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);


CREATE TABLE BADGES (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    badgename VARCHAR(100) NOT NULL,
    FOREIGN KEY (username) REFERENCES CREDENTIALS(username)
);



SHOW TABLES;
select * from BADGES;
SELECT * FROM CREDENTIALS;



INSERT INTO CREDENTIALS (username, password) VALUES
('S24Student92', 'S24Student92'),
('S24Student149', 'S24Student149'),
('S24Student256', 'S24Student256'),
('S24Student157', 'S24Student157'),
('S24Student227', 'S24Student227'),
('S24Student335', 'S24Student335'),
('S24Student160', 'S24Student160'),
('S24Student205', 'S24Student205'),
('S24Student271', 'S24Student271'),
('S24Student249', 'S24Student249'),
('S24Student221', 'S24Student221'),
('S24Student61', 'S24Student61'),
('S24Student186', 'S24Student186'),
('S24Student340', 'S24Student340'),
('S24Student234', 'S24Student234'),
('S24Student339', 'S24Student339'),
('S24Student355', 'S24Student355'),
('S24Student357', 'S24Student357'),
('S24Student312', 'S24Student312'),
('S24Student110', 'S24Student110'),
('S24Student215', 'S24Student215'),
('S24Student359', 'S24Student359'),
('S24Student80', 'S24Student80'),
('S24Student141', 'S24Student141'),
('S24Student293', 'S24Student293'),
('S24Student145', 'S24Student145'),
('S24Student347', 'S24Student347'),
('S24Student225', 'S24Student225'),
('S24Student204', 'S24Student204'),
('S24Student228', 'S24Student228'),
('S24Student109', 'S24Student109'),
('S24Student195', 'S24Student195'),
('S24Student161', 'S24Student161'),
('S24Student226', 'S24Student226'),
('S24Student192', 'S24Student192'),
('S24Student203', 'S24Student203'),
('S24Student169', 'S24Student169'),
('S24Student81', 'S24Student81'),
('S24Student299', 'S24Student299'),
('S24Student346', 'S24Student346'),
('S24Student66', 'S24Student66'),
('S24Student15', 'S24Student15'),
('S24Student242', 'S24Student242'),
('S24Student216', 'S24Student216'),
('S24Student348', 'S24Student348'),
('S24Student86', 'S24Student86'),
('Carlatextpreview', 'Carlatextpreview'),
('S24Student191', 'S24Student191'),
('S24Student328', 'S24Student328');

-- select badgename from badges where username = "S24Student149";




