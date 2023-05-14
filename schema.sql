DROP TABLE IF EXISTS books;

CREATE TABLE books (
    serial_number INTEGER PRIMARY KEY AUTOINCREMENT,
    date_of_publication date NOT NULL,
    title TEXT NOT NULL,
    publisher TEXT NOT NULL,
    pages TEXT NOT NULL,
    book_type TEXT NOT NULL
);