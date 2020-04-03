/*Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались значения в формате "20.10.2017 8:10". 
 * Необходимо преобразовать поля к типу DATETIME, сохранив введеные ранее значения*/

DROP DATABASE IF EXISTS vk;
CREATE DATABASE vk;
USE vk;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    email VARCHAR(120) UNIQUE,
    phone BIGINT, 
    created_at VARCHAR(50),
    updated_at VARCHAR(50),
    INDEX users_firstname_lastname_idx(firstname, lastname)
);


insert into users (firstname , lastname , email , phone , created_at, updated_at ) values
('Reuben', 'Nienow', 'arlo5010e2@example.org', '9374071116', '20.10.2017 8:10', '20.10.2017 8:10'),
('Masha', 'Upton', 'terrence.cartwright@example.org', '9127498182', '20.10.2017 8:10', '20.10.2017 8:10'),
('Masha', 'Windler', 'rupert55@example.org', '9921090703', '20.10.2017 8:10', '20.10.2017 8:10'),
('Masha', 'West', 'rebekah29@example.net', '9592139196', '20.10.2017 8:10', '20.10.2017 8:10'),
('Frederick', 'Effertz', 'von.bridget@example.net', '9909791725', '20.10.2017 8:10', '20.10.2017 8:10'),
('Shagen', 'Petrov', 'sd@example.org', '9374071116', '20.10.2017 8:10', '20.10.2017 8:10'),
('Masha', 'Krylova', 'krysa@mail.ru', '9127498182', '20.10.2017 8:10', '20.10.2017 8:10'),
('Sergey', 'Kuznetsov', 'kuz@example.org', '9921090703', '20.10.2017 8:10', '20.10.2017 8:10'),
('Olga', 'Lopushkina', 'ol@example.net', '9592139196', '20.10.2017 8:10', '20.10.2017 8:10'),
('Semen', 'Ivanov', 'arlo45@example.org', '9374071116', '20.10.2017 8:10', '20.10.2017 8:10'),
('Patrik', 'Ferg', 'terr@example.org', '9127498182', '20.10.2017 8:10', '20.10.2017 8:10'),
('Dina', 'Petrova', 'dp@example.org', '9921090703', '20.10.2017 8:10', '20.10.2017 8:10'),
('Dasha', 'Mon', 'dm@example.net', '9592139196', '20.10.2017 8:10', '20.10.2017 8:10'),
('Anastas', 'Savina', 'AN@example.net', '9909791725', '20.10.2017 8:10', '20.10.2017 8:10')
;



UPDATE users 
set created_at = STR_TO_DATE(created_at, '%d.%m.%Y %H:%i'),
	updated_at = STR_TO_DATE(updated_at, '%d.%m.%Y %H:%i') 
;

SELECT * from users;

