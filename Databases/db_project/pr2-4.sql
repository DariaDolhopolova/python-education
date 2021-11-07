BEGIN;
ROLLBACK;
COMMIT;

SELECT * FROM potential_customers;
-- 1
BEGIN;
INSERT INTO potential_customers(email, name, surname, second_name, city)
VALUES ('my_email', 'my_name', 'my_surname','my_second_name', 'my_city');
ROLLBACK;
COMMIT;


BEGIN;
UPDATE potential_customers
    SET email = 'not my_email'
WHERE name = 'my_name';

SAVEPOINT not_email;

DELETE FROM potential_customers
WHERE email = 'not my_email';

ROLLBACK TO not_email;

SELECT email
FROM potential_customers
WHERE name = 'my_name';

RELEASE not_email;

--2
BEGIN;
INSERT INTO orders(order_id, order_status_order_status_id, total)
VALUES (11312, 2, 56.18);

SAVEPOINT add_order;

DELETE FROM orders
WHERE order_id = 11312;

SAVEPOINT delete_order;

UPDATE orders
    SET total = 1100.01
WHERE order_id = 1;

SAVEPOINT update_order;

DELETE FROM orders
WHERE total = 1100.01;

ROLLBACK TO update_order;
ROLLBACK TO delete_order;
ROLLBACK TO add_order;
ROLLBACK;

--3
SELECT * FROM carts;

BEGIN;

UPDATE carts
    SET total = total + 100
WHERE users_user_id > 100;

SAVEPOINT update_total;

INSERT INTO carts (cart_id, total)
VALUES (566587, 150.20),
       (2225446, 189.90),
       (7964853, 999.99);
SAVEPOINT insert_no_user;

DELETE FROM carts
WHERE users_user_id IS NULL;

ROLLBACK TO insert_no_user;
ROLLBACK TO update_total;
ROLLBACK;






