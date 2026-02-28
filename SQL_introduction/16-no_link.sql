-- In the previous exercises, we have seen how to use the GROUP BY clause to group rows based on a specific column. In this exercise, we will explore how to use the GROUP BY clause with multiple columns.

SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;
