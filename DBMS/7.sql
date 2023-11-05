use University
create table instructor
( ID int, name nvarchar(50), dept_name nvarchar(50),salary int )
select * from instructor
insert into instructor values(22222,'Einstein','Physics',95000)
insert into instructor values(12121,'Weng','Finance',90000)
insert into instructor values(32343,'herry','History',60000)
insert into instructor values(45565,'Katz','CSE',75000)
insert into instructor values(98345,'cartigo','EEE',80000)
insert into instructor values(98346,'diomond','ICE',80000)
select * from instructor
--create another table for update value keeping
create table backup_ins( ID int, name nvarchar(50),
 dept_name nvarchar(50),
 salary int );
select * from backup_ins
--create another table for deleted value keeping
create table backup_del
( ID int, name nvarchar(50), dept_name nvarchar(50),salary int )
select * from backup_del
--creating trrigger
create trigger ins_trigger
on instructor 
after insert
as begin
 print'The tigger inserted successfully'
end
--update trigger
alter TRIGGER ins_trigger
ON instructor
AFTER INSERT
AS 
BEGIN
    INSERT INTO backup_ins(ID, name, dept_name, salary)
    SELECT ID, name, dept_name, salary
    FROM inserted;
END;
--deleted tigger
create TRIGGER del_trigger
ON instructor
AFTER DELETE
AS 
BEGIN
    INSERT INTO backup_del (ID, name, dept_name, salary)
    SELECT ID, name, dept_name, salary
    FROM deleted;
END;

DELETE FROM instructor WHERE ID = 32343;
select * from backup_del

insert into instructor values('1123','gulam mustofa','ice',67667)
select * from backup_ins
