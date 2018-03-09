-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema loginsdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema loginsdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `loginsdb` DEFAULT CHARACTER SET utf8 ;
USE `loginsdb` ;

-- -----------------------------------------------------
-- Table `loginsdb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `loginsdb`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `salt` VARCHAR(45) NULL,
  `email_address` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `loginsdb`.`registrations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `loginsdb`.`registrations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_registrations_users_idx` (`user_id` ASC),
  CONSTRAINT `fk_registrations_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `loginsdb`.`users` (`id`)
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




