CREATE DATABASE IF NOT EXISTS got;
USE got;
DROP TABLE IF EXISTS got_script;
SET GLOBAL sql_mode='';
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema got
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema got
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `got` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `got` ;

-- -----------------------------------------------------
-- Table `got`.`got_script`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `got`.`got_script` (
  `index` VARCHAR(20) NOT NULL,
  `Release Date` VARCHAR(45) NULL,
  `Season` VARCHAR(20) NOT NULL,
  `Episode` VARCHAR(20) NOT NULL,
  `Episode Title` VARCHAR(45) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Sentence` LONGTEXT NOT NULL,
  PRIMARY KEY (`index`)
  )
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/got_script.csv' 
	INTO TABLE got_script
	FIELDS TERMINATED BY ',' 
	ENCLOSED BY '"'
	LINES TERMINATED BY '\r\n'
	IGNORE 1 ROWS;

ALTER TABLE got_script RENAME COLUMN `index` TO ID;
ALTER TABLE got_script MODIFY ID INTEGER;

-- Testing queries
SELECT * FROM got_script;

SELECT Sentence FROM got_script
WHERE Name = "Jon Snow"
ORDER BY RAND()
LIMIT 1
;

CREATE TEMPORARY TABLE top10sentence
SELECT Name, count('Sentence') FROM got_script
	GROUP BY Name
    ORDER BY count('Sentence') DESC
    LIMIT 10;

SELECT * FROM top10sentence
GROUP BY Name;

SELECT * FROM got_script
WHERE Name IN
	(SELECT Name FROM top10sentence);
    
SELECT ID, Season, Episode, `Episode Title`, Name, Sentence FROM got_script
	WHERE Season = "Season 1"
		AND Episode = "Episode 1";

