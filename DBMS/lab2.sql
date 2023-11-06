use university;
-- create new table called employe
create table employe(
    id int primary key,
    name varchar(100) not null
);
insert into employe values(101, 'abir');
insert into employe values(102, 'ahsan');
select * from employe;
-- add new column in the employe table
alter table employe
      add phone varchar(20);
insert into employe values(103, 'yasin', '0123456789');
select * from employe;
-- delete table
drop table employe;
