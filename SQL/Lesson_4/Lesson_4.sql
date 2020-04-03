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
    INDEX users_firstname_lastname_idx(firstname, lastname)
);


DROP TABLE IF EXISTS messages;
CREATE TABLE messages (
	id SERIAL PRIMARY KEY,
	from_user_id BIGINT UNSIGNED NOT NULL,
    to_user_id BIGINT UNSIGNED NOT NULL,
    body TEXT,
    created_at DATETIME,

    FOREIGN KEY (from_user_id) REFERENCES users(id),
    FOREIGN KEY (to_user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS friend_requests;
CREATE TABLE friend_requests (
	initiator_user_id BIGINT UNSIGNED NOT NULL,
    target_user_id BIGINT UNSIGNED NOT NULL,
    `status` ENUM('requested', 'approved', 'unfriended', 'declined') DEFAULT 'requested',
	requested_at DATETIME DEFAULT NOW(),
	confirmed_at DATETIME,
	
    PRIMARY KEY (initiator_user_id, target_user_id),
    FOREIGN KEY (initiator_user_id) REFERENCES users(id),
    FOREIGN KEY (target_user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS communities;
CREATE TABLE communities(
	id SERIAL PRIMARY KEY,
	name VARCHAR(150),

	INDEX communities_name_idx(name)
);

DROP TABLE IF EXISTS users_communities;
CREATE TABLE users_communities(
	user_id BIGINT UNSIGNED NOT NULL,
	community_id BIGINT UNSIGNED NOT NULL,
  
	PRIMARY KEY (user_id, community_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (community_id) REFERENCES communities(id)
);

DROP TABLE IF EXISTS media_types;
CREATE TABLE media_types(
	id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS media;
CREATE TABLE media(
	id SERIAL PRIMARY KEY,
    media_type_id BIGINT UNSIGNED NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
  	body text,
    filename VARCHAR(255),
    `size` INT,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (media_type_id) REFERENCES media_types(id)
);

DROP TABLE IF EXISTS likes;
CREATE TABLE likes(
	id SERIAL PRIMARY KEY,
    user_id BIGINT UNSIGNED NOT NULL,
    media_id BIGINT UNSIGNED NOT NULL,
    created_at DATETIME DEFAULT NOW(),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (media_id) REFERENCES media(id)

);

DROP TABLE IF EXISTS `photo_albums`;
CREATE TABLE `photo_albums` (
	`id` SERIAL,
	`name` varchar(255) DEFAULT NULL,
    `user_id` BIGINT UNSIGNED DEFAULT NULL,

    FOREIGN KEY (user_id) REFERENCES users(id),
  	PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `photos`;
CREATE TABLE `photos` (
	id SERIAL PRIMARY KEY,
	`album_id` BIGINT unsigned NOT NULL,
	`media_id` BIGINT unsigned NOT NULL,

	FOREIGN KEY (album_id) REFERENCES photo_albums(id),
    FOREIGN KEY (media_id) REFERENCES media(id)
);


DROP TABLE IF EXISTS city_location;
CREATE TABLE city_location(
	id SERIAL PRIMARY KEY,
    city VARCHAR(255),
    INDEX users_cityname_idx(city)
);

DROP TABLE IF EXISTS region_location;
CREATE TABLE region_location(
	id SERIAL PRIMARY KEY,
    region VARCHAR(255),
    INDEX users_region_idx(region)
);

DROP TABLE IF EXISTS location;
CREATE TABLE location(
	id SERIAL PRIMARY KEY,
    city_id BIGINT unsigned NOT NULL,
    region_id BIGINT unsigned NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (city_id) REFERENCES city_location(id),
    FOREIGN KEY (region_id) REFERENCES region_location(id)
	
);

DROP TABLE IF EXISTS `profiles`;
CREATE TABLE `profiles` (
	user_id SERIAL PRIMARY KEY,
    gender CHAR(1),
    birthday DATE,
	photo_id BIGINT UNSIGNED NULL,
    created_at DATETIME DEFAULT NOW(),
    hometown_id BIGINT UNSIGNED,
    FOREIGN KEY (hometown_id) REFERENCES location (id)
    
);

ALTER TABLE `profiles` ADD CONSTRAINT fk_user_id
	FOREIGN KEY (user_id) REFERENCES users(id)
    ON UPDATE CASCADE
    ON DELETE restrict;

ALTER TABLE vk.profiles ADD is_active BIT DEFAULT 1 NOT NULL;


use vk;


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

insert into city_location (city) values
('Moscow'),
('Spb'),
('Krasnodar'),
('Омск'),
('Воронеж'),
('Тула'),
('Новосибирск'),
('Ярославль'),
('Липецк'),
('Горозый'),
('Ставрополь'),
('Благовещенск'),
('Зеленоград'),
('Майкоп')
;

insert into region_location (region) values
('Moscow'),
('Spb'),
('Краснодарский край'),
('Омская область'),
('Воронежская область'),
('Тульская область'),
('Новосибирская область'),
('Ярославская область'),
('Липецкая область'),
('Чеченская республика'),
('Ставропольский край'),
('Амурская область'),
('Москвоская область'),
('Руспублика Адыгея')
;


insert into location (city_id, region_id, user_id ) values
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10),
(11, 11, 11),
(12, 12, 12),
(13, 13, 13),
(14, 14, 14)
;


insert into profiles (user_id, gender, birthday, photo_id, hometown_id, is_active) values
(1, 'м', '1995-08-28', 1, 1, 1),
(2, 'ж', '1994-01-28', 2, 2, 1),
(3, 'ж', '1993-02-28', 3, 3, 1),
(4, 'ж', '1992-03-28', 4, 4, 1),
(5, 'м', '1991-04-28', 5, 5, 1),
(6, 'м', '1990-05-28', 6, 6, 1),
(7, 'ж', '1989-06-28', 7, 7, 1),
(8, 'м', '1988-07-28', 8, 8, 1),
(9, 'ж', '1987-08-28', 9, 9, 1),
(10, 'м', '1986-09-28', 10, 10, 1),
(11, 'м', '2004-10-28', 11, 11, 1),
(12, 'ж', '1984-11-28', 12, 12, 1),
(13, 'ж', '1983-12-28', 13, 13, 1),
(14, 'м', '2003-01-28', 14, 14, 1)
;


insert into messages (from_user_id, to_user_id, body, created_at) values
(1, 14, 'Привет', '2020-04-01 07:10:39'),
(2, 13, 'Пока', '2021-04-01 07:10:39'),
(3, 12, 'Как дела?', '2022-04-01 07:10:39'),
(4, 11, 'Ага', '2023-04-01 07:10:39'),
(5, 10, 'Lol', '2019-04-01 07:10:39'),
(6, 9, 'Кек', '2018-04-01 07:10:39'),
(7, 8, 'А зачем?', '2017-04-01 07:10:39'),
(8, 7, 'lol', '2019-04-01 07:10:39'),
(9, 6, 'Ну надо', '2019-04-01 07:10:39'),
(10, 5, 'Приходи', '2019-04-01 07:10:39'),
(11, 4, 'Да', '2019-04-01 07:10:39'),
(12, 3, 'Нет', '2019-04-01 07:10:39'),
(13, 2, 'Наверно', '2019-04-01 07:10:39'),
(14, 1, 'Может быть', '2019-04-01 07:10:39')
;

insert into photo_albums (user_id, name) values
(1, 'Семья'),
(2, 'Город'),
(3, 'Друзья'),
(4, 'Разное'),
(5, 'Разобрать'),
(6, 'Красивые'),
(7, 'Отдых'),
(8, 'Париж'),
(9, 'Интересное'),
(10, 'Отстой'),
(11, 'Мемы'),
(12, 'Удалить'),
(13, 'Крым'),
(14, 'История')
;


insert into communities (name) values
('Почта'),
('xxx'),
('Город'),
('Район'),
('Мульты'),
('Фильмы'),
('История'),
('Города'),
('Париж'),
('Правительство'),
('Готовка'),
('Мебель'),
('Истории'),
('Темы')
;

insert into friend_requests (initiator_user_id, target_user_id, status) values
(1, 2, 'requested'),
(2, 2, 'approved'),
(3, 1, 'unfriended'),
(4, 2, 'declined'),
(4, 1, 'requested'),
(4, 3, 'approved'),
(10, 12, 'unfriended'),
(11, 13, 'approved'),
(9, 10, 'requested'),
(8, 13, 'unfriended'),
(7, 2, 'approved'),
(6, 1, 'declined'),
(14, 2, 'declined'),
(14, 1, 'declined')
;


insert into media_types (name) values
('photo'),
('video'),
('audio')
;

insert into media (media_type_id, user_id, body, filename, `size` ) values
(1, 2, 'Quod dicta omnis placeat id et officiis et. Beatae enim aut aliquid neque occaecati odit. Facere eum distinctio assumenda omnis est delectus magnam', 'skldfjl.jpg', 234242),
(2, 2, 'Quod dicta omnis placeat id et officiis et. Beatae enim aut aliquid neque occaecati odit. Facere eum distinctio assumenda omnis est delectus magnam', '2.mpg', 3423323),
(3, 1, 'Quod dicta omnis placeat id et officiis et. Beatae enim aut aliquid neque occaecati odit. Facere eum distinctio assumenda omnis est delectus magnam', '4.vob', 987979),
(1, 2, 'Quod dicta omnis placeat id et officiis et. Beatae enim aut aliquid neque occaecati odit. Facere eum distinctio assumenda omnis est delectus magnam', '5.png', 6782723),
(1, 1, 'Quod dicta omnis placeat id et officiis et. Beatae enim aut aliquid neque occaecati odit. Facere eum distinctio assumenda omnis est delectus magnam', '6.jpg', 7664922),
(1, 3, 'requested', '7.jpg', 498234),
(1, 12, 'Quod dicta omnis placeat id et officiis et. Beatae enim aut aliquid neque occaecati odit. Facere eum distinctio assumenda omnis est delectus magnam', '8.jpg', 7832340),
(1, 13, 'requested', '9.jpg', 8723942),
(1, 10, 'Quod dicta omnis placeat id et officiis et. Beatae enim aut aliquid neque occaecati odit. Facere eum distinctio assumenda omnis est delectus magnam', '10.jpg', 7623492),
(1, 13, 'sdfsfssdf', '11.jpg', 2386232),
(1, 2, 'requested', '12.jpg', 623842934),
(1, 1, 'sfsdf', '1314.jpg', 274792),
(1, 2, 'sdvsdsdsdf', '234.jpg', 8340),
(1, 1, 'fsdsdvsdvsdv', '15.jpg', 88234)
;

insert into photos (album_id, media_id ) values
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12),
(13, 13),
(14, 14)
;

insert into likes (user_id, media_id ) values
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12),
(13, 13),
(14, 14)
;

insert into users_communities (user_id, community_id) values
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12),
(13, 13),
(14, 14)
;

-- Написать скрипт, возвращающий список имен (только firstname) пользователей без повторений в алфавитном порядке
SELECT DISTINCT firstname FROM users ORDER BY firstname ;

-- Написать скрипт, отмечающий несовершеннолетних пользователей как неактивных (поле is_active = false)
UPDATE profiles 
set is_active = 0 
where DATEDIFF(CURDATE(), birthday) < 6570;

-- Написать скрипт, удаляющий сообщения «из будущего» (дата больше сегодняшней)
DELETE FROM messages WHERE created_at > NOW()
