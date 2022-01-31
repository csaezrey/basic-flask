CREATE SCHEMA IF NOT EXISTS cpex;

CREATE TABLE cpex.Wallet(
    id SERIAL PRIMARY KEY,
    owner_id INTEGER,
    amount NUMERIC(20,4)
)


