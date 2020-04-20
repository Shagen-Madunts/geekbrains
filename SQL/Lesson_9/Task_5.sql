/*В таблице products есть два текстовых поля: name с названием товара и description с его описанием. 
 * Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема. 
 * Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены. 
 * При попытке присвоить полям NULL-значение необходимо отменить операцию.*/
DROP DATABASE IF EXISTS whs;
CREATE DATABASE whs;
USE whs;

DROP TABLE IF EXISTS products;
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Название',
  desription TEXT COMMENT 'Описание'
);

DELIMITER //
DROP TRIGGER IF EXISTS check_insert//
CREATE TRIGGER check_insert BEFORE INSERT ON products
FOR EACH ROW 
 BEGIN 
  DECLARE name_data VARCHAR(255);
  SELECT name INTO name_data FROM products ORDER BY id DESC LIMIT 1;
  IF name_data IS NULL THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'INSERT canceled';
  ELSE 
    SET NEW.name = COALESCE(NEW.name, name_data);
  END IF;
 END 
//


DELIMITER ;
INSERT INTO products
  (name, desription)
VALUES
  ('Intel Core i3-8100', 'Процессор для настольных персональных компьютеров, основанных на платформе Intel.'),
  ('Intel Core i5-7400', 'Процессор для настольных персональных компьютеров, основанных на платформе Intel.'),
  ('AMD FX-8320E', 'Процессор для настольных персональных компьютеров, основанных на платформе AMD.'),
  ('AMD FX-8320', 'Процессор для настольных персональных компьютеров, основанных на платформе AMD.'),
  ('ASUS ROG MAXIMUS X HERO', 'Материнская плата ASUS ROG MAXIMUS X HERO, Z370, Socket 1151-V2, DDR4, ATX'),
  ('Gigabyte H310M S2H', 'Материнская плата Gigabyte H310M S2H, H310, Socket 1151-V2, DDR4, mATX'),
  ('MSI B250M GAMING PRO', 'Материнская плата MSI B250M GAMING PRO, B250, Socket 1151, DDR4, mATX'),
  (NULL, 'Материнская плата MSI B250M GAMING PRO, B250, Socket 1151, DDR4, mATX');  
  
 SELECT * from products p ;
 
