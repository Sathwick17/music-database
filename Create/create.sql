BEGIN;


-- Artist Table
CREATE TABLE artist (
    artist_id CHARACTER VARYING(30) PRIMARY KEY,
    name CHARACTER VARYING(150)
);

-- Album Table
CREATE TABLE album (
    album_id CHARACTER VARYING(30) PRIMARY KEY,
    title CHARACTER VARYING(150),
    artist_id CHARACTER VARYING(30),
    FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
);

-- Genre Table
CREATE TABLE genre (
    genre_id CHARACTER VARYING(30) PRIMARY KEY,
    name CHARACTER VARYING(50)
);

-- Media Type Table
CREATE TABLE media_type (
    media_type_id CHARACTER VARYING(30) PRIMARY KEY,
    name CHARACTER VARYING(30)
);

-- Media Type Pricing Table (BCNF decomposition)
CREATE TABLE media_type_pricing (
    media_type_id CHARACTER VARYING(30),
    unit_price NUMERIC,
    PRIMARY KEY (media_type_id, unit_price),
    FOREIGN KEY (media_type_id) REFERENCES media_type(media_type_id)
);

-- Track Table
CREATE TABLE track (
    track_id CHARACTER VARYING(30) PRIMARY KEY,
    name CHARACTER VARYING(250),
    album_id CHARACTER VARYING(30),
    media_type_id CHARACTER VARYING(30),
    genre_id CHARACTER VARYING(30),
    composer CHARACTER VARYING(250),
    milliseconds BIGINT,
    bytes INTEGER,
    FOREIGN KEY (album_id) REFERENCES album(album_id),
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id),
    FOREIGN KEY (media_type_id) REFERENCES media_type(media_type_id)
);

-- Track Price Table (BCNF decomposition)
CREATE TABLE track_price (
    track_id CHARACTER VARYING(30) PRIMARY KEY,
    unit_price NUMERIC,
    FOREIGN KEY (track_id) REFERENCES track(track_id)
);

-- Playlist Table
CREATE TABLE playlist (
    playlist_id CHARACTER VARYING(30) PRIMARY KEY,
    name CHARACTER VARYING(50)
);

-- Playlist Track Table (Many-to-Many Relation)
CREATE TABLE playlist_track (
    playlist_id CHARACTER VARYING(30),
    track_id CHARACTER VARYING(30),
    PRIMARY KEY (playlist_id, track_id),
    FOREIGN KEY (playlist_id) REFERENCES playlist(playlist_id),
    FOREIGN KEY (track_id) REFERENCES track(track_id)
);

-- Employee Table
CREATE TABLE employee (
    employee_id CHARACTER VARYING(30) PRIMARY KEY,
    last_name CHARACTER(50),
    first_name CHARACTER(50),
    title CHARACTER VARYING(250),
    reports_to CHARACTER VARYING(30),
    levels CHARACTER VARYING(10),
    birth_date TIMESTAMP,
    hire_date TIMESTAMP,
    address CHARACTER VARYING(120),
    postal_code CHARACTER VARYING(30),
    phone CHARACTER VARYING(30),
    fax CHARACTER VARYING(30),
    email CHARACTER VARYING(30),
    FOREIGN KEY (reports_to) REFERENCES employee(employee_id)
);

-- Location Table (for Employee Postal Code)
CREATE TABLE location (
    postal_code CHARACTER VARYING(30) PRIMARY KEY,
    city CHARACTER VARYING(50),
    state CHARACTER VARYING(30),
    country CHARACTER VARYING(30)
);

ALTER TABLE employee
    ADD CONSTRAINT fk_employee_location FOREIGN KEY (postal_code) REFERENCES location(postal_code);

-- Customer Table
CREATE TABLE customer (
    customer_id CHARACTER VARYING(30) PRIMARY KEY,
    first_name CHARACTER(30),
    last_name CHARACTER(30),
    company CHARACTER VARYING(150),
    address CHARACTER VARYING(250),
    postal_code CHARACTER VARYING(30),
    phone CHARACTER VARYING(30),
    fax CHARACTER VARYING(30),
    email CHARACTER VARYING(30),
    support_rep_id CHARACTER VARYING(30),
    FOREIGN KEY (support_rep_id) REFERENCES employee(employee_id)
);

ALTER TABLE customer
    ADD CONSTRAINT fk_customer_location FOREIGN KEY (postal_code) REFERENCES location(postal_code);

-- Customer Billing Table (BCNF decomposition)
CREATE TABLE customer_billing (
    customer_id CHARACTER VARYING(30) PRIMARY KEY,
    billing_address CHARACTER VARYING(120),
    billing_city CHARACTER VARYING(30),
    billing_state CHARACTER VARYING(30),
    billing_country CHARACTER VARYING(30),
    billing_postal CHARACTER VARYING(30),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

-- Invoice Table
CREATE TABLE invoice (
    invoice_id CHARACTER VARYING(30) PRIMARY KEY,
    customer_id CHARACTER VARYING(30),
    invoice_date TIMESTAMP,
    total DOUBLE PRECISION,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

-- Invoice Line Table
CREATE TABLE invoice_line (
    invoice_line_id CHARACTER VARYING(30) PRIMARY KEY,
    invoice_id CHARACTER VARYING(30),
    track_id CHARACTER VARYING(30),
    quantity INTEGER,
    FOREIGN KEY (invoice_id) REFERENCES invoice(invoice_id),
    FOREIGN KEY (track_id) REFERENCES track(track_id)
);

COMMIT;
