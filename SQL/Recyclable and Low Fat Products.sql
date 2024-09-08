-- Link to the exercise : https://leetcode.com/problems/recyclable-and-low-fat-products/description/?envType=study-plan-v2&envId=top-sql-50

-- --- --- --- INSTRUCTIONS --- --- --- --
------------------------------------------

-- Write a solution to find the ids of products that are both low fat and recyclable.
-- Return the result table in any order.
-- The result format is in the following example.

-- --- --- --- EXERCISE --- --- --- --
--------------------------------------

SELECT product_id
FROM Products 
WHERE low_fats = 'Y' AND recyclable = 'Y';