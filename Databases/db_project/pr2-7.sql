CREATE TEMPORARY TABLE all_orders_table(
            user_id int,
            order_id int,
            shipping_total float,
            city varchar);
BEGIN;
ROLLBACK;

create function set_shipping_total(my_city varchar)
returns all_orders_table
language plpgsql as $$
    DECLARE aot all_orders_table;
    BEGIN

        SELECT c.users_user_id,
               orders.order_id,
               orders.shipping_total,
               c.city
        INTO aot
        FROM orders
        INNER JOIN (
            SELECT carts.users_user_id,
                   carts.cart_id,
                   u.city
            FROM carts
            INNER JOIN users u on carts.users_user_id = u.user_id
            ) c on c.cart_id = orders.carts_carts_id
        WHERE c.city = my_city;

        if not found then
            raise 'Users inside % not found', my_city;
        else
            update orders
                set shipping_total = 0
            where orders.order_id = aot.order_id;
            return aot;
        end if;
    end;
$$;

select set_shipping_total('city 14');

DROP FUNCTION set_shipping_total(my_city varchar);

select * from orders;
-- stored procedures
begin;
rollback;

create or replace procedure clear_cart(user_id int, cart_id int)
language plpgsql
as $$
declare
    new_total float;
begin
    update carts
    set subtotal = 0,
        total = 0
    where users_user_id = user_id
    returning total
    into new_total;

    update cart_product
    set products_product_id = Null
    where carts_cart_id = cart_id;

end;$$;

call clear_cart(12, 12);

create procedure add_bonus(my_order_id int)
language plpgsql
as $$
    declare
        new_total float;
        my_cart_id int;
    begin
        select total
        from orders
        where order_id = my_order_id
        into new_total;

        my_cart_id = (select carts_carts_id from orders where order_id = my_order_id);

        if new_total >= 500 then
        insert into cart_product(carts_cart_id, products_product_id)
        values (my_cart_id, 1);
        end if;
    end;$$;

call add_bonus(25);

drop procedure add_bonus(my_order_id int);
drop procedure clear_cart(user_id int, cart_id int);