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
CREATE SCHEMA IF NOT EXISTS `friendsdb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `friendsdb` ;

-- -----------------------------------------------------
-- Table `mydb`.`friends`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendsdb`.`friends` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `age` int(11) NULL,
  `occupation` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


INSERT INTO friends(first_name, last_name, age, occupation, created_at, updated_at), ("Jay", "Patel", 35, "Instructor", NOW(), NOW()), (first_name, last_name, age, occupation, created_at, updated_at),("Jimmy", "Jun", 40, "Instructor", NOW(), NOW()),("James", "Johnson", 18, "Student", NOW(), NOW()),("George", "Lopez", 52, "Comedian", NOW(), NOW());