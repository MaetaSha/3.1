-- Creating new database called university
create database university;
use university;
-- Creating new table called students
create table students(
   id int primary key,
    name varchar(100) not null,
    age int not null,
    department varchar(10) not null,
    city varchar(30) not null
);
-- insert data in the students table
INSERT INTO students (id, name, age, department, city)
VALUES
(200616, 'rakib', 24, 'ICE', 'Pabna'),
(200617, 'sabuz', 23, 'ICE', 'Dhaka'),
(200618, 'sumona', 23, 'ICE', 'Naogoan');

-- to view the table
select * from students;
-- update the students table
update students set age=25 where id=200618;
select * from students;
-- delete a row from the students table
delete from students where id=200618;
select * from students;
-- delete table
drop table students;
-- delete database
drop database university;

