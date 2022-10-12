-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Tv
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Tv
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Tv` ;
USE `Tv` ;

-- -----------------------------------------------------
-- Table `Tv`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Tv`.`usuarios` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(45) NOT NULL,
    `apellido` VARCHAR(45) NOT NULL,
    `correo` VARCHAR(45) NOT NULL,
    `contraseña` VARCHAR(45) NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT NOW(),
    `update_at` DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Tv`.`programas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Tv`.`programas` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `titulo` VARCHAR(45) NOT NULL,
    `canal` VARCHAR(45) NOT NULL,
    `lanzamiento` DATE NOT NULL,
    `descripcion` VARCHAR(45) NULL,
    `created_at` DATETIME NOT NULL,
    `update_at` DATETIME NOT NULL,
    `usuarios_id` INT NOT NULL,
    PRIMARY KEY (`id`),
    INDEX `fk_programas_usuarios_idx` (`usuarios_id` ASC) VISIBLE,
    CONSTRAINT `fk_programas_usuarios`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `Tv`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
