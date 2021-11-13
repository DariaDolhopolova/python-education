select * from orders;

select c.first_name, c.last_name, car.car_name, price, days_of_renting
from orders
left join car on car.car_id = orders.car_id
left join customer c on orders.customer_id = c.customer_id
where price > money(100)
order by price;

explain analyse select c.first_name, c.last_name, car.car_name, price, days_of_renting
from orders
left join car on car.car_id = orders.car_id
left join customer c on orders.customer_id = c.customer_id
where price > money(100)
order by price;

-- indexes which are used and improving cost/time
create index customer_idx on customer(customer_id,first_name, last_name);
create index car_idx on car(car_id, car_name);
drop index customer_idx;
drop index car_idx;
--select 2

select first_name, last_name, a.address, o.order_id
from customer
inner join addresses a on customer.address_id = a.address_id
left join orders o on customer.customer_id = o.customer_id
where customer.customer_id < 450 and o.order_id is not null;

explain analyse select first_name, last_name, a.address, o.order_id
from customer
inner join addresses a on customer.address_id = a.address_id
left join orders o on customer.customer_id = o.customer_id
where customer.customer_id < 450 and o.order_id is not null;

-- create index orders_idx on orders(order_id);
-- drop index  orders_idx;

--select 3

select * from addresses;

explain analyse select *
from customer
where customer.first_name like '%5' and last_name like '%5' and customer_id in (select customer_id from orders);

create index orders_idx on orders(customer_id);
drop index customer_idx;