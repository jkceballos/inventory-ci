CREATE TABLE IF NOT EXISTS inventory (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  quantity INTEGER NOT NULL
);

INSERT INTO inventory (name, quantity)
VALUES ('Laptop', 10),
       ('Mouse', 50),
       ('Teclado', 30);
