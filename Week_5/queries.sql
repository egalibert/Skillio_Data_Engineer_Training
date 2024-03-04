CREATE TABLE Product
(
  Product_id INT NOT NULL,
  Quantity_in_stock INT NOT NULL,
  Product_name VARCHAR(100) NOT NULL,
  Price FLOAT NOT NULL,
  PRIMARY KEY (Product_id)
);

CREATE TABLE Reviews
(
  Review_id INT NOT NULL,
  Rating FLOAT NOT NULL,
  Product_id INT NOT NULL,
  PRIMARY KEY (Review_id),
  FOREIGN KEY (Product_id) REFERENCES Product(Product_id)
);

CREATE TABLE Orders
(
  Order_id INT NOT NULL,
  Order_date DATE NOT NULL,
  Delivered  BOOLEAN NOT NULL,
  Total_amount FLOAT NOT NULL,
  Product_id INT NOT NULL,
  PRIMARY KEY (Order_id),
  FOREIGN KEY (Product_id) REFERENCES Product(Product_id)
);

CREATE TABLE Customers
(
  Customer_id INT NOT NULL,
  Name VARCHAR(50) NOT NULL,
  Review_id INT NOT NULL,
  Order_id INT NOT NULL,
  PRIMARY KEY (Customer_id),
  FOREIGN KEY (Review_id) REFERENCES Reviews(Review_id),
  FOREIGN KEY (Order_id) REFERENCES Orders(Order_id)
)

CREATE TABLE CustomerLoyaltyLevels (
  LoyaltyLevel_id SERIAL PRIMARY KEY,
  Customer_id INT NOT NULL,
  LoyaltyLevel VARCHAR(50) NOT NULL,
  StartDate DATE NOT NULL,
  EndDate DATE,
  FOREIGN KEY (Customer_id) REFERENCES Customers(Customer_id)
);

ALTER TABLE Customers
ADD COLUMN LoyaltyLevel_id INT;

ALTER TABLE Customers
ADD CONSTRAINT fk_loyalty_level
FOREIGN KEY (LoyaltyLevel_id) REFERENCES CustomerLoyaltyLevels(LoyaltyLevel_id);

SELECT * FROM customerloyaltylevels