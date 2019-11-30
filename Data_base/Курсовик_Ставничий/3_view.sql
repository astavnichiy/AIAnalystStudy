CREATE OR REPLACE
VIEW `AntiFraud`.`clients_with_alert` AS
select
    `AntiFraud`.`clients`.`id` AS `id`,
    `AntiFraud`.`clients`.`fullname` AS `fullname`,
    `AntiFraud`.`clients`.`age` AS `age`,
    `AntiFraud`.`clients`.`document` AS `document`,
    `AntiFraud`.`clients`.`sex` AS `sex`
from
     `AntiFraud`.`clients` join `AntiFraud`.`payments`as `pay1` on
     `AntiFraud`.`clients`.`id` = `pay1`.`client_id`
join `AntiFraud`.`alerts` on `AntiFraud`.`alerts`.`payment_id` = `pay1`.`id`
where
    `AntiFraud`.`alerts`.`resolution` is null
	
CREATE OR REPLACE
VIEW `AntiFraud`.`clients_alert_count` AS
select
	COUNT(`AntiFraud`.`clients`.`fullname`),
    `AntiFraud`.`clients`.`fullname` AS `fullname`
from
     `AntiFraud`.`clients` join `AntiFraud`.`payments`as `pay1` on
     `AntiFraud`.`clients`.`id` = `pay1`.`client_id`
join `AntiFraud`.`alerts` on `AntiFraud`.`alerts`.`payment_id` = `pay1`.`id`
where
    `AntiFraud`.`alerts`.`resolution` = 'Мошенничество'
group by `AntiFraud`.`clients`.`fullname`
 
	
