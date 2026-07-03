USE sales_pipeline;

-- SELECT ROUND(SUM(Revenue),2) AS Total_Revenue
-- FROM sales;
-- Total Revenue=> 9737069.01

-- SELECT COUNT(DISTINCT InvoiceNo) AS Total_Orders
-- FROM sales;
-- Total Orders => 25897

-- SELECT COUNT(DISTINCT CustomerID) AS Total_Customers
-- FROM sales
-- WHERE CustomerID IS NOT NULL
-- AND CustomerID <> ''
-- AND CustomerID <> 'UNKNOWN';
--  Total Customers => 4372

-- SELECT COUNT(DISTINCT StockCode) AS Total_Products
-- FROM sales;
--  Total Products => 3957

-- SELECT COUNT(DISTINCT Country) AS Total_Countries
-- FROM sales;
-- Total Countries=> 38

-- SELECT ROUND(
-- SUM(Revenue) /
-- COUNT(DISTINCT CASE
-- WHEN IsReturn = 0 THEN InvoiceNo
-- END),
-- 2) AS Average_Order_Value
-- FROM sales;
-- Average Order Value=> 441.37

-- SELECT COUNT(*) AS Return_Transactions
-- FROM sales
-- WHERE IsReturn = 1;
-- Total Returns => 9251

-- SELECT ROUND(
-- 100 *
-- COUNT(DISTINCT CASE
-- WHEN IsReturn = 1 THEN InvoiceNo
-- END)
-- /
-- COUNT(DISTINCT InvoiceNo),
-- 2
-- ) AS ReturnRate
-- FROM sales;
-- Return Rate => 14.81