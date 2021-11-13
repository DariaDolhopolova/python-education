BEGIN;
SELECT product_id, product_title, category_id, price,
       avg(price) OVER (PARTITION BY category_id)
FROM products;
ROLLBACK;


BEGIN;
CREATE OR REPLACE FUNCTION cart_insert_trigger_func()
    RETURNS trigger
    LANGUAGE plpgsql
    AS
    $$
    DECLARE next_order_id int;
    BEGIN
        SELECT order_id FROM orders ORDER BY order_id DESC LIMIT 1
        INTO next_order_id;

        INSERT INTO orders(order_id, carts_carts_id, order_status_order_status_id, shipping_total, total, created_at, updated_at)
        VALUES (next_order_id + 1, NEW.cart_id, 1, NEW.total, NEW.total, current_date, current_date);
    RETURN NEW;

end;
$$;

CREATE TRIGGER cart_insert_trigger
  AFTER INSERT
  ON carts
  FOR EACH ROW
  EXECUTE PROCEDURE cart_insert_trigger_func();

--demo

begin;
rollback;
INSERT INTO carts(cart_id, users_user_id, subtotal, total, timestamp)
VALUES (22556, 15, 158.95, 158.95,current_date);
select * from orders
where carts_carts_id = 22556;

-- trigger 2
BEGIN;

CREATE OR REPLACE FUNCTION user_delete_trigger_func()
    RETURNS trigger
    LANGUAGE plpgsql
    AS
    $$
    BEGIN
        INSERT INTO potential_customers(email, name, surname, second_name, city)
        VALUES (NEW.email, NEW.first_name, NEW.last_name, NEW.middle_name, NEW.city);

    RETURN NEW;

end;
$$;

CREATE TRIGGER user_delete_trigger
  AFTER DELETE
  ON users
  FOR EACH ROW
 EXECUTE PROCEDURE user_delete_trigger_func();

-- block to delete all connections and foreign keys
DELETE FROM orders WHERE carts_carts_id = (SELECT cart_id from carts where users_user_id = 25);
DELETE FROM cart_product WHERE carts_cart_id = (SELECT cart_id from carts where users_user_id = 25);
DELETE FROM carts WHERE users_user_id = 25;
DELETE FROM users
WHERE user_id = 25;

ROLLBACK;


