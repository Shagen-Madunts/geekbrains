/*� ������� ��������� ������� storehouses_products � ���� value ����� ����������� ����� ������ �����: 0, 
 * ���� ����� ���������� � ���� ����, ���� �� ������ ������� ������. ���������� ������������� ������ ����� �������, 
 * ����� ��� ���������� � ������� ���������� �������� value. ������, ������� ������ ������ ���������� � �����, ����� ���� �������.*/


DROP DATABASE IF EXISTS shop;
CREATE DATABASE shop;
USE shop;


DROP TABLE IF EXISTS storehouses_products;
CREATE TABLE storehouses_products (
  id SERIAL PRIMARY KEY,
  storehouse_id INT UNSIGNED,
  product_id INT UNSIGNED,
  value INT UNSIGNED COMMENT '����� �������� ������� �� ������',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = '������ �� ������';


INSERT INTO storehouses_products (storehouse_id, product_id, value) VALUES
  (1, 1, 20),
  (1, 2, 0),
  (1, 3, 0),
  (1, 4, 0),
  (1, 5, 30),
  (1, 6, 400),
  (1, 7, 5000);


SELECT * FROM storehouses_products ORDER BY value IN (SELECT value FROM storehouses_products WHERE value > 0) DESC;

