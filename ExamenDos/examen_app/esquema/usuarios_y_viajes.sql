-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema usuarios_y_viajes_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema usuarios_y_viajes_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `usuarios_y_viajes_db` ;
USE `usuarios_y_viajes_db` ;

-- -----------------------------------------------------
-- Table `usuarios_y_viajes_db`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `usuarios_y_viajes_db`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `correo` VARCHAR(45) NOT NULL,
  `contrasena` VARCHAR(200) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `usuarios_y_viajes_db`.`viajes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `usuarios_y_viajes_db`.`viajes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `plan` VARCHAR(45) NOT NULL,
  `inicio_viaje` DATE NOT NULL,
  `fin_viaje` DATE NOT NULL,
  `descripcion` VARCHAR(200) NOT NULL,
  `creado_por` INT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = armscii8;


-- -----------------------------------------------------
-- Table `usuarios_y_viajes_db`.`usuarios_y_viajes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `usuarios_y_viajes_db`.`usuarios_y_viajes` (
  `usuarios_id` INT NOT NULL,
  `viajes_id` INT NOT NULL,
  PRIMARY KEY (`usuarios_id`, `viajes_id`),
  INDEX `fk_usuarios_has_viajes_viajes1_idx` (`viajes_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_viajes_usuarios_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_has_viajes_usuarios`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `usuarios_y_viajes_db`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_viajes_viajes1`
    FOREIGN KEY (`viajes_id`)
    REFERENCES `usuarios_y_viajes_db`.`viajes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
