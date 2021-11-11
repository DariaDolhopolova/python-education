CREATE TABLE IF NOT EXISTS addresses(
    address_id SERIAL PRIMARY KEY,
    address varchar(255)
);

CREATE TABLE IF NOT EXISTS phone_numbers(
    phone_id SERIAL PRIMARY KEY,
    phone_number bigint
);

CREATE TABLE IF NOT EXISTS branch(
    branch_id SERIAL PRIMARY KEY,
    branch_name varchar(255),
    phone_id int,
    address_id int,
    FOREIGN KEY (phone_id) REFERENCES phone_numbers(phone_id),
    FOREIGN KEY (address_id) REFERENCES addresses(address_id)
);

CREATE TABLE IF NOT EXISTS car(
    car_id SERIAL PRIMARY KEY,
    car_name varchar(255),
    branch_id int,
    FOREIGN KEY (branch_id) REFERENCES branch(branch_id)
);


CREATE TABLE IF NOT EXISTS customer(
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone_id INT,
    address_id INT,
    car_id INT,
    FOREIGN KEY (phone_id) REFERENCES phone_numbers(phone_id),
    FOREIGN KEY (address_id) REFERENCES addresses(address_id),
    FOREIGN KEY (car_id) REFERENCES car(car_id)
);

CREATE TABLE IF NOT EXISTS orders(
    order_id SERIAL PRIMARY KEY,
    price money,
    period_of_renting text,
    days_of_renting smallint,
    branch_id int,
    customer_id INT,
    car_id INT,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (branch_id) REFERENCES branch(branch_id),
    FOREIGN KEY (car_id) REFERENCES car(car_id)
);

insert into addresses(address)
select 'my long address ' || i
from generate_series(1, 1500) as i;

insert into phone_numbers(phone_number)
select 38066593 + i
from generate_series(1, 1500) as i;

insert into branch(branch_name)
select 'my branch name' || i
from generate_series(1, 500) as i;

update branch
set address_id = a.address_id
from addresses a
where a.address_id = branch.branch_id;

update branch
set phone_id = pn.phone_id
from phone_numbers pn
where pn.phone_id = branch.branch_id;


insert into car(car_name)
select 'car model' || i
from generate_series(1, 1000) as i;

update car
set branch_id = b.branch_id
from branch b
where b.branch_id + 500 = car.car_id;

insert into customer (first_name, last_name)
select 'first name' || i,'last name' || i
from generate_series(1, 1000) as i;

update customer
set phone_id = 500 + p.phone_id
from phone_numbers p
where p.phone_id = customer.customer_id;

update customer
set address_id = 500 + a.address_id
from addresses a
where a.address_id = customer.customer_id;

update customer
set car_id = c.car_id
from car c
where c.car_id = customer.customer_id;


select * from orders;

insert into orders(price, period_of_renting, days_of_renting)
select 45.89 + i, '2021-01-1 - 2021-01-' || i, i
from generate_series(1, 30) as i;

insert into orders(price, period_of_renting, days_of_renting)
select 55.54 + i, '2021-02-1 - 2021-02-' || i, i
from generate_series(1, 30) as i;

insert into orders(price, period_of_renting, days_of_renting)
select 80.53 + i, '2021-03-1 - 2021-03-' || i, i
from generate_series(1, 30) as i;

insert into orders(price, period_of_renting, days_of_renting)
select 92.45 + i, '2021-04-1 - 2021-04-' || i, i
from generate_series(1, 30) as i;

insert into orders(price, period_of_renting, days_of_renting)
select 59.20 + i, '2021-05-1 - 2021-05-' || i, i
from generate_series(1, 30) as i;

insert into orders(price, period_of_renting, days_of_renting)
select 250.89 + i, '2021-06-1 - 2021-06-' || i, i
from generate_series(1, 30) as i;

insert into orders(price, period_of_renting, days_of_renting)
select 184.90 + i, '2021-07-1 - 2021-07-' || i, i
from generate_series(1, 30) as i;

insert into orders(price, period_of_renting, days_of_renting)
select 67.80 + i, '2021-08-1 - 2021-08-' || i, i
from generate_series(1, 30) as i;

insert into orders(price, period_of_renting, days_of_renting)
select 79.35 + i, '2021-09-1 - 2021-09-' || i, i
from generate_series(1, 30) as i;

insert into orders(price, period_of_renting, days_of_renting)
select 310.58 + i, '2021-10-1 - 2021-10-' || i, i
from generate_series(1, 30) as i;

insert into orders(price, period_of_renting, days_of_renting)
select 418.60 + i, '2021-11-1 - 2021-11-' || i, i
from generate_series(1, 30) as i;

insert into orders(price, period_of_renting, days_of_renting)
select 44.70 + i, '2021-12-1 - 2021-12-' || i, i
from generate_series(1, 30) as i;

update orders
set car_id = c.car_id
from car c
where c.car_id = orders.order_id;

update orders
set branch_id = b.branch_id
from branch b
where b.branch_id = orders.order_id;

update orders
set customer_id = c.customer_id
from customer c
where c.customer_id = orders.order_id;

select * from orders;