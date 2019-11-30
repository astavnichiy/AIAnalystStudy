INSERT INTO `AntiFraud`.`ptypes` (`name`, `desc`) VALUES ('На телефон', 'Перевод по телефонному номеру');
INSERT INTO `AntiFraud`.`ptypes` (`name`, `desc`) VALUES ('На карту', 'Перевод на карту любого банка');


INSERT INTO `AntiFraud`.`channels` (`name`, `desc`) VALUES ('Мобильный банк', 'Мобильное банковское приложение');
INSERT INTO `AntiFraud`.`channels` (`name`, `desc`) VALUES ('Интернет банк', 'Интернет банк');


INSERT INTO `AntiFraud`.`black_list_card` (`card_number`) VALUES ('111111111111');
INSERT INTO `AntiFraud`.`black_list_card` (`card_number`) VALUES ('222222222222');

INSERT INTO `AntiFraud`.`black_list_phone` (`phone`) VALUES ('9055731183');
INSERT INTO `AntiFraud`.`black_list_phone` (`phone`) VALUES ('9262450735');


INSERT INTO `AntiFraud`.`phones` (`phone_number`) VALUES ('9099091122');
INSERT INTO `AntiFraud`.`phones` (`phone_number`) VALUES ('8088082211');
INSERT INTO `AntiFraud`.`phones` (`phone_number`) VALUES ('9019014020');
INSERT INTO `AntiFraud`.`phones` (`phone_number`) VALUES ('9019012020');
INSERT INTO `AntiFraud`.`phones` (`phone_number`) VALUES ('9209200101');
INSERT INTO `AntiFraud`.`phones` (`phone_number`) VALUES ('9099090101');

INSERT INTO `AntiFraud`.`phone_types` (`type`) VALUES ('Для СМС');
INSERT INTO `AntiFraud`.`phone_types` (`type`) VALUES ('Рабочий');
INSERT INTO `AntiFraud`.`phone_types` (`type`) VALUES ('Домашний');


INSERT INTO `clients` VALUES ('1','Manley Franecki','541','2147483647','a'),
('2','Margarete Will','591','2147483647','h'),
('3','Telly Douglas','293','2147483647','y'),
('4','Mrs. Zelma Kling IV','914','2147483647','a'),
('5','Carrie Hayes','255','2147483647','e'); 


INSERT INTO `AntiFraud`.`phone_links` (`phone_type_id`, `phone_id`, `client_id`, `status`) VALUES ('1', '1', '2', 'Активно');
INSERT INTO `AntiFraud`.`phone_links` (`phone_type_id`, `phone_id`, `client_id`, `status`) VALUES ('2', '1', '3', 'Активно');
INSERT INTO `AntiFraud`.`phone_links` (`phone_type_id`, `phone_id`, `client_id`, `status`) VALUES ('1', '2', '3', 'Активно');
INSERT INTO `AntiFraud`.`phone_links` (`phone_type_id`, `phone_id`, `client_id`, `status`) VALUES ('3', '3', '1', 'Активно');
INSERT INTO `AntiFraud`.`phone_links` (`phone_type_id`, `phone_id`, `client_id`, `status`) VALUES ('3', '1', '2', 'Устаревший');
