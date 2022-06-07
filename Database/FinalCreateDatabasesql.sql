CREATE DATABASE QLTV
USE QLTV
create table LIBCARDS(
LIBCARD_ID int IDENTITY(1,1) CONSTRAINT PK_LC PRIMARY KEY,
NAME nVarchar(30)	Not Null,
AGES INT not null,
ADDRESS nVARCHAR(100) NOT NULL,
CLASS VARCHAR(15) NOT NULL
)

create table BOOKS(
BOOK_ID	int IDENTITY(1,1) CONSTRAINT PK_B PRIMARY KEY,
TITLE	nVarchar(50)	Not Null,
STATE INT not null,
POSITION nVARCHAR(10) not null,
PATH NVARCHAR(200) NULL
)

CREATE TABLE ACCOUNT(
	USERNAME VARCHAR(20) CONSTRAINT PK_ACC PRIMARY KEY,
	PASSWORD VARCHAR(30)
)
INSERT INTO ACCOUNT VALUES('ADMIN','ADMIN')

SET DATEFORMAT dmy

--use QLTV EXEC sp_changedbowner 'sa' --dung de cap quyen owner cho database de ve diagram khi copy tu may nay qua may khac
