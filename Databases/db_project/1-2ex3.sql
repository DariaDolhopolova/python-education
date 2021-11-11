
CREATE VIEW orders_more_100 AS
    SELECT order_id, price
    FROM orders
    WHERE price > money(100)
    order by price;

SELECT * FROM orders_more_100;

DROP VIEW orders_more_100;


SELECT * FROM orders;

CREATE VIEW order_with_cars AS
    SELECT orders.period_of_renting AS order_period,
           orders.order_id AS order_id,
           car.car_name AS car_name,
           orders.price AS price
    FROM orders
    INNER JOIN car on orders.car_id = car.car_id;

SELECT * FROM order_with_cars;

DROP VIEW order_with_cars;

CREATE MATERIALIZED VIEW user_order_car_total AS
    SELECT customer.first_name as name,
           customer.last_name as last_name,
           o.order_id as order_id,
           o.car_name as car_name,
           o.price as total
    FROM customer
    INNER JOIN (
        SELECT car_name,
               o.order_id,
               o.customer_id,
               o.price
        FROM car
        INNER JOIN orders o on car.car_id = o.car_id
        ) o
        on o.customer_id = customer.customer_id;

SELECT * FROM user_order_car_total;

DROP MATERIALIZED VIEW user_order_car_total;
