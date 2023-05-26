CREATE TABLE People (
    id INT PRIMARY KEY NOT NULL,
    name TEXT,
    date_of_birth TEXT,
    phone_number TEXT
);

INSERT INTO People (id, name, date_of_birth, phone_number) VALUES
    (0, "Thomas Powell", "1990-05-13", "044465456410"),
    (1, "Bob Jones", "2003-02-34", "01541255");