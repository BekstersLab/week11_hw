create database week11_hwk;

use week11_hwk;

create table contact_information(
ContactID int auto_increment primary key,
Firstname varchar(50) not null,
Lastname varchar(50) not null,
email varchar(100) not null,
comments text not null,
timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);