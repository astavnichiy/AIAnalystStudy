ALTER TABLE `geodata`.`_countries` 
ADD COLUMN `title` VARCHAR(150) NOT NULL AFTER `title_cz`,
CHANGE COLUMN `country_id` `id` INT(11) NOT NULL AUTO_INCREMENT ,
ADD PRIMARY KEY (`id`),
ADD INDEX `INDEX` (`title` ASC) VISIBLE;

ALTER TABLE `geodata`.`_regions` 
ADD COLUMN `title` VARCHAR(150) NULL AFTER `title_cz`,
CHANGE COLUMN `region_id` `id` INT(11) NOT NULL AUTO_INCREMENT ,
ADD PRIMARY KEY (`id`),
ADD INDEX `INDEX` (`title` ASC) VISIBLE;
;
ALTER TABLE `geodata`.`_regions` 
ADD INDEX `FK_REGIONS_idx` (`country_id` ASC) VISIBLE;
;
ALTER TABLE `geodata`.`_regions` 
ADD CONSTRAINT `FK_REGIONS`
  FOREIGN KEY (`country_id`)
  REFERENCES `geodata`.`_countries` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
  
ALTER TABLE `geodata`.`_cities` 
ADD COLUMN `title` VARCHAR(150) NOT NULL AFTER `region_cz`,
CHANGE COLUMN `city_id` `id` INT(11) NOT NULL AUTO_INCREMENT ,
CHANGE COLUMN `region_id` `region_id` INT(11) NULL ,
ADD PRIMARY KEY (`id`),
ADD INDEX `INDEX` (`title` ASC) INVISIBLE,
ADD INDEX `FK_country_id_idx` (`country_id` ASC) VISIBLE,
ADD INDEX `FK_region_id_idx` (`region_id` ASC) VISIBLE;
;
ALTER TABLE `geodata`.`_cities` 
ADD CONSTRAINT `FK_country_id`
  FOREIGN KEY (`country_id`)
  REFERENCES `geodata`.`_countries` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `FK_region_id`
  FOREIGN KEY (`region_id`)
  REFERENCES `geodata`.`_regions` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
  

