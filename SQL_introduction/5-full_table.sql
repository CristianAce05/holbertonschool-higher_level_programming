-- Print the description of first_table without using DESCRIBE or EXPLAIN
SELECT column_name AS Field, column_type AS Type, is_nullable AS Null, column_key AS Key
FROM information_schema.columns
WHERE table_schema = DATABASE() AND table_name = 'first_table';
