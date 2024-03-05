CREATE TABLE Book
(
  Book_id INT NOT NULL,
  Book_name VARCHAR(50) NOT NULL,
  Author VARCHAR(50) NOT NULL,
  Cur_status VARCHAR(50) NOT NULL,
  Pub_year INT NOT NULL,
  PRIMARY KEY (Book_id)
);

CREATE TABLE Library
(
  Library_id INT NOT NULL,
  Library_name VARCHAR(50) NOT NULL,
  City VARCHAR(50) NOT NULL,
  PRIMARY KEY (Library_id)
);

CREATE TABLE Date_table
(
  Year DATE NOT NULL,
  Month DATE NOT NULL,
  Day DATE NOT NULL
);

CREATE TABLE Customer
(
  Customer_id INT NOT NULL,
  Name VARCHAR(50) NOT NULL,
  Address VARCHAR(50) NOT NULL,
  PRIMARY KEY (Customer_id)
);

CREATE TABLE Loans
(
  Loan_id INT NOT NULL,
  Loan_start DATE NOT NULL,
  Loan_end DATE NOT NULL,
  Loan_limit DATE NOT NULL,
  Late_fee FLOAT NOT NULL,
  Customer_id INT NOT NULL,
  Library_id INT NOT NULL,
  Book_id INT NOT NULL,
  PRIMARY KEY (Loan_id),
  FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id),
  FOREIGN KEY (Library_id) REFERENCES Library(Library_id),
  FOREIGN KEY (Book_id) REFERENCES Book(Book_id)
);