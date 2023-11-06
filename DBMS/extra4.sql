

use university;
create table student(
ID varchar(5),
name varchar(20) not NULL );
insert into student values('2','shama');
insert into student values('3','mim');

select * from student;
create table info(
mark int,
department varchar(20))
insert into info values(66,'ice');
insert into info values(77,'math');
select * from info;
create view combine as
select ID,Name,mark,department
from student , info;
select * from combine;
