-- Quantity by Manufacturer
SELECT [Manufacturer Description], 
       SUM([Quantity Industry Registration]) AS Total_Quantity
FROM vehicle_data
GROUP BY [Manufacturer Description]
ORDER BY Total_Quantity DESC;

-- Quantity by Sales Type
SELECT [Sales Type], 
       SUM([Quantity Industry Registration]) AS Total_Quantity
FROM vehicle_data
GROUP BY [Sales Type];

-- Monthly Trend
SELECT MONTH([Registration Date]) AS Month, 
       SUM([Quantity Industry Registration]) AS Total_Quantity
FROM vehicle_data
GROUP BY MONTH([Registration Date])
ORDER BY Month;

-- Record Count by Manufacturer
SELECT [Manufacturer Description], 
       COUNT(*) AS Count_Records
FROM vehicle_data
GROUP BY [Manufacturer Description]
ORDER BY Count_Records DESC;