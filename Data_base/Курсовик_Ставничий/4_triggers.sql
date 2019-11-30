CREATE TRIGGER `payments_AFTER_INSERT` AFTER INSERT ON `payments` FOR EACH ROW BEGIN
	IF(NEW.dst_card IN (SELECT `card_number` FROM black_list_card )) THEN
       INSERT INTO alerts Set payment_id = NEW.id, `status` = 'Новый', `reason` = 'Карта получателя в черном списке';
	END IF;
END

CREATE TRIGGER `payments_AFTER_INS2` AFTER INSERT ON `payments` FOR EACH ROW BEGIN
	IF(NEW.dst_phone IN (SELECT `phone` FROM black_list_phone )) THEN
       INSERT INTO alerts Set payment_id = NEW.id, `status` = 'Новый', `reason` = 'Телефон получателя в черном списке';
	END IF;
END

CREATE TRIGGER `payments_AFTER_INS3` AFTER INSERT ON `payments` FOR EACH ROW BEGIN
	IF(NEW.sum > NEW.balance - 10) THEN
       INSERT INTO alerts Set payment_id = NEW.id, `status` = 'Новый', `reason` = 'Попытка обнуления счета';
	END IF;
END