-- DROP all tables
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
COMMENT ON SCHEMA public IS 'standard public schema';

-- CREATE tables 
CREATE TABLE brand(
	brand_id INT NOT NULL,
	brand_name text NOT NULL,
	PRIMARY KEY (brand_id)
);

CREATE TABLE cpu(
	cpu_id INT NOT NULL,
	cpu_model text NOT NULL,
	cpu_price numeric NOT NULL,
	cpu_year INT NOT NULL,
	PRIMARY KEY (cpu_id)
);

CREATE TABLE screen(
	scr_id INT NOT NULL,
	scr_size numeric NOT NULL,
	scr_price numeric NOT NULL,
	scr_hardness numeric NOT NULL,
	PRIMARY KEY (scr_id)
);

CREATE TABLE product(
	prod_id INT NOT NULL,
	prod_name text NOT NULL,
	cpu_model text NOT NULL,
	cpu_id INT NOT NULL,
	scr_size numeric NOT NULL,
	scr_id INT NOT NULL,
	prod_price numeric NOT NULL,
	brand_id INT NOT NULL,
	PRIMARY KEY (prod_id),
	FOREIGN KEY (cpu_id) REFERENCES cpu (cpu_id) ON DELETE CASCADE,
	FOREIGN KEY (scr_id) REFERENCES screen (scr_id) ON DELETE CASCADE,
	FOREIGN KEY (brand_id) REFERENCES brand (brand_id) ON DELETE CASCADE
);

CREATE TABLE service(
	ser_id INT NOT NULL,
	ser_name text NOT NULL,
	brand_id INT NOT NULL,
	PRIMARY KEY (ser_id),
	FOREIGN KEY (brand_id) REFERENCES brand (brand_id) ON DELETE CASCADE	
);

CREATE TABLE retailer(
	ret_id INT NOT NULL,
	ret_name text NOT NULL,
	PRIMARY KEY (ret_id)
);

CREATE TABLE order_items(
	o_id serial NOT NULL,
	o_num bigserial NOT NULL,
	prod_id INT NOT NULL,
	ser_id INT,
	ret_id INT NOT NULL,
	PRIMARY KEY (o_id),
	FOREIGN KEY (prod_id) REFERENCES product (prod_id) ON DELETE CASCADE,
	FOREIGN KEY (ser_id) REFERENCES service (ser_id) ON DELETE CASCADE,
	FOREIGN KEY (ret_id) REFERENCES retailer (ret_id) ON DELETE CASCADE	
);

-- INSERT dataset
--brand
INSERT INTO brand (brand_id, brand_name) VALUES (1, 'Apple');
INSERT INTO brand (brand_id, brand_name) VALUES (2, 'Samsung');
--cpu
INSERT INTO cpu (cpu_id, cpu_model, cpu_price, cpu_year) VALUES (1, 'A5', 100, 2011);
INSERT INTO cpu (cpu_id, cpu_model, cpu_price, cpu_year) VALUES (2, 'A7', 150, 2013);
INSERT INTO cpu (cpu_id, cpu_model, cpu_price, cpu_year) VALUES (3, 'A9', 129, 2016);
INSERT INTO cpu (cpu_id, cpu_model, cpu_price, cpu_year) VALUES (4, 'G535', 139, 2012);
INSERT INTO cpu (cpu_id, cpu_model, cpu_price, cpu_year) VALUES (5, 'G800', 160, 2014);
INSERT INTO cpu (cpu_id, cpu_model, cpu_price, cpu_year) VALUES (6, 'G820', 180, 2016);
--screen
INSERT INTO screen (scr_id, scr_size, scr_price, scr_hardness) VALUES (1, 4, 20, 0.9);
INSERT INTO screen (scr_id, scr_size, scr_price, scr_hardness) VALUES (2, 4.7, 20, 0.9);
INSERT INTO screen (scr_id, scr_size, scr_price, scr_hardness) VALUES (3, 5.5, 25, 0.85);
--product
INSERT INTO product (prod_id, prod_name, cpu_model, cpu_id, scr_size, scr_id, prod_price, brand_id) VALUES (1, 'iPhone5 ', 'A5', 1, 4,   1, 499, 1);
INSERT INTO product (prod_id, prod_name, cpu_model, cpu_id, scr_size, scr_id, prod_price, brand_id) VALUES (2, 'iPhone5c', 'A5', 1, 4,   1, 549, 1);
INSERT INTO product (prod_id, prod_name, cpu_model, cpu_id, scr_size, scr_id, prod_price, brand_id) VALUES (3, 'iPhone5s', 'A5', 1, 4,   1, 599, 1);
INSERT INTO product (prod_id, prod_name, cpu_model, cpu_id, scr_size, scr_id, prod_price, brand_id) VALUES (4, 'iPhone6 ', 'A7',	2, 4.7, 2, 599, 1);
INSERT INTO product (prod_id, prod_name, cpu_model, cpu_id, scr_size, scr_id, prod_price, brand_id) VALUES (5, 'iPhone6s', 'A9',	3, 4.7, 2, 549, 1);
INSERT INTO product (prod_id, prod_name, cpu_model, cpu_id, scr_size, scr_id, prod_price, brand_id) VALUES (6, 'Samsung Note3', 'G535', 4, 5.5, 3, 639, 2);
INSERT INTO product (prod_id, prod_name, cpu_model, cpu_id, scr_size, scr_id, prod_price, brand_id) VALUES (7, 'Samsung Note4', 'G535', 4, 5.5, 3, 699, 2);
INSERT INTO product (prod_id, prod_name, cpu_model, cpu_id, scr_size, scr_id, prod_price, brand_id) VALUES (8, 'Samsung S7',    'G800', 5, 5.5, 3, 799, 2);
INSERT INTO product (prod_id, prod_name, cpu_model, cpu_id, scr_size, scr_id, prod_price, brand_id) VALUES (9, 'Samsung Note7', 'G820', 5, 5.5, 3, 899, 2);
--service
INSERT INTO service (ser_id, ser_name, brand_id) VALUES (1, 'Apple Music', 1);
INSERT INTO service (ser_id, ser_name, brand_id) VALUES (2, 'iCloud', 2);
INSERT INTO service (ser_id, ser_name, brand_id) VALUES (3, 'Samsung Cloud', 2);
INSERT INTO service (ser_id, ser_name, brand_id) VALUES (4, 'Samsung Music', 2);
--retailer
INSERT INTO retailer (ret_id, ret_name) VALUES (1, 'Ebay');
INSERT INTO retailer (ret_id, ret_name) VALUES (2, 'Amazon');
--order_items
INSERT INTO order_items (o_num, prod_id, ser_id, ret_id) VALUES (300947, 1, 1, 1);
INSERT INTO order_items (o_num, prod_id, ser_id, ret_id) VALUES (427791, 5, 3, 1);
INSERT INTO order_items (o_num, prod_id, ser_id, ret_id) VALUES (510010, 4, 1, 2);
INSERT INTO order_items (o_num, prod_id, ser_id, ret_id) VALUES (894020, 8, 4, 2);



