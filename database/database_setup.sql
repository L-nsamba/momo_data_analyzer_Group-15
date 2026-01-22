#Use DDL Statements to create table to store basic user information
CREATE TABLE Users (
    User_id INT AUTO_INCREMENT PRIMARY KEY,
    Full_name VARCHAR(100) NOT NULL,
    Phone_Number VARCHAR(15) UNIQUE,
    Account_Number VARCHAR(20) NULL,
    User_Type ENUM ('Customer', 'Agent', 'Merchant'),
    Keywords TEXT NOT NULL
);

#Example of some DML Statements to insert data into the table
INSERT  INTO Users(User_id, Full_name, Phone_Number, Account_Number, User_Type, Keywords)
VALUES
    (1, 'MitchellBarure', 0794467731, 9568899732,'Customer', '1 MitchellBarure, 0794467731, 9568899732, Customer'),
    (2, 'JohnMichael', 0893349976, 235179334, 'Agent', '2, JohnMichael, 0893347796, Agent');
