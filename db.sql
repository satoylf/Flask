drop database if exists Farmville;
create database Farmville;

drop user if exists Farmville;
create user Farmville identified by '123';
grant all on Farmville.* to Farmville with grant option;
