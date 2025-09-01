# Write your MySQL query statement below
SELECT unique_id, name FROM EmployeeUNI as eu
RIGHT JOIN Employees as e
ON e.id = eu.id; 