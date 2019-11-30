1. Добавить необходимые внешние ключи для всех таблиц базы данных vk (приложить команды).
Ответ: Получилось так, что я это сдела ранее. Не сохранял запросы. :(


2. По созданным связям создать ER диаграмму, используя Dbeaver (приложить графический файл к ДЗ).
Примечание: при просмотре своей схемы, увидел ошибку. И изменил ее с помощью workBench. А Dbeaver, пока не перезагрузил, ее не увидел. 

Ответ: приложен

3. Переписать запросы, заданые к ДЗ урока 6 с использованием JOIN (четыре запроса).
3.2:

SELECT (SELECT CONCAT(first_name, ' ', last_name) FROM users WHERE id = from_user_id) AS friend,
  COUNT(*) AS total_messages 
  FROM messages INNER JOIN (SELECT friend_id AS id 
                             FROM friendship 
                             --  WHERE user_id = 52
                             UNION
                             SELECT user_id AS id 
                             FROM friendship 
                             -- WHERE friend_id = 52
                             ) as users
  ON messages.from_user_id = users.id 
  WHERE to_user_id = 53 
  GROUP BY messages.from_user_id
  ORDER BY total_messages DESC
  ;


3.3:
SELECT SUM(likes_per_user) AS likes_total 
FROM ( 
      SELECT COUNT(*) AS likes_per_user 
      FROM likes INNER JOIN (SELECT user_id 
                             FROM profiles 
                             ORDER BY birthday 
                             DESC LIMIT 10
							) AS sorted_profiles 
      WHERE target_type_id = 3
        AND target_id = sorted_profiles.user_id 
      GROUP BY target_id
) AS counted_likes;

3.4:
 -- Я бы оставил как есть. Красивый запрос. 
SELECT CASE(sex)
		WHEN 'm' THEN 'male'
		WHEN 'f' THEN 'female'
	END AS sex, 
	COUNT(*) as likes_count 
	  FROM (
	    SELECT 
	      user_id as user, 
		    (SELECT sex FROM profiles WHERE user_id = user) as sex 
		  FROM likes) dummy_table 
  GROUP BY sex;

3.5:
 -- Тут не нужен join вообще
SELECT CONCAT(first_name, ' ', last_name) AS user, 
	(SELECT COUNT(*) FROM likes WHERE likes.user_id = users.id) + 
	(SELECT COUNT(*) FROM media WHERE media.user_id = users.id) + 
	(SELECT COUNT(*) FROM messages WHERE messages.from_user_id = users.id) 
	AS overall_activity 
	FROM users
	ORDER BY overall_activity
	LIMIT 10;


