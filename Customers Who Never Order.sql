# Write your MySQL query statement below
SELECT C.name AS Customers
FROM Customers C 
WHERE C.id NOT IN ( 
    SELECT C.id
    FROM Customers C, Orders O
    WHERE C.id = O.customerId )
