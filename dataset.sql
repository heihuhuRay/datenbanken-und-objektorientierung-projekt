-- CREATE tables 
CREATE TABLE brand(
	phone_id INT PRIMARY KEY NOT NULL,
	brand text NOT NULL
);

CREATE TABLE version(
	phone_id INT PRIMARY KEY,
	version text NOT NULL,
	screen_size INT NOT NULL,
	cpu_model text NOT NULL,
	ram_model text NOT NULL
);

CREATE TABLE cpu(
	phone_id INT PRIMARY KEY,
	cpu_model char(50) NOT NULL,
	cpu_price INT NOT NULL
);

CREATE TABLE ram(
	phone_id INT PRIMARY KEY,
	ram_model text NOT NULL,
	storage text NOT NULL,
	ram_price INT NOT NULL
);

CREATE TABLE screen(
	phone_id INT PRIMARY KEY,
	screen_size text NOT NULL,
	screen_price INT NOT NULL
);



-- DROP all tables
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
COMMENT ON SCHEMA public IS 'standard public schema';



-- INSERT dataset
INSERT INTO brand (phone_id, brand) VALUES (1, 'Apple');
INSERT INTO brand (phone_id, brand) VALUES (2, 'Samsung');
INSERT INTO brand (phone_id, brand) VALUES (3, 'HTC');
INSERT INTO version (phone_id, version, screen_size, cpu_model, ram_model) VALUES (1, '3', 4.7, 'ARM', 'DDR3');
INSERT INTO version (phone_id, version, screen_size, cpu_model, ram_model) VALUES (2, 'S7', 5.5, 'Intel', 'DDR2');
INSERT INTO version (phone_id, version, screen_size, cpu_model, ram_model) VALUES (3, 'Butterfly', 6, 'Intel Core', 'DDR1');
INSERT INTO cpu (phone_id, cpu_model, cpu_price) VALUES (1, 'GX6450', 500);
INSERT INTO cpu (phone_id, cpu_model, cpu_price) VALUES (2, 'LG7745', 750);
INSERT INTO cpu (phone_id, cpu_model, cpu_price) VALUES (3, 'XR55662', 230);
INSERT INTO ram (phone_id, ram_model, storage, ram_price) VALUES (1, 'DDR3', '1G', 150);
INSERT INTO ram (phone_id, ram_model, storage, ram_price) VALUES (2, 'DDR2', '500MB', 120);
INSERT INTO ram (phone_id, ram_model, storage, ram_price) VALUES (3, 'DDR1', '2G', 80);
INSERT INTO screen (phone_id, screen_size, screen_price) VALUES (1, 4.7, 120);
INSERT INTO screen (phone_id, screen_size, screen_price) VALUES (2, 5.5, 85);
INSERT INTO screen (phone_id, screen_size, screen_price) VALUES (3, 6, 65);

-- SELECT 
SELECT * FROM brand, version, cpu, ram, screen;


