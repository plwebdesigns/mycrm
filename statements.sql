CREATE TABLE clients (
  id serial PRIMARY KEY,
  first_name varchar(80) NOT NULL,
  last_name varchar(80) NOT NULL,
  address_1 varchar(150),
  address_2 varchar(150),
  city varchar (80),
  state varchar (80),
  zipcode varchar (10),
  phone_1 varchar (12),
  phone_2 varchar (12),
  phone_3 varchar (12),
  phone_4 varchar (12),
  dob date,
  ssn varchar (12)
  );

CREATE TABLE employees (
  id serial PRIMARY KEY,
  first_name varchar(80) NOT NULL,
  last_name varchar(80) NOT NULL,
  address_1 varchar(150),
  address_2 varchar(150),
  city varchar (80),
  state varchar (80),
  zipcode varchar (10),
  phone_1 varchar (12),
  phone_2 varchar (12),
  dob date,
  ssn varchar (12),
  department varchar (30),
  manager varchar (30),
  salary money);


CREATE TABLE deals (
id serial PRIMARY KEY,
client_id integer REFERENCES clients(id),
employee_id integer REFERENCES employees(id),
amount money NOT NULL ,
payments_purchased integer NOT NULL
);