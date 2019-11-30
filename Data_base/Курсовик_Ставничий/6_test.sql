-- Тестирование триггеров:

INSERT INTO `AntiFraud`.`payments` ( `client_id`, `processing_number`, `sum`, `commition`, `type_id`, `channel_id`, `dst_card`, `dst_phone`, `balance`) VALUES ('1', '1', '100', '10', '1', '1', '111111111111', '', '1000');

INSERT INTO `AntiFraud`.`payments` (`client_id`, `processing_number`, `sum`, `commition`, `type_id`, `channel_id`, `dst_card`, `dst_phone`, `balance`) VALUES ('2', '2', '100', '10', '1', '1', '', '', '101');

INSERT INTO `AntiFraud`.`payments` (`client_id`, `processing_number`, `sum`, `commition`, `type_id`, `channel_id`, `dst_card`, `dst_phone`, `balance`) VALUES ('3', '3', '100', '10', '2', '2', '111111111111', '', '101');
