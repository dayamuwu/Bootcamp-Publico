-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojos_y_ninjas_02
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dojos_y_ninjas_02
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojos_y_ninjas_02` ;
USE `dojos_y_ninjas_02` ;

-- -----------------------------------------------------
-- Table `dojos_y_ninjas_02`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_y_ninjas_02`.`dojos` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(45) NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT NOW(),
    `update_at` DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dojos_y_ninjas_02`.`ninjas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_y_ninjas_02`.`ninjas` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(45) NOT NULL,
    `apellido` VARCHAR(45) NOT NULL,
    `edad` INT NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT NOW(),
    `update_at` DATETIME NOT NULL DEFAULT NOW(),
    `dojo_id` INT NOT NULL,
    PRIMARY KEY (`id`),
    INDEX `fk_ninjas_dojos_idx` (`dojo_id` ASC) VISIBLE,
    CONSTRAINT `fk_ninjas_dojos`
    FOREIGN KEY (`dojo_id`)
    REFERENCES `dojos_y_ninjas_02`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
