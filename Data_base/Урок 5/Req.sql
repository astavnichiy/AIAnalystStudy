
-- Задание 1
UPDATE users 
SET created_at = current_timestamp(), 
	updated_at = current_timestamp()
WHERE id > 0; -- для обхода безопасности 

-- Задание 2
ALTER TABLE users
CHANGE COLUMN `created_at` `created_at1` VARCHAR(40) NULL DEFAULT NULL,
CHANGE COLUMN `updated_at` `updated_at1` VARCHAR(40) NULL DEFAULT NULL,
ADD COLUMN `created_at` DATETIME NULL AFTER `updated_at1`,
ADD COLUMN `updated_at` DATETIME NULL AFTER `created_at`;

UPDATE users 
SET created_at = str_to_date(created_at1, '%d.%m.%Y %h:%i'),
	updated_at = str_to_date(updated_at1, '%d.%m.%Y %h:%i')
WHERE id > 0; -- для обхода безопасности 

ALTER TABLE users`
DROP COLUMN `updated_at1`,
DROP COLUMN `created_at1`;

-- Использовал длинный путь, чтобы была возможность серить данные и откатиться, если перенслись криво или не все.

-- Задание 3
-- Мне кажется, что так будет работать
SELECT *
FROM (SELECT * 
	  FROM store.storehouses_products
	  WHERE `value` > 0
	  ORDER BY `value` asc) AS second_table
UNION ALL
SELECT * 
FROM store.storehouses_products
WHERE `value` = 0; 
