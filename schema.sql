-- *********************************************
-- * Standard SQL generation                   
-- *--------------------------------------------
-- * DB-MAIN version: 11.0.2              
-- * Generator date: Sep 14 2021              
-- * Generation date: Wed Jul 24 12:32:13 2024 
-- * LUN file: C:\Users\SOSO\Documents\FORMATION\CNAM\projet\projas.lun 
-- * Schema: SCHEMA ERA
-- ********************************************* 


-- Database Section
-- ________________ 

create database SCHEMA SCHUTZ;


-- DBSpace Section
-- _______________


-- Tables Section
-- _____________ 

create table EMPLACEMENTS (
     ID NUMERIC(10) not null,
     R_ID char(1) not null,
     constraint ID_EMPLACEMENTS_ID primary key (ID));

create table ALLEE (
     ID char(1) not null,
     constraint ID_ALLEE_ID primary key (ID));

create table INVENTAIRE (
     REF varchar(50) not null,
     Date date not null,
     ID numeric(1) not null,
     constraint ID_INVENTAIRE_ID primary key (REF),
     constraint SID_INVENTAIRE_ID unique (Date),
     constraint FKR_1_ID unique (ID));


-- Constraints Section
-- ___________________ 

alter table EMPLACEMENTS add constraint FKR_FK
     foreign key (R_ID)
     references ALLEE;

alter table INVENTAIRE add constraint FKR_1_FK
     foreign key (ID)
     references EMPLACEMENTS;


-- Index Section
-- _____________ 

create unique index ID_EMPLACEMENTS_IND
     on EMPLACEMENTS (ID);

create index FKR_IND
     on EMPLACEMENTS (R_ID);

create unique index ID_ALLEE_IND
     on ALLEE (ID);

create unique index ID_INVENTAIRE_IND
     on INVENTAIRE (REF);

create unique index SID_INVENTAIRE_IND
     on INVENTAIRE (Date);

create unique index FKR_1_IND
     on INVENTAIRE (ID);

