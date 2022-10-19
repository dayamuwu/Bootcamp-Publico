-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema citas_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema citas_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `citas_db` ;
USE `citas_db` ;

-- -----------------------------------------------------
-- Table `citas_db`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `citas_db`.`usuarios` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(45) NOT NULL,
    `correo` VARCHAR(200) NOT NULL,
    `contrasena` VARCHAR(200) NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT NOW(),
    `updated_at` DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `citas_db`.`citas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `citas_db`.`citas` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `tareas` VARCHAR(200) NOT NULL,
    `fecha` DATE NOT NULL,
    `estado` VARCHAR(100) NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT NOW(),
    `updated_at` DATETIME NOT NULL DEFAULT NOW(),
    `usuarios_id` INT NOT NULL,
    PRIMARY KEY (`id`, `usuarios_id`),
    INDEX `fk_citas_usuarios_idx` (`usuarios_id` ASC) VISIBLE,
    CONSTRAINT `fk_citas_usuarios`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `citas_db`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
