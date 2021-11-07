-- task 1
CREATE TABLE potential_customers(
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    name VARCHAR(255),
    surname VARCHAR(255),
    second_name VARCHAR(255),
    city VARCHAR(255)
);

insert into potential_customers (email, name, surname, second_name, city)
select 'email' || i,'name' || i, 'surname' || i, 'second_name' || i,'city' || i
from generate_series(1, 1000) as i;

SELECT name, surname, email
FROM potential_customers
WHERE city = 'city17';
-- task 2
SELECT first_name, last_name, email
FROM users
ORDER BY city, first_name;
-- task 3
SELECT category_title, (SELECT COUNT(product_title)
FROM products WHERE products.category_id = categories.category_id) AS total_products
FROM categories;

-- task 4
-- 1

SELECT product_title, product_id
FROM products p
LEFT JOIN cart_product cp on p.product_id = cp.products_product_id
WHERE cp.products_product_id IS NULL;

-- 2

SELECT product_title, product_id
FROM products p
LEFT JOIN cart_product cp on p.product_id = cp.products_product_id
WHERE cp.products_product_id IS NULL
UNION
SELECT product_title, product_id
FROM products
WHERE product_id IN (
    SELECT products_product_id
    FROM cart_product
    LEFT JOIN orders on cart_product.carts_cart_id = orders.carts_carts_id
    WHERE orders.carts_carts_id IS NULL)
ORDER BY product_id;

-- 3

SELECT products_product_id, COUNT(products_product_id) AS Occurences
FROM cart_product
GROUP BY products_product_id
ORDER BY Occurences DESC
LIMIT 10;

-- 4

SELECT products_product_id, COUNT(products_product_id) AS Occurences
FROM cart_product
WHERE carts_cart_id IN(
    SELECT carts_cart_id FROM orders
    )
GROUP BY products_product_id
ORDER BY Occurences DESC
LIMIT 10;

-- 5
SELECT first_name, last_name, user_id
FROM users
WHERE user_id IN(
    SELECT users_user_id
    FROM carts
    GROUP BY users_user_id
    ORDER BY SUM(total) DESC
    )
LIMIT 5;

SELECT users_user_id, SUM(total)
FROM carts
GROUP BY users_user_id
ORDER BY SUM(total) DESC;

-- 6

SELECT first_name, last_name, user_id
FROM users
WHERE user_id IN (
    SELECT users_user_id
    FROM carts
    WHERE cart_id IN(
        SELECT carts_carts_id
        FROM orders o
        LEFT JOIN carts on o.carts_carts_id = carts.cart_id
    )
    GROUP BY users_user_id
    ORDER BY COUNT(cart_id) DESC
    )
LIMIT 5;

--7

SELECT first_name, last_name, user_id
FROM users
WHERE user_id IN(
    SELECT users_user_id
    FROM carts
    LEFT JOIN orders ON orders.carts_carts_id = carts.cart_id
    WHERE orders.carts_carts_id IS NULL
    GROUP BY users_user_id
    ORDER BY COUNT(cart_id) DESC
    )
LIMIT 5;





