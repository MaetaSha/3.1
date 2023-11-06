create database university;
use university; 
create table instruct( 
    ID varchar(20) primary key, 
    name varchar(20) not null, 
    dept_name varchar(20), 
  
    salary numeric(8,2) 
); 
insert into instruct 
values 
('10101','Srinivasan','CSE',65000), 
('12121','Wu','Finance',90000), 
('15151','Mozart','Music',40000), 
('22222','Einstein','Physics',95000), 
('32343','EI Said','History',60000), 
('33456','Gold','Physics',87000); 
select * from instruct; 
create table DEPARTMENT( 
    dept_name varchar(20) primary key, 
    Building_name varchar(20), 
    Budget numeric(12,2) 
); 
insert into DEPARTMENT  
(dept_name,Building_name,Budget) values  
('ICE','Engineering building','90000'), 
('CSE','Engineering building','80000'), 
('EEE','Engineering building','90500'), 
('Physics','Science building','50500'), 
('Social Work','Arts building','30500'); 
select * from DEPARTMENT; 
-- cartesian product 
select Building_name,salary from DEPARTMENT,instruct where 
DEPARTMENT.dept_name=instruct.dept_name; 
-- join operation 
select ID,name,budget from DEPARTMENT join instruct on 
DEPARTMENT.dept_name=instruct.dept_name; 
-- left outer join 
  
select * from DEPARTMENT left outer join instruct on 
DEPARTMENT.dept_name=instruct.dept_name; 
-- right outer join 
select * from DEPARTMENT right outer join instruct on 
DEPARTMENT.dept_name=instruct.dept_name; 
-- full outer join 
select * from DEPARTMENT left join instruct on 
DEPARTMENT.dept_name=instruct.dept_name 
union 
select * from DEPARTMENT right join instruct on 
DEPARTMENT.dept_name=instruct.dept_name;
drop database university;