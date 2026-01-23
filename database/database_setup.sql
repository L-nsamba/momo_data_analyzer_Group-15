#DDL Statements to create system logs table
CREATE TABLE system_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    raw_message TEXT NOT NULL, #Stores the full XML string 
    processing_status ENUM('pending', 'success', 'failed') DEFAULT 'pending', #Track the lifecycle of the data
    error TEXT DEFAULT NULL, #Field to store error details if status is 'failed'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    processed_at TIMESTAMP NULL DEFAULT NULL
);

#Sample DML statements to populate the system_logs table
INSERT INTO system_logs (raw_message, processing_status)
VALUES
    ('<sms protocol="0" address="M-Money" date="1715351458724" type="1" subject="null" body="You have received 2000 RWF from Jane Smith (*********013) on your mobile money account at 2024-05-10 16:30:51. Message from sender: . Your new balance:2000 RWF. Financial Transaction Id: 76662021700." toa="null" sc_toa="null" service_center="+250788110381" read="1" status="-1" locked="0" date_sent="1715351451000" sub_id="6" readable_date="10 May 2024 4:30:58 PM" contact_name="(Unknown)" />',
    'pending')
    ('transaction message sample 2''failed');
