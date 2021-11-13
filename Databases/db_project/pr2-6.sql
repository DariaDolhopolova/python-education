-- views
--products table

SELECT * FROM products;

CREATE VIEW product_price_more_100 AS
    SELECT product_title, price
    FROM products
    WHERE price > 100;

SELECT * FROM product_price_more_100;

DROP VIEW product_price_more_100;

-- orders and order_status table
SELECT * FROM orders;

CREATE VIEW order_with_status AS
    SELECT orders.created_at AS order_date,
           orders.order_id AS order_id,
           os.status_name AS order_status,
           orders.total AS total
    FROM orders
    INNER JOIN order_status os on orders.order_status_order_status_id = os.order_status_id;

SELECT * FROM order_with_status;

DROP VIEW order_with_status;
-- products and categories

SELECT * FROM products;

CREATE VIEW products_with_categories AS
    SELECT products.product_title AS Title,
           products.product_description AS Description,
           c.category_title AS Category_Title,
           c.category_description AS Category_Description
    FROM products
    INNER JOIN categories c on products.category_id = c.category_id;

SELECT * FROM products_with_categories;

DROP VIEW products_with_categories;
-- materialized view

CREATE MATERIALIZED VIEW user_order_status_total AS
    SELECT users.first_name as name,
           users.last_name as last_name,
           c.order_id as order_id,
           c.status_name as status,
           c.total as total
    FROM users
    INNER JOIN (
        SELECT users_user_id,
               o.order_id,
               o.total,
               o.status_name
        FROM carts
        INNER JOIN (
            SELECT orders.order_id,
                   orders.carts_carts_id,
                   os.status_name,
                   orders.total
            FROM orders
            INNER JOIN order_status os on orders.order_status_order_status_id = os.order_status_id
            ) o on carts.cart_id = o.carts_carts_id
        ) c
        on users.user_id = c.users_user_id;

SELECT * FROM user_order_status_total;

DROP MATERIALIZED VIEW user_order_status_total;
