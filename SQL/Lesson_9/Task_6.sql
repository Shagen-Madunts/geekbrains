/*Напишите хранимую функцию для вычисления произвольного числа Фибоначчи. 
 * Числами Фибоначчи называется последовательность в которой число равно сумме двух предыдущих чисел. 
 * Вызов функции FIBONACCI(10) должен возвращать число 55*/

DROP DATABASE IF EXISTS tmp;
CREATE DATABASE tmp;
USE tmp;

DROP FUNCTION IF EXISTS FIBONACCI;

DELIMITER //
CREATE FUNCTION FIBONACCI(num INT) 
  RETURNS INT
  BEGIN
    DECLARE a INT DEFAULT 0;
	DECLARE b INT DEFAULT 1;
	DECLARE c INT DEFAULT 2;
	DECLARE i INT DEFAULT 0;
    IF num = 0 THEN
	  RETURN a;
    ELSEIF num = 1 THEN
  	  RETURN b;
    ELSE
      WHILE i < num-1 DO
       SET c = a + b;
       SET a = b;
       SET b = c;
       SET i = i + 1;
      END WHILE;      
      RETURN b;
    END IF;
  END
//

DELIMITER ;
SELECT FIBONACCI(10);
