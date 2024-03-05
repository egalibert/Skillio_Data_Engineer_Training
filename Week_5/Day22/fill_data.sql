-- Insert data into Book table
INSERT INTO Book (Book_id, Book_name, Author, Cur_status, Pub_year)
VALUES
  (1, 'The Great Gatsby', 'F. Scott Fitzgerald', 'Available', 1925),
  (2, 'To Kill a Mockingbird', 'Harper Lee', 'Available', 1960),
  (3, '1984', 'George Orwell', 'Available', 1949),
  (4, 'Pride and Prejudice', 'Jane Austen', 'Available', 1813),
  (5, 'The Catcher in the Rye', 'J.D. Salinger', 'Available', 1951),
  (6, 'The Hobbit', 'J.R.R. Tolkien', 'Available', 1937),
  (7, 'Harry Potter and the Sorcerer''s Stone', 'J.K. Rowling', 'Available', 1997);

-- Insert data into Library table
INSERT INTO Library (Library_id, Library_name, City)
VALUES
  (1, 'Helsinki Library', 'Helsinki'),
  (2, 'Espoo Library', 'Espoo'),
  (3, 'Turun Kirjasto', 'Turku');

-- Insert data into Date_table for the entire year
INSERT INTO Date_table (Year, Month, Day)
SELECT
  '2024-01-01'::DATE + (n || ' days')::INTERVAL AS Year,
  '2024-01-01'::DATE + (n || ' days')::INTERVAL AS Month,
  '2024-01-01'::DATE + (n || ' days')::INTERVAL AS Day
FROM generate_series(0, 364) n;

-- Insert data into Customer table
INSERT INTO Customer (Customer_id, Name, Address)
VALUES
  (1, 'Aliisa Johansson', 'Kulmakatu 1, Vantaa'),
  (2, 'Paavo Nurmi', 'Sivukatu 3, Helsinki'),
  (3, 'Jaakko Ruskeasuo', 'Raidekuja 1, Helsinki'),
  (4, 'Tiina Mannikko', 'Päätie 2, Espoo');

-- Insert data into Loans table
INSERT INTO Loans (Loan_id, Loan_start, Loan_end, Loan_limit, Late_fee, Customer_id, Library_id, Book_id)
VALUES
  (1, '2024-02-01'::DATE, '2024-02-15'::DATE, '2024-02-15'::DATE, 5.00, 1, 1, 1),
  (2, '2024-02-10'::DATE, '2024-02-24'::DATE, '2024-02-24'::DATE, 0.00, 2, 2, 3),
  (3, '2024-02-20'::DATE, '2024-03-05'::DATE, '2024-03-05'::DATE, 0.00, 3, 3, 5),
  (4, '2024-03-01'::DATE, '2024-03-15'::DATE, '2024-03-15'::DATE, 0.00, 4, 1, 2),
  (5, '2024-03-10'::DATE, '2024-03-24'::DATE, '2024-03-24'::DATE, 8.00, 1, 3, 6),
  (6, '2024-03-15'::DATE, '2024-03-29'::DATE, '2024-03-29'::DATE, 0.00, 2, 1, 4);
