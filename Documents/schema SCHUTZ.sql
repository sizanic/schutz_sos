-- *********************************************
-- * SQL MySQL generation                      
-- *--------------------------------------------
-- * DB-MAIN version: 11.0.2              
-- * Generator date: Sep 14 2021              
-- * Generation date: Thu Jul 25 15:45:43 2024 
-- * LUN file: C:\Users\SOSO\Documents\FORMATION\CNAM\projet\projas.lun 
-- * Schema: SCHUTZ/1 
-- ********************************************* 


-- Database Section
-- ________________ 

-- create database SCHUTZ;
-- use SCHUTZ;


-- Tables Section
-- _____________ 

create table EMPLACEMENTS (
     ALLEE_ID char(1) not null,
     ID int not null,
     ID_EMPLACEMENTS_ID primary key (ALLEE_ID, ID));

create table INVENTAIRE (
     REF varchar(50) not null,
     Date date not null,
     ALLEE_ID char(1) not null,
     ID int not null,
     ID_INVENTAIRE_ID primary key (REF),
     SID_INVENTAIRE_ID unique (Date),
     FKALLEE_ID unique (ALLEE_ID, ID));


-- Constraints Section
-- ___________________ 

alter table INVENTAIRE add constraint FKALLEE_FK
     foreign key (ALLEE_ID, ID)
     references EMPLACEMENTS (ALLEE_ID, ID);


-- Index Section
-- _____________ 

create unique index ID_EMPLACEMENTS_IND
     on EMPLACEMENTS (ALLEE_ID, ID);

create unique index ID_INVENTAIRE_IND
     on INVENTAIRE (REF);

create unique index SID_INVENTAIRE_IND
     on INVENTAIRE (Date);

create unique index FKALLEE_IND
     on INVENTAIRE (ALLEE_ID, ID);

