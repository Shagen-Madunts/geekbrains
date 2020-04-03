/*�� ������� users ���������� ������� �������������, ���������� � ������� � ���. 
 * ������ ������ � ���� ������ ���������� �������� ('may', 'august')*/

DROP DATABASE IF EXISTS shop;
CREATE DATABASE shop;
USE shop;


DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT '��� ����������',
  birthday_at DATE COMMENT '���� ��������',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = '����������';

INSERT INTO users (name, birthday_at) VALUES
  ('��������', '1990-10-05'),
  ('�������', '1984-11-12'),
  ('���������', '1985-05-20'),
  ('������', '1988-02-14'),
  ('����', '1998-01-12'),
  ('�����', '1992-08-29');
  
 -- SELECT * from users WHERE MONTH(STR_TO_DATE(birthday_at, '%Y-%m-%d')) IN (5,8);

 SELECT * from users WHERE DATE_FORMAT(birthday_at, '%M') in('may', 'august');