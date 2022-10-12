-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Tv_db2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Tv_db2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Tv_db2` ;
USE `Tv_db2` ;

-- -----------------------------------------------------
-- Table `Tv_db2`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Tv_db2`.`usuarios` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(45) NOT NULL,
    `apellido` VARCHAR(45) NOT NULL,
    `correo` VARCHAR(45) NOT NULL,
    `contraseña` VARCHAR(200) NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT NOW(),
    `update_at` DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Tv_db2`.`programas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Tv_db2`.`programas` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `titulo` VARCHAR(45) NOT NULL,
    `canal` VARCHAR(45) NOT NULL,
    `lanzamiento` DATE NOT NULL,
    `descripcion` VARCHAR(45) NULL,
    `created_at` DATETIME NOT NULL DEFAULT NOW(),
    `update_at` DATETIME NOT NULL DEFAULT NOW(),
    `usuarios_id` INT NOT NULL,
    PRIMARY KEY (`id`),
    INDEX `fk_programas_usuarios_idx` (`usuarios_id` ASC) VISIBLE,
    CONSTRAINT `fk_programas_usuarios`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `Tv_db2`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
