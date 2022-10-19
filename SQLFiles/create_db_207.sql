-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Parts207`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Parts207` (
  `partNo007` INT NOT NULL,
  `partName207` VARCHAR(45) NULL,
  `currentPrice207` DECIMAL NULL,
  `qoh207` INT NULL,
  PRIMARY KEY (`partNo007`),
  UNIQUE INDEX `idParts007_207_UNIQUE` (`partNo007` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Clients207`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Clients207` (
  `clientId207` INT NOT NULL,
  `clientName207` VARCHAR(45) NULL,
  `clientCity207` VARCHAR(45) NULL,
  `clientPassword207` VARCHAR(45) NULL,
  `moneyOwned207` VARCHAR(45) NULL,
  PRIMARY KEY (`clientId207`),
  UNIQUE INDEX `clientId207_UNIQUE` (`clientId207` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`POs207`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`POs207` (
  `poNo207` INT NOT NULL,
  `clientCompID207` VARCHAR(45) NULL,
  `dataOfPO207` DATE NULL,
  `status207` VARCHAR(45) NULL,
  `Clients207_clientId207` INT NOT NULL,
  PRIMARY KEY (`poNo207`, `Clients207_clientId207`),
  UNIQUE INDEX `poNo207_UNIQUE` (`poNo207` ASC) VISIBLE,
  INDEX `fk_POs207_Clients2071_idx` (`Clients207_clientId207` ASC) VISIBLE,
  CONSTRAINT `fk_POs207_Clients2071`
    FOREIGN KEY (`Clients207_clientId207`)
    REFERENCES `mydb`.`Clients207` (`clientId207`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Lines207`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Lines207` (
  `POs207_poNo207` INT NOT NULL,
  `Parts207_partNo007` INT NOT NULL,
  `lineNo207` INT NOT NULL,
  `qty207` INT NULL,
  `priceOrdered207` DECIMAL NULL,
  PRIMARY KEY (`POs207_poNo207`, `Parts207_partNo007`, `lineNo207`),
  INDEX `fk_POs207_has_Parts207_Parts2071_idx` (`Parts207_partNo007` ASC) VISIBLE,
  INDEX `fk_POs207_has_Parts207_POs207_idx` (`POs207_poNo207` ASC) VISIBLE,
  CONSTRAINT `fk_POs207_has_Parts207_POs207`
    FOREIGN KEY (`POs207_poNo207`)
    REFERENCES `mydb`.`POs207` (`poNo207`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_POs207_has_Parts207_Parts2071`
    FOREIGN KEY (`Parts207_partNo007`)
    REFERENCES `mydb`.`Parts207` (`partNo007`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
