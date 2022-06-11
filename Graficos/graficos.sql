create database bd_estatisticas_saude;
use bd_estatisticas_saude;

create table autoavaliacao_saude (
	idAutoAvaliacao int not null primary key auto_increment,
    intervalo varchar(20) not null,
    proporcao float not null    
);

insert into autoavaliacao_saude (intervalo, proporcao)  values 
('De 18 a 29 anos', '80.7'),
('De 30 a 59 anos', '67.7'),
('De 60 a 64 anos', '52'),
('De 65 a 74 anos', '47'),
('Acima de 75 anos', '41.1');

## Consumo recomendado de hortaliças e frutas, inclusive suco (pelo menos 25 vezes na semana). 
create table consumo_hortalicas (
	idConsumoHortalica int not null primary key auto_increment,
    intervalo varchar(20) not null,
    proporcao float not null    
);

insert into consumo_hortalicas (intervalo, proporcao)  values 
('De 18 a 24 anos', '7.4'),
('De 25 a 39 anos', '10.7'),
('De 40 a 59 anos', '14.1'),
('Acima de 60 anos', '17.9');


## Consumo regular de feijão (cinco ou mais dias da semana)
create table consumo_feijao (
	idConsumoFeijao int not null primary key auto_increment,
    intervalo varchar(20) not null,
    proporcao float not null    
);

insert into consumo_feijao (intervalo, proporcao)  values 
('De 18 a 24 anos', '68'),
('De 25 a 39 anos', '66.3'),
('De 40 a 59 anos', '69'),
('Acima de 60 anos', '70.2');

## Consumo regular de alimentos considerados não saudáveis, como bolos, tortas doces, chocolates, gelatinas, balas, biscoitos ou bolachas recheadas (cinco ou mais dias da semana)
create table consumo_naoSaudaveis (
	idConsumoNaoSaudaveis int not null primary key auto_increment,
    intervalo varchar(20) not null,
    proporcao float not null    
);

insert into consumo_naoSaudaveis (intervalo, proporcao)  values 
('De 18 a 24 anos', '23.8'),
('De 25 a 39 anos', '15.8'),
('De 40 a 59 anos', '11.9'),
('Acima de 60 anos', '12.7');

## Proporção de prática do nível recomendado de atividade física no lazer (fora do âmbito escolar ou trabalho, por mais de 150 minutos para atividade moderada ou por 75 minutos para atividades vigorosas na semana)
create table exercicio_lazer (
	idExercicioLazer int not null primary key auto_increment,
    intervalo varchar(20) not null,
    proporcao float not null    
);

insert into exercicio_lazer (intervalo, proporcao)  values 
('De 18 a 24 anos', '41'),
('De 25 a 39 anos', '35.4'),
('De 40 a 59 anos', '27.6'),
('Acima de 60 anos', '19.8');

## 
create table habito_tabagismo (
	idHabitoTabagismo int not null primary key auto_increment,
    intervalo varchar(20) not null,
    proporcao float not null    
);

insert into habito_tabagismo (intervalo, proporcao)  values 
('De 18 a 24 anos', '10.8'),
('De 25 a 39 anos', '12'),
('De 40 a 59 anos', '14.9'),
('Acima de 60 anos', '11.9');

## Por 3h ou mais por dia
create table habito_televisao (
	idHabitoTelevisao int not null primary key auto_increment,
    intervalo varchar(20) not null,
    proporcao float not null    
);

insert into habito_televisao (intervalo, proporcao)  values 
('População Adulta', '21.8'),
('População Idosa', '29.6');
