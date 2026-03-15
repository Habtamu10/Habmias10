# SQL Cheat Sheet

## Basic Queries
```sql
SELECT * FROM users;
SELECT name, email FROM users WHERE active = 1;
SELECT * FROM orders ORDER BY created_at DESC LIMIT 10;
```

## Filtering
```sql
WHERE age > 18 AND city = 'Addis Ababa'
WHERE name LIKE '%Habtamu%'
WHERE id IN (1, 2, 3)
WHERE salary BETWEEN 1000 AND 5000
```

## Joins
```sql
SELECT u.name, o.total FROM users u
JOIN orders o ON u.id = o.user_id;
```

## Aggregation
```sql
SELECT department, COUNT(*) as count, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

## Data Modification
```sql
INSERT INTO users (name, email) VALUES ('Habtamu', 'h@example.com');
UPDATE users SET email = 'new@example.com' WHERE id = 1;
DELETE FROM users WHERE id = 1;
```
