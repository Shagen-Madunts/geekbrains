-- ѕусть в таблице users пол€ created_at и updated_at оказались незаполненными. «аполните их текущими датой и временем.

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
    created_at DATETIME DEFAULT NULL,
    updated_at DATETIME DEFAULT NULL,
    INDEX users_firstname_lastname_idx(firstname, lastname)
);

insert into users (firstname, lastname, email, phone) values
('Reuben', 'Nienow', 'arlo5010e2@example.org', '9374071116'),
('Masha', 'Upton', 'terrence.cartwright@example.org', '9127498182'),
('Masha', 'Windler', 'rupert55@example.org', '9921090703'),
('Masha', 'West', 'rebekah29@example.net', '9592139196'),
('Frederick', 'Effertz', 'von.bridget@example.net', '9909791725'),
('Shagen', 'Petrov', 'sd@example.org', '9374071116'),
('Masha', 'Krylova', 'krysa@mail.ru', '9127498182'),
('Sergey', 'Kuznetsov', 'kuz@example.org', '9921090703'),
('Olga', 'Lopushkina', 'ol@example.net', '9592139196'),
('Semen', 'Ivanov', 'arlo45@example.org', '9374071116'),
('Patrik', 'Ferg', 'terr@example.org', '9127498182'),
('Dina', 'Petrova', 'dp@example.org', '9921090703'),
('Dasha', 'Mon', 'dm@example.net', '9592139196'),
('Anastas', 'Savina', 'AN@example.net', '9909791725')
;

UPDATE users 
set created_at = NOW(),
	updated_at = NOW() 
;

SELECT * from users;

