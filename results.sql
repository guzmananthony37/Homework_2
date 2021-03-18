-- Anthony Guzman 1503239
-- select * from user
use mydb;
drop table hwk2_results;
create table hwk2_results(
	id INT NOT NULL auto_increment,
	city varchar(50), 
	date datetime, 
	temp decimal(5,2),
	feels_like decimal(5,2), 
    temp_min decimal(5,2),
    temp_max decimal(5,2),
    pressure int,
    humidity int,
    PRIMARY KEY (id)
)

Select * From hwk2_results;
