-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `emailsdb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `emailsdb` ;

-- -----------------------------------------------------
-- Table `mydb`.`emails`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `emailsdb`.`emails` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

LOCK TABLES `emails` WRITE;
INSERT INTO emails(id, first_name, last_name, email, created_at, updated_at) VALUES (1, "Jay", "Patel", "jpatel@yahoo.com", NOW(), NOW()),(2, "Jimmy", "Jun", "jjun@gmail.com", NOW(), NOW()),(3, "James", "Johnson", "jjohnson@codingdojo.com", NOW(), NOW()),(4, "George", "Lopez", "glopez@hotmail.com", NOW(), NOW());