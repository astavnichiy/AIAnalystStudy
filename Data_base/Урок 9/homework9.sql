Задание 1.1.: В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных. Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. Используйте транзакции.

Примечание: Id = 1 удалился. подставил 2. :)

Результат:

START TRANSACTION; 
INSERT INTO sample.users SELECT id, `name` FROM store.users WHERE id = 2;
COMMIT;

Задание 1.2.:Создайте представление, которое выводит название name товарной позиции из таблицы products и соответствующее название каталога name из таблицы catalogs.

Результат:

CREATE VIEW `products_v` AS 
	   SELECT prod.`name` as Product_name, cat.`name` as Category_name
       FROM `products` as prod INNER JOIN `catalogs` as cat
       ON cat.id = prod.catalog_id;
	   
Задание 3.1.:	Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток. С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи".  

Решение:
CREATE DEFINER=`root`@`localhost` PROCEDURE `new_procedure`()
BEGIN
 IF (HOUR(sysdate()) BETWEEN "9" and "12" ) THEN
    SELECT "Доброе утро" AS privet;
 END IF;
 IF (HOUR(sysdate()) BETWEEN "12" and "18" ) THEN
    SELECT "Добрый день" AS privet;
 END IF;
 IF (HOUR(sysdate()) BETWEEN "18" and "24" ) THEN
    SELECT "Доброй ночи" AS privet;
 END IF;

END

Задание 4.1.:В таблице products есть два текстовых поля: name с названием товара и description с его описанием. Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема. Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены. При попытке присвоить полям NULL-значение необходимо отменить операцию.

Решение:
create trigger first1 before insert on products
for each row begin
IF NEW.`name` = '' then
   signal sqlstate '45000';
END IF;
END