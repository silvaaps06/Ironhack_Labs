CREATE DATABASE lab_mysql;

CREATE TABLE lab_mysql.Cars (ID INT, 
					VIN VARCHAR(52),
					Manufacturer VARCHAR(52),
                    Model VARCHAR(52), 
                    `Year` INT,
                    Color VARCHAR(52));
                    
CREATE TABLE lab_mysql.Customers (ID INT, 
						`Customer ID` INT,
						`Name` VARCHAR(52),
						Phone VARCHAR(52), 
						Email VARCHAR(52),
						Address VARCHAR(52),
                        City VARCHAR(52),
                        `State/Province` VARCHAR(52),
                        Country VARCHAR(52),
                        Postal INT);
                        
CREATE TABLE lab_mysql.Salesperson (ID INT,
									`Staff ID` INT, 
									`Name` VARCHAR(52),
									Store VARCHAR(52));
                                    
CREATE TABLE lab_mysql.Invoices (ID INT,
								`Invoice Number` INT, 
								`Date` DATE,
								Car INT, 
								Customer INT,
								Salesperson INT); 