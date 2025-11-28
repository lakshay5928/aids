
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(50),
    City VARCHAR(50),
    Email VARCHAR(100)
);

CREATE TABLE Loan (
    LoanID INT PRIMARY KEY,
    LoanType VARCHAR(50),
    BankName VARCHAR(50)
);

CREATE TABLE Borrows (
    CustomerID INT,
    LoanID INT,
    LoanAmount DECIMAL(10,2),
    PRIMARY KEY (CustomerID, LoanID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (LoanID) REFERENCES Loan(LoanID)
);

CREATE OR REPLACE TRIGGER prevent_negative_loan_amount
BEFORE INSERT OR UPDATE ON Borrows
FOR EACH ROW
BEGIN
    IF :NEW.LoanAmount < 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'Loan Amount cannot be negative');
    END IF;
END;
/



INSERT INTO Customer(CustomerID, Name, City, Email)
VALUES (customer_id_seq.NEXTVAL, 'Rahul', 'Delhi', 'rahul@gmail.com');

CREATE VIEW Car_Loan_Customers AS
SELECT 
    C.CustomerID,
    C.Name,
    C.City,
    L.LoanID,
    L.LoanType,
    B.LoanAmount
FROM Customer C
JOIN Borrows B ON C.CustomerID = B.CustomerID
JOIN Loan L ON B.LoanID = L.LoanID
WHERE L.LoanType = 'Car';
