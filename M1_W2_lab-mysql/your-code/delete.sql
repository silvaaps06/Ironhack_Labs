/* Changing the safe mode (0 off) (1 on) */
SET SQL_SAFE_UPDATES = 0;

DELETE FROM lab_mysql.Cars
WHERE ID = 4;

SET SQL_SAFE_UPDATES = 1;

SELECT * FROM lab_mysql.Cars;