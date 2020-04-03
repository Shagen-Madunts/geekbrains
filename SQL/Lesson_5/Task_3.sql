/*В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0, если товар закончился и выше нуля, если на складе имеются запасы. 
 * Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения value. 
 * Однако, нулевые запасы должны выводиться в конце, после всех записей..*/


DROP DATABASE IF EXISTS shop;
CREATE DATABASE shop;
USE shop;


DROP TABLE IF EXISTS storehouses_products;
CREATE TABLE storehouses_products (
  id SERIAL PRIMARY KEY,
  storehouse_id INT UNSIGNED,
  product_id INT UNSIGNED,
  value INT UNSIGNED,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


INSERT INTO storehouses_products (storehouse_id, product_id, value) VALUES
  (1, 1, 20),
  (1, 2, 0),
  (1, 3, 0),
  (1, 4, 0),
  (1, 5, 30),
  (1, 6, 400),
  (1, 7, 5000);


SELECT * FROM storehouses_products ORDER BY value IN (SELECT value FROM storehouses_products WHERE value > 0) DESC;

