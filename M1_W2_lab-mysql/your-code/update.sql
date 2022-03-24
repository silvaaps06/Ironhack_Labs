
/* Changing the safe mode (0 off) (1 on) */
SET SQL_SAFE_UPDATES = 0;

UPDATE lab_mysql.Customers
SET Email = "ppicasso@gmail.com"
WHERE ID LIKE 0;

UPDATE lab_mysql.Salesperson
SET Store = "Miami"
WHERE Name LIKE "Paige Turner";

SET SQL_SAFE_UPDATES = 1;