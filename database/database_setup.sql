CREATE TABLE transactions (
    transaction_id INT NOT NULL AUTO_INCREMENT
        COMMENT 'Unique identifier for each transaction',

    sender_id INT NOT NULL
        COMMENT 'User who initiates the transaction (money sender)',

    receiver_id INT NOT NULL
        COMMENT 'User who receives the funds',

    category_id INT NOT NULL
        COMMENT 'Transaction category classification',

    amount DECIMAL(12,2) NOT NULL
        COMMENT 'Transaction amount excluding fees',

    transaction_fee DECIMAL(12,2) DEFAULT 0.00
        COMMENT 'Fee charged for processing the transaction',

    balance_after DECIMAL(12,2) NOT NULL
        COMMENT 'Sender account balance after transaction completion',

    transaction_type VARCHAR(50)
        COMMENT 'Logical transaction type (SEND, RECEIVE, PAYMENT, CASH_OUT)',

    status VARCHAR(20) DEFAULT 'SUCCESS'
        COMMENT 'Transaction status (SUCCESS, FAILED, PENDING)',

    transaction_reference VARCHAR(100)
        COMMENT 'Unique external reference for the transaction',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        COMMENT 'Timestamp when the transaction was created',

    FOREIGN KEY (sender_id) REFERENCES users(user_id),
    FOREIGN KEY (receiver_id) REFERENCES users(user_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);
