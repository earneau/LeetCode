-- Link to the exercise : https://leetcode.com/problems/find-customer-referee/description/?envType=study-plan-v2&envId=top-sql-50

-- --- --- --- INSTRUCTIONS --- --- --- --
------------------------------------------

-- Find the names of the customer that are not referred by the customer with id = 2.
-- Return the result table in any order.
-- The result format is in the following example.

-- --- --- --- EXERCISE --- --- --- --
--------------------------------------

SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;