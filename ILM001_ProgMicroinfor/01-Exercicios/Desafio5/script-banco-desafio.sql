create database contatos;
use contatos;

create table contatos
(
	#cod_contatos int primary key auto_increment,
	email varchar(45) not null unique,
    nome varchar(45) not null,
    assunto varchar(60) not null
);


describe contatos;

insert into contatos (email, nome, assunto) values
('fatec@fatec.sp.gov.br','Fatec','Flask'),
('fatec1@fatec.sp.gov.br','Fatec','Banco de Dados');


select * from contatos;