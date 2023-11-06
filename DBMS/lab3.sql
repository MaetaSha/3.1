use University;
create table dept(
   Dept_name varchar(20),
   Building varchar(20),
   Budget numeric(12,2),
   primary key(Dept_name)
);
insert into dept 
(Dept_name,Building,Budget)
values 
('ICE','Engineering building','90000'),
('CSE','Engineering building','80000'),
('EEE','Engineering building','90500'),
('Physics','Science building','50500');

select * from dept;
select Building from dept;
select Dept_name from dept where Building='Engineering building';
