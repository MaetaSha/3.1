--Create Database
create database university_190609
use university_190609

-- Create Table
create table instructor(
ID varchar(5),
name varchar(20) not NULL, 
dept_name varchar(20),
salary numeric(8,2), 
primary key(ID));

--Insert Value in Table
insert into instructor values('101','RAHATUL','ICE',90000);
insert into instructor values('102','BAPPY','CSE',20000);
insert into instructor values('103','SUHAN','EEE',100000);

--To Display all value of Department Table
select * from instructor;

--group by clause
select dept_name,AVG(salary) as avg_salary from instructor group by dept_name;

--having clause
select dept_name,AVG(salary) as avg_salary from instructor group by dept_name having AVG(salary)>42000;

--order by clause
select * from instructor order by salary desc,name asc;

--create view
create view faculty as select ID,name,dept_name from instructor;
--to display
select * from faculty;

--Indexing
select salary from instructor;
--create indexing
create index salary_index on instructor(salary asc);
select salary from instructor;
--delete indexing
drop index instructor.salary_index;

--create procedure
CREATE PROCEDURE instructor_proc
AS
BEGIN
select name as authors_name from instructor where ID='101';
END
EXEC instructor_proc --Call procedure
--to display
select * from instructor;

drop procedure instructor_proc;