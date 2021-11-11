create or replace procedure insert_customer(fname varchar, lname varchar)
language plpgsql
as $$
begin
    insert into customer(first_name, last_name)
    values (fname, lname);
end;$$;

begin;
call insert_customer('John', 'Marrow')
rollback;
drop procedure insert_customer(fname varchar, lname varchar);

create or replace procedure delete_car(name varchar)
language plpgsql
as $$
begin

    delete from orders
    where car_id = (select car_id from car where car_name = name);

    delete from customer
    where car_id = (select car_id from car where car_name = name);

    delete from car
    where car_name = name;
end;$$;

begin;
call delete_car('car model540');
rollback;
drop procedure delete_car(name varchar);
select * from car;

