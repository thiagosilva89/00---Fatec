CREATE database desafiodw;

USE desafiodw;

CREATE TABLE contato(
	id int(11) not null auto_increment primary key,
	email varchar(32) not null,
	assunto varchar(255) not null,
	descricao varchar(1000) not null
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4;