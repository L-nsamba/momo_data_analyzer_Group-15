CREATE TABLE transaction_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    category_type VARCHAR(50) NOT NULL,
    sub_category VARCHAR(50) NOT NULL,
    transaction_id INT NOT NULL,
    transaction_sign INT NOT NULL,
    keywords TEXT NOT NULL,

    CONSTRAINT chk_transaction_sign
        CHECK ( transaction_sign IN (1, -1) ),

    CONSTRAINT fk_transaction_categories_transaction
        FOREIGN KEY (transaction_id)
        REFERENCES transactions (transaction_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Inserting parent codes first from transactions table
INSERT INTO transactions (transaction_id)
VALUES (101), (102);

-- Inserting the next records (auto increment handled by mysql)
INSERT INTO transaction_categories
(category_name, category_type, sub_category, transaction_id, transaction_sign, keywords)
VALUES
    ('Salary', 'Income', 'Monthly Salary', 101, 1, 'Salary Income Monthly Credit'),
    ('Groceries', 'Expense', 'Food', 102, -1, 'Groceries Food Expense Debit');
