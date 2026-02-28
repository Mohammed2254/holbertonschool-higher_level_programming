-- In the previous exercises, we have seen how to use the GROUP BY clause to group rows based on a specific column. In this exercise, we will explore how to use the GROUP BY clause with multiple columns.

SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
