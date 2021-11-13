CREATE TABLE IF NOT EXISTS Users(
    user_id INT PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    middle_name VARCHAR(255),
    is_staff smallint,
    country VARCHAR(255),
    city VARCHAR(255),
    address TEXT
);

CREATE TABLE IF NOT EXISTS Carts(
    cart_id INT PRIMARY KEY,
    Users_user_id INT ,
    subtotal DECIMAL,
    total DECIMAL,
    timestamp TIMESTAMP(2),
    FOREIGN KEY (Users_user_id) REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS Orders(
    order_id INT PRIMARY KEY,
    Carts_carts_id INT,
    order_status_order_status_id INT,
    shipping_total DECIMAL,
    total DECIMAL,
    created_at TIMESTAMP(2),
    updated_at TIMESTAMP(2),
    FOREIGN KEY (Carts_carts_id) REFERENCES Carts(cart_id),
    FOREIGN KEY (order_status_order_status_id) REFERENCES Order_status(order_status_id)
);

CREATE TABLE IF NOT EXISTS Order_status(
    order_status_id INT PRIMARY KEY,
    status_name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Cart_product(
    carts_cart_id INT,
    products_product_id INT,
    FOREIGN KEY (carts_cart_id) REFERENCES Carts(cart_id),
    FOREIGN KEY (products_product_id) REFERENCES Products(product_id)
);

CREATE TABLE IF NOT EXISTS Products(
    product_id INT PRIMARY KEY,
    product_title VARCHAR(255),
    product_description TEXT,
    in_stock INT,
    price FLOAT,
    slug VARCHAR(45),
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

CREATE TABLE IF NOT EXISTS Categories(
    category_id INT PRIMARY KEY,
    category_title VARCHAR(255),
    category_description TEXT
);

-- COPY Users(user_id, email, password, first_name, last_name, middle_name, is_staff, country, city, address)
-- FROM 'users.csv'
-- DELIMITER ','
-- CSV;

--SELECT * FROM categories;

ALTER TABLE users ADD phone_number INT;

ALTER TABLE users
ALTER COLUMN phone_number TYPE VARCHAR;

UPDATE products
SET price = price * 2;
