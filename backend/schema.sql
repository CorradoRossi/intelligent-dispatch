-- Database schema for Intelligent Scheduling and Dispatch MVP

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT
);

CREATE TABLE technicians (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    skills TEXT[]
);

CREATE TABLE service_requests (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    service_type VARCHAR(50) NOT NULL,
    description TEXT,
    requested_date DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'pending'
);

CREATE TABLE technician_availability (
    id SERIAL PRIMARY KEY,
    technician_id INTEGER REFERENCES technicians(id),
    date DATE NOT NULL,
    is_available BOOLEAN DEFAULT true
);

CREATE TABLE assignments (
    id SERIAL PRIMARY KEY,
    service_request_id INTEGER REFERENCES service_requests(id),
    technician_id INTEGER REFERENCES technicians(id),
    assigned_date DATE NOT NULL
);