-- Total revenue
SELECT SUM(amount) AS total_revenue FROM sales;

-- Revenue by product
SELECT product, SUM(amount) AS revenue
FROM sales
GROUP BY product;

-- Top customers
SELECT customer_id, SUM(amount) AS total_spent
FROM sales
GROUP BY customer_id
ORDER BY total_spent DESC;