create database week11_hwk;

use week11_hwk;
--created some basic tables to test the database connection for both inserting data and getting content
create table contact_information(
ContactID int auto_increment primary key,
Firstname varchar(50) not null,
Lastname varchar(50) not null,
email varchar(100) not null,
comments text not null,
timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from contact_information;

create table portfolio(
ProjectID int auto_increment primary key,
Portfoliouser varchar(50) not null,
imagelink varchar(200),
Projectheader varchar(50) not null,
Projectparagraph1 text,
Projectparagraph2 text,
Projectparagraph3 text,
Projectparagraph4 text,
Projectlink text
);

insert into portfolio(Portfoliouser, imagelink, Projectheader, Projectparagraph1, Projectparagraph2, Projectparagraph3, Projectparagraph4, Projectlink)
values ('Katy', 'image/katy-images/object_oriented_programming_outline_diagram-1.webp', 'Week 9 Homework', 'Learning more about databases', 'We practiced creating views', 'We were then given homework!', 'The home was to create our library database with two views and two stored procedures', 'https://github.com/Jiyabharti/Libraryv1'),
('Katy', 'image/katy-images/catonabook.jpeg', 'Week 6 Homework', 'We were learning all about Object Orientated Programming OOP', 'OOP has been the hardest thing to learn so far!! Hence it taking two weeks of sessions!',"We've been understanding classes, methods, inheritance, polymorphism, encapsulation.", 'We revisited our banking apps and rock, paper,scissors', 'https://github.com/Jiyabharti/week6hwk">Our homework for week 6');

select * from portfolio;


