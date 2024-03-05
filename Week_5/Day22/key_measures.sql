
-- Overall number of books loaned:
SELECT COUNT(*) AS Overall_Books_Loaned
FROM Loans;

-- Currently loaned books (those with 'Loaned'):
SELECT COUNT(*) AS Currently_Loaned_Books
FROM Loans L
JOIN Book B ON L.Book_id = B.Book_id
WHERE B.Cur_status = 'Loaned';

-- Number of customers with multiple loans at the same time:
SELECT COUNT(DISTINCT Customer_id) AS Customers_With_Multiple_Loans
FROM Loans
WHERE Loan_start <= '2024-03-05'::DATE  -- Adjust the date as needed
  AND '2024-02-20'::DATE <= Loan_end;

-- Average loan time:
SELECT AVG(Loan_end - Loan_start) AS Average_Loan_Time
FROM Loans
WHERE Loan_end IS NOT NULL;

-- Update Book status when a book is loaned
UPDATE Book
SET Cur_status = 'Loaned'
WHERE Book_id IN (SELECT Book_id FROM Loans WHERE '2024-03-05'::DATE >= Loan_end);

-- Update Book status when a book is returned
UPDATE Book
SET Cur_status = 'Available'
WHERE Book_id IN (SELECT Book_id FROM Loans WHERE '2024-03-05'::DATE < Loan_end);