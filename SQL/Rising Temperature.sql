-- Link to the exercise : https://leetcode.com/problems/rising-temperature/description/?envType=study-plan-v2&envId=top-sql-50
-- --- --- --- INSTRUCTIONS --- --- --- --
------------------------------------------

-- Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).
-- Return the result table in any order.
-- The result format is in the following example.

-- --- --- --- EXERCISE --- --- --- --
--------------------------------------

SELECT id
FROM Weather tab1
WHERE temperature > (
    SELECT temperature
    FROM Weather tab2
    WHERE tab2.recordDate = DATE_SUB(tab1.recordDate, INTERVAL 1 DAY)
);
