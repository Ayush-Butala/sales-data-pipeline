-- DROP DATABASE IF EXISTS sales_pipeline;
-- CREATE DATABASE sales_pipeline;
-- USE sales_pipeline;

-- CREATE TABLE sales (
--     InvoiceNo VARCHAR(20),
--     StockCode VARCHAR(20),
--     Description VARCHAR(255),
--     CustomerID VARCHAR(20),
--     Country VARCHAR(100),
--     InvoiceDate DATETIME,
--     Year SMALLINT,
--     Quarter CHAR(2),
--     Month VARCHAR(15),
--     MonthNumber TINYINT,
--     DayOfWeek VARCHAR(15),
--     Quantity INT,
--     UnitPrice DECIMAL(10,2),
--     Revenue DECIMAL(12,2),
--     TransactionType VARCHAR(10),
--     IsReturn BOOLEAN
-- );

-- SET GLOBAL local_infile = 1;
-- SHOW VARIABLES LIKE 'local_infile';

LOAD DATA LOCAL INFILE 'C:/Users/AYUSH BUTALA/OneDrive/Desktop/Coding/Sales_Data_Pipeline/data/cleaned_data/analytics_sales.csv'
INTO TABLE sales
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    InvoiceNo,
    StockCode,
    Description,
    CustomerID,
    Country,
    InvoiceDate,
    Year,
    Quarter,
    Month,
    MonthNumber,
    DayOfWeek,
    Quantity,
    UnitPrice,
    Revenue,
    TransactionType,
    IsReturn
);

-- DROP TABLE IF EXISTS sales;