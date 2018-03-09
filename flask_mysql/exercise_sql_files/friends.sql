-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema friends
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema friends
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `friends` DEFAULT CHARACTER SET utf8 ;
USE `friends` ;

-- -----------------------------------------------------
-- Table `friends`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friends`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `friends`.`friendships`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friends`.`friendships` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NULL,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  `friend_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_friendships_uses_idx` (`user_id` ASC),
  INDEX `fk_friendships_users1_idx` (`friend_id` ASC),
  CONSTRAINT `fk_friendships_uses`
    FOREIGN KEY (`user_id`)
    REFERENCES `friends`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_friendships_users1`
    FOREIGN KEY (`friend_id`)
    REFERENCES `friends`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `friends`.`friend`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friends`.`friend` (
  `id` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
