#Create table to store basic user information
CREATE TABLE Users (
    User_id INT AUTO_INCREMENT PRIMARY KEY,
    Full_name VARCHAR(100) NOT NULL,
    Phone_Number VARCHAR(15) UNIQUE,
    Account_Number VARCHAR(20) NULL,
    User_Type ENUM ('Customer', 'Agent', 'Merchant'),
    Keywords TEXT NOT NULL
);
