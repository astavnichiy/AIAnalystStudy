Задание 1: Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине

Ответ:

select distinct users.name, users.birthday_at
from users inner join orders on users.id = orders.user_id


Задание 2: 

Ответь:

select products.*, catalogs.name
from products left join catalogs on products.catalog_id = catalogs.id




Задание 3: (по желанию) Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name). Поля from, to и label содержат английские названия городов, поле name — русское. Выведите список рейсов flights с русскими названиями городов.

Ответ:

select 
  flights1.id, 
  cities1.`name`, 
  cities2.`name`
from 
  flights as flights1 LEFT JOIN cities as cities1 ON flights1.`from` = cities1.`label`,
  flights as flights2 LEFT JOIN cities as cities2 ON flights2.`to` = cities2.`label`
where 1=1
  and flights1.id = flights2.id
  and cities1.`name` REGEXP '[а-яА-Я]'
  and cities2.`name` REGEXP '[а-яА-Я]'