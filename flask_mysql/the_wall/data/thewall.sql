-- 

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema walldb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema walldb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `walldb` DEFAULT CHARACTER SET utf8 ;
USE `walldb` ;

-- -----------------------------------------------------
-- Table `walldb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `walldb`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `email_address` VARCHAR(255) NULL,
  `password` VARCHAR(255) NOT NULL,
  `salt` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `walldb`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `walldb`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  `message` TEXT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_users_idx` (`user_id` ASC),
  CONSTRAINT `fk_messages_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `walldb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `walldb`.`friend`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `walldb`.`friend` (
  `id` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `walldb`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `walldb`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comment` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `messages_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_messages1_idx` (`messages_id` ASC),
  INDEX `fk_comments_users1_idx` (`user_id` ASC),
  CONSTRAINT `fk_comments_messages1`
    FOREIGN KEY (`messages_id`)
    REFERENCES `walldb`.`messages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `walldb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


-- -----------------------------------------------------
-- Adding data to table: users.
-- -----------------------------------------------------
INSERT INTO `users` (id, first_name, last_name, password, salt, email_address, created_at, updated_at) VALUES (1,'Chris','Baker','6c184c8cc84e9f3d929b9865e1d5d20d','9febcb47a49c6afa2dfec40e4f0216','cbarker@gmail.com', NOW(), NOW()),(2,'Jessica','Davidson','6c184c8cc84e9f3d929b9865e1d5d20d','9febcb47a49c6afa2dfec40e4f0216','jdavidson@yahoo.com',NOW(),NOW()),(3,'James','Johnson','6c184c8cc84e9f3d929b9865e1d5d20d','9febcb47a49c6afa2dfec40e4f0216','jjohnson@codingdojo.com',NOW(),NOW()),(4,'Diana','Smith','6c184c8cc84e9f3d929b9865e1d5d20d','9febcb47a49c6afa2dfec40e4f0216','dmsith@hotmail.com',NOW(),NOW());




