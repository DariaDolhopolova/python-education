-- first
SELECT first_name, last_name FROM users;

SELECT product_title, product_description FROM products;

SELECT * FROM order_status;

-- second
SELECT * FROM orders
WHERE order_status_order_status_id = 4;

--third
SELECT product_title, price FROM products
WHERE price > 80.0 AND price <= 150.0;

SELECT * FROM orders
WHERE created_at > '2020-10-01';

SELECT * FROM orders
WHERE created_at >= '2020-01-01' AND created_at <= '2020-06-01';

SELECT category_id, category_title FROM categories;

SELECT * FROM products
WHERE category_id = 7 OR category_id = 11 OR category_id = 18;

SELECT * FROM orders
WHERE order_status_order_status_id <> 4 AND updated_at <= '2020-12-31';

SELECT * FROM carts
LEFT JOIN orders ON orders.carts_carts_id = carts.cart_id
WHERE orders.carts_carts_id IS NULL;

-- fourth
SELECT COUNT(*) FROM orders
WHERE order_status_order_status_id = 4;

SELECT SUM(total)/357 FROM orders
WHERE order_status_order_status_id = 4;

SELECT MAX(total) FROM orders
WHERE created_at > '2020-07-01' AND created_at < '2020-09-30';
