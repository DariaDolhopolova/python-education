CREATE INDEX idx_full_name ON users(first_name, last_name);
DROP INDEX idx_full_name;

SET enable_seqscan TO off;
-- actually execution time is improved almost 4 times using index,
-- but it chooses to use it only if seqscan is manually turned off...
EXPLAIN ANALYSE SELECT *
FROM users
WHERE first_name LIKE '%2' OR last_name LIKE '%12';

SET enable_seqscan TO on;


-- 2
SELECT * FROM orders;

CREATE INDEX idx_created_at ON orders(created_at);
DROP INDEX idx_created_at;

EXPLAIN ANALYSE SELECT total, created_at
FROM orders
WHERE created_at > '2020-01-01';
-- ~0.100-0.150 ms better than without index, it chooses this way automatically

--3
SELECT * FROM products;

CREATE INDEX idx_product_description ON products(product_description);

EXPLAIN ANALYSE SELECT product_title, product_description
FROM products
WHERE product_description = 'Product description 556';


