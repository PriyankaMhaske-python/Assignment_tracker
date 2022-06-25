create database assignment_tracking;
use assignment_tracking;

create table user(userid int ,name varchar(100),
password varchar(100),
mobile_number varchar(100),
email_address varchar(100),
type_of_user varchar(100),
primary key(userid));


create table assignment(assignmentid int ,
title varchar(100),
description varchar(1000),
due_date varchar(100),
primary key(assignmentid));




create table submission(submissionid int primary key,
assignmentid int ,
userid int ,
submission_date varchar(100),
solution varchar(1000),
status varchar(100),
FOREIGN KEY (assignmentid) REFERENCES assignment(assignmentid),
FOREIGN KEY (userid) REFERENCES user(userid)
);













