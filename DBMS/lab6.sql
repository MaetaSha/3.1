use university; 
select * from instruct; 
-- count 
select count(ID) as cnt_ID from instruct where dept_name='Physics'; 
-- max 
select max(salary) as maxSalary from instruct; 
-- min 
select min(salary) as minSalary from instruct; 
  
-- avg 
select avg(salary) as avg_salary from instruct; 