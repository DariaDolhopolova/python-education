create or replace function get_branch_number_address(my_branch_id int)
    returns text as $$
DECLARE
    address_and_phone text default '';
    rec_addr_phone record;
    cur_addr_phone cursor(branch_id int)
        for select pn.phone_number, a.address
        from branch
        left join addresses a on branch.address_id = a.address_id
        left join phone_numbers pn on branch.phone_id = pn.phone_id
        where branch.branch_id = my_branch_id;
begin
    open cur_addr_phone(my_branch_id);
    address_and_phone := 'Address and phone af your chosen branch: ';

    loop
        fetch cur_addr_phone into rec_addr_phone;
        exit when not found;

        if rec_addr_phone.address like '%long%' then
            address_and_phone := address_and_phone || rec_addr_phone.address || ', ' || rec_addr_phone.phone_number;
        end if;
    end loop;
    close cur_addr_phone;
    return address_and_phone;
end;$$
language plpgsql;

select get_branch_number_address(15);
drop function get_branch_number_address(my_branch_id int);


create or replace function get_car (name_pattern varchar, my_branch_id int)
returns table(p_car_name varchar, p_branch_id int)
language plpgsql
as $$
    DECLARE
        var_r record;
    begin
        for var_r in (
            select car_name, branch_id
            from car
            where car_name ilike name_pattern and
                  branch_id = my_branch_id
            ) loop p_car_name := upper(var_r.car_name);
                p_branch_id := var_r.branch_id;
                return next;
            end loop;
    end;$$;

drop function get_car(name_pattern varchar, my_branch_id int);
select get_car('%mod%', 24);