
CREATE TABLE `black_list_phone` (
  `phone` varchar(10) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `black_list_card` (
  `card_number` varchar(28) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `AntiFraud`.`channels` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  `desc` VARCHAR(255) NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `AntiFraud`.`ptypes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  `desc` VARCHAR(255) NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `AntiFraud`.`phones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `phone_number` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `AntiFraud`.`phone_types` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `clients` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fullname` varchar(100) NOT NULL,
  `age` int(3) NOT NULL,
  `document` int(11) NOT NULL,
  `sex` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `AntiFraud`.`white_list` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `dst_card` VARCHAR(28) NULL,
  `dst_phone` VARCHAR(12) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_white_list_1_idx` (`client_id` ASC) VISIBLE,
  CONSTRAINT `fk_white_list_1`
    FOREIGN KEY (`client_id`)
    REFERENCES `AntiFraud`.`clients` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


CREATE TABLE `phone_links` (
  `phone_type_id` int(11) NOT NULL,
  `phone_id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  `status` enum('Активно','Устаревший') DEFAULT NULL,
  PRIMARY KEY (`phone_type_id`,`phone_id`,`client_id`),
  KEY `fk_phone_links_client_idx` (`client_id`),
  KEY `fk_phone_links_phone_idx` (`phone_id`),
  KEY `index4` (`phone_type_id`,`phone_id`,`client_id`),
  CONSTRAINT `fk_phone_links_client` FOREIGN KEY (`client_id`) REFERENCES `clients` (`id`),
  CONSTRAINT `fk_phone_links_phone` FOREIGN KEY (`phone_id`) REFERENCES `phones` (`id`),
  CONSTRAINT `fk_phone_links_type` FOREIGN KEY (`phone_type_id`) REFERENCES `phone_types` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `payments` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `client_id` int(11) NOT NULL,
  `processing_number` int(11) NOT NULL,
  `sum` decimal(10,2) NOT NULL,
  `commition` decimal(10,2) DEFAULT NULL,
  `type_id` int(11) NOT NULL,
  `channel_id` int(11) NOT NULL,
  `dst_card` varchar(28) DEFAULT NULL,
  `dst_phone` varchar(12) DEFAULT NULL,
  `balance` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_payments_1_idx` (`type_id`),
  KEY `fk_payments_channels_idx` (`channel_id`),
  KEY `fk_payments_client_idx` (`client_id`),
  CONSTRAINT `fk_payments_channels` FOREIGN KEY (`channel_id`) REFERENCES `channels` (`id`),
  CONSTRAINT `fk_payments_client` FOREIGN KEY (`client_id`) REFERENCES `clients` (`id`),
  CONSTRAINT `fk_payments_ptypes` FOREIGN KEY (`type_id`) REFERENCES `ptypes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `alerts` (
  `payment_id` bigint(20) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reason` varchar(255) DEFAULT NULL,
  `status` varchar(45) NOT NULL,
  `resolution` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_new_table_1_idx` (`payment_id`),
  CONSTRAINT `fk_new_table_1` FOREIGN KEY (`payment_id`) REFERENCES `payments` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



