Задание 2: 
Пусть задан некоторый пользователь.
Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим
пользоваетелем.

Запрос: 
SELECT 
count(1) as `nub_mes`, 
from_user_id
FROM vk.messages
Where users_id = 1 -- некоторый пользователь
GROUP BY from_user_id
ORDER BY nub_mes desc
LIMIT 1
;


Задание 3: 
Подсчитать общее количество лайков, которые получили 10 самых молодых пользователей.

select user_id,
	   (select count(1) 
        from likes 
		where likes.id = prof.user_id 
        Group by likes.user_id) as like_count
from `profiles` as prof
where 1=1
ORDER BY birthday DESC
Limit 10;

-- неправилдьно

Задание 4: Определить кто больше поставил лайков (всего) - мужчины или женщины?

Запрос:

select 
sex,
count(id)
from
	(select sex, likes.id
	from `profiles` as prof, likes
	where likes.id = prof.user_id) as sexlike
GROUP BY sexlike.sex



Задание 5: Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной
сети.
-- За наименьшую активность принимаю пользователей, которые меньше всего сделали лайков и которрые меньше написали сообщений за последний месяц  


Select count(1) as activity, `user`
from 
	(select from_user_id as `user`, created_at  
	from messages
	where created_at > NOW() - INTERVAL 1 MONTH
	union all
	select user_id as `user` , created_at
	from likes
	where created_at > NOW() - INTERVAL 1 MONTH) as activeuser
GROUP BY `user`
ORDER BY activity ASC
LIMIT 10
    