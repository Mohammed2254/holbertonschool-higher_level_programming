-- Write a SQL query to find the name and score of all students with a score higher than or equal to 10 in the second_table, ordered by score from highest to lowest.

SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
