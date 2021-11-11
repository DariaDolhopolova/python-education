CREATE TABLE customer_audits (
   id INT GENERATED ALWAYS AS IDENTITY,
   customer_id INT NOT NULL,
   last_name VARCHAR(40) NOT NULL,
   changed_on TIMESTAMP(6) NOT NULL
);

CREATE TABLE new_customers (
   id INT GENERATED ALWAYS AS IDENTITY,
   customer_id INT NOT NULL,
   first_name varchar(40) NOT NULL,
   last_name VARCHAR(40) NOT NULL,
   joined_on TIMESTAMP(6) NOT NULL
);

CREATE OR REPLACE FUNCTION check_if_new_customer()
    RETURNS TRIGGER
    language plpgsql
    AS
$$
BEGIN
    if NEW.last_name not in (SELECT last_name from customer)
        and NEW.first_name not in (SELECT first_name from customer) then
        insert into new_customers(customer_id,first_name, last_name, joined_on)
        values (NEW.customer_id, NEW.first_name, NEW.last_name, now());
    end if;

    return NEW;
end;$$;

CREATE TRIGGER new_customer_trigger
  AFTER UPDATE
  ON customer
  FOR EACH ROW
  EXECUTE PROCEDURE check_if_new_customer();

CREATE OR REPLACE FUNCTION log_last_name_changes()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
BEGIN
	IF NEW.last_name <> OLD.last_name THEN
		 INSERT INTO customer_audits(customer_id,last_name,changed_on)
		 VALUES(OLD.customer_id,OLD.last_name,now());
	END IF;

	RETURN NEW;
END;$$;

CREATE TRIGGER last_name_changes
  BEFORE UPDATE
  ON customer
  FOR EACH ROW
  EXECUTE PROCEDURE log_last_name_changes();

begin;
rollback;

INSERT INTO customer (first_name, last_name)
VALUES ('John', 'Doe');
