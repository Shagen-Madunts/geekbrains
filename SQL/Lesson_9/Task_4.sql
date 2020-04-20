/* Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток. 
 * С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", с 12:00 до 18:00 функция должна возвращать фразу 
 * "Добрый день", с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи"*/
DROP DATABASE IF EXISTS tmp;
CREATE DATABASE tmp;
USE tmp;

DROP FUNCTION IF EXISTS hello;

DELIMITER //
CREATE FUNCTION hello() 
RETURNS VARCHAR(255) DETERMINISTIC
 begin	
	 DECLARE period INT;
	 set period =  DATE_FORMAT(NOW(), '%H');
	 if (period > 6 and period <= 12) then
	     RETURN 'Доброе утро';
	 end if;
	 if (period > 12 and period <= 18) then
	     RETURN 'Добрый день';
	 end if;
	 if (period > 18 and period <= 00) then
	     RETURN 'Добрый вечер';
	 end if;
	 if (period > 1 and period <= 6) then
	     RETURN 'Доброй ночи';
	 end if;
 end
//

DELIMITER ;
SELECT hello();
