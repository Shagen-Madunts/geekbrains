/*Создайте таблицу logs типа Archive. 
 * Пусть при каждом создании записи в таблицах users, catalogs и products 
 * в таблицу logs помещается время и дата создания записи, название таблицы, идентификатор первичного ключа и содержимое поля name.*/

DROP DATABASE IF EXISTS whs;
CREATE DATABASE whs;
USE whs;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Имя покупателя',
  birthday_at DATE COMMENT 'Дата рождения',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Покупатели';


DROP TABLE IF EXISTS catalogs;
CREATE TABLE catalogs (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Название раздела',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  UNIQUE unique_name(name(10))
) COMMENT = 'Разделы интернет-магазина';


DROP TABLE IF EXISTS products;
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Название',
  description TEXT COMMENT 'Описание',
  price DECIMAL (11,2) COMMENT 'Цена',
  catalog_id INT UNSIGNED,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  KEY index_of_catalog_id (catalog_id)
) COMMENT = 'Товарные позиции';


DROP TABLE IF EXISTS logs;
CREATE TABLE logs (
  tbl_name VARCHAR(255) COMMENT 'Название таблицы',
  created_at DATETIME COMMENT 'Дата создания',
  id_key BIGINT COMMENT 'Идентификатор первичного ключа',
  name_content VARCHAR(255) COMMENT 'Содержимое поля name'
) ENGINE = ARCHIVE ;


DELIMITER //
DROP TRIGGER IF EXISTS log_user_insert//
CREATE TRIGGER log_user_insert AFTER INSERT ON users
FOR EACH ROW 
 BEGIN 
  DECLARE tbl_name VARCHAR(255);
  DECLARE created_at DATETIME; 
  DECLARE id_key BIGINT; 
  SELECT table_name INTO tbl_name FROM information_schema.tables where table_name = 'users' and TABLE_SCHEMA = 'whs';
  SELECT created_at INTO created_at FROM users LIMIT 1 ;
  SELECT id INTO id_key FROM users LIMIT 1 ; 
  INSERT INTO logs VALUES (tbl_name, NEW.created_at, NEW.id, NEW.name);
 END 
//

DROP TRIGGER IF EXISTS log_product_insert//
CREATE TRIGGER log_product_insert AFTER INSERT ON products
FOR EACH ROW 
 BEGIN 
  DECLARE tbl_name VARCHAR(255);
  DECLARE created_at DATETIME; 
  DECLARE id_key BIGINT; 
  SELECT table_name INTO tbl_name FROM information_schema.tables where table_name = 'products' and TABLE_SCHEMA = 'whs';
  SELECT created_at INTO created_at FROM products LIMIT 1 ;
  SELECT id INTO id_key FROM products LIMIT 1 ; 
  INSERT INTO logs VALUES (tbl_name, NEW.created_at, NEW.id, NEW.name);
 END 
//

DROP TRIGGER IF EXISTS log_catalogs_insert//
CREATE TRIGGER log_catalogs_insert AFTER INSERT ON catalogs
FOR EACH ROW 
 BEGIN 
  DECLARE tbl_name VARCHAR(255);
  DECLARE created_at DATETIME; 
  DECLARE id_key BIGINT; 
  SELECT table_name INTO tbl_name FROM information_schema.tables where table_name = 'catalogs' and TABLE_SCHEMA = 'whs';
  SELECT created_at INTO created_at FROM catalogs LIMIT 1 ;
  SELECT id INTO id_key FROM catalogs LIMIT 1 ; 
  INSERT INTO logs VALUES (tbl_name, NEW.created_at, NEW.id, NEW.name);
 END 
//

DELIMITER ;

INSERT INTO users (name, birthday_at)  VALUES
  ('Геннадий', '1990-10-05'),
  ('Наталья', '1984-11-12'),
  ('Александр', '1985-05-20'),
  ('Сергей', '1988-02-14'),
  ('Иван', '1998-01-12'),
  ('Мария', '1992-08-29');


INSERT INTO products
  (name, description )
VALUES
  ('Intel Core i3-8100', 'Процессор для настольных персональных компьютеров, основанных на платформе Intel.'),
  ('Intel Core i5-7400', 'Процессор для настольных персональных компьютеров, основанных на платформе Intel.'),
  ('AMD FX-8320E', 'Процессор для настольных персональных компьютеров, основанных на платформе AMD.'),
  ('AMD FX-8320', 'Процессор для настольных персональных компьютеров, основанных на платформе AMD.'),
  ('ASUS ROG MAXIMUS X HERO', 'Материнская плата ASUS ROG MAXIMUS X HERO, Z370, Socket 1151-V2, DDR4, ATX'),
  ('Gigabyte H310M S2H', 'Материнская плата Gigabyte H310M S2H, H310, Socket 1151-V2, DDR4, mATX'),
  ('MSI B250M GAMING PRO', 'Материнская плата MSI B250M GAMING PRO, B250, Socket 1151, DDR4, mATX'),
  ('Gigabyte', 'Материнская плата MSI B250M GAMING PRO, B250, Socket 1151, DDR4, mATX');  
 
INSERT INTO catalogs (name ) VALUES
  ('Процессоры'),
  ('Материнские платы'),
  ('Видеокарты'),
  ('Жесткие диски'),
  ('Оперативная память');
 
 
SELECT * from logs ;
