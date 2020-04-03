/*Подсчитайте произведение чисел в столбце таблицы.*/

DROP DATABASE IF EXISTS shop;
CREATE DATABASE shop;
USE shop;


DROP TABLE IF EXISTS numbers;
CREATE TABLE numbers (
  num BIGINT
);

INSERT INTO numbers (num) VALUES
  (2),
  (3),
  (4),
  (5),
  (6);

 
 SELECT exp(SUM(log(num))) mult FROM numbers;
 