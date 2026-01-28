-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: mysql-33d76eb2-alustudent-26bb.f.aivencloud.com    Database: momo_data_analyzer
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `User_id` int NOT NULL AUTO_INCREMENT,
  `Full_name` varchar(100) NOT NULL,
  `Phone_Number` varchar(15) DEFAULT NULL,
  `Account_Number` varchar(20) DEFAULT NULL, /*NULL ensures that the table still operates even if a user does not have an Account_number*/
  `User_Type` enum('Customer','Agent','Merchant') DEFAULT NULL,
  `Keywords` text NOT NULL, /*Search Indexing to ensure user can find data faster*/
  PRIMARY KEY (`User_id`),
  UNIQUE KEY `Phone_Number` (`Phone_Number`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'MitchellBarure','794467731','9568899732','Customer','1 MitchellBarure, 0794467731, 9568899732, Customer'),(2,'JohnMichael','893349976','235179334','Agent','2, JohnMichael, 0893347796, Agent'),(3,'GustavoFrank','777967578','909090909','Customer','3, GustavoFrank, 777967578, 909090909, Customer'),(4,'LeonNsamba','779495055','12345678','Agent','4, LeonNsamba, 779495055, Agent'),(5,'DarrenGlover','771435066','8769089087','Customer','5, DarrenGlover, 771435066, 8769089087, Customer');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_logs`
--

DROP TABLE IF EXISTS `system_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_logs` (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `raw_message` text NOT NULL, /*Stores the full XML string */
  `processing_status` enum('pending','success','failed') DEFAULT 'pending', /*Track the lifecycle of the data*/
  `error` text, /*Field to store error details if status is 'failed'*/
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `processed_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_logs`
--

LOCK TABLES `system_logs` WRITE;
/*!40000 ALTER TABLE `system_logs` DISABLE KEYS */;
INSERT INTO `system_logs` VALUES (1,'<transaction><amount>200000.00</amount><user>1</user></transaction','pending',NULL,'2026-01-23 17:39:16',NULL),(2,'<transaction><amount>17500.00</amount><user>2</user></transaction','pending',NULL,'2026-01-23 17:40:33',NULL),(3,'<transaction><amount>37000.00</amount><user>3</user></transaction','pending',NULL,'2026-01-23 17:41:24',NULL),(4,'<transaction><amount>9900.00</amount><user>4</user></transaction','pending',NULL,'2026-01-23 18:41:29',NULL),(5,'<transaction><amount>122000.00</amount><user>5</user></transaction','pending',NULL,'2026-01-23 18:41:58',NULL);
/*!40000 ALTER TABLE `system_logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction_categories`
--

DROP TABLE IF EXISTS `transaction_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction_categories` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) NOT NULL,
  `category_type` varchar(50) NOT NULL,
  `sub_category` varchar(50) NOT NULL,
  `keywords` text NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction_categories`
--

LOCK TABLES `transaction_categories` WRITE;
/*!40000 ALTER TABLE `transaction_categories` DISABLE KEYS */;
INSERT INTO `transaction_categories` VALUES (1,'Salary','Income','Monthly Salary','Salary, Income, Monthly Credit'),(3,'Transport','Expense','Public Transport','Transport, Bus, Taxi, Car'),(4,'Groceries','Expense','Food','SuperMarket, Expense, Food'),(5,'Transport','Expense','Public Transport','Bus, Taxi, Car, Expense'),(6,'Utilities','Expense','Monthly Bills','Water, Gas, Electricity, Expense');
/*!40000 ALTER TABLE `transaction_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `transaction_id` int NOT NULL AUTO_INCREMENT
    COMMENT 'Primary key uniquely identifying each transaction',

  `sender_id` int NOT NULL
    COMMENT 'User ID of the sender initiating the transaction',

  `receiver_id` int NOT NULL
    COMMENT 'User ID of the receiver of the transaction',

  `category_id` int NOT NULL
    COMMENT 'Category identifier describing the transaction type',

  `amount` decimal(12,2) NOT NULL
    COMMENT 'Transaction amount excluding transaction fees',

  `transaction_fee` decimal(12,2) DEFAULT '0.00'
    COMMENT 'Fee charged for processing the transaction',

  `balance_after` decimal(12,2) NOT NULL
    COMMENT 'Sender account balance after the transaction is completed',

  `transaction_type` varchar(50) DEFAULT NULL
    COMMENT 'Logical type of transaction such as SEND, RECEIVE, PAYMENT',

  `status` varchar(20) DEFAULT 'SUCCESS'
    COMMENT 'Transaction processing status (SUCCESS, FAILED, PENDING)',

  `transaction_references` varchar(100) DEFAULT NULL
    COMMENT 'Unique external or system-generated transaction reference',

  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
    COMMENT 'Timestamp indicating when the transaction was created',
  PRIMARY KEY (`transaction_id`),
  UNIQUE KEY `transaction_references` (`transaction_references`),
  KEY `sender_id` (`sender_id`),
  KEY `receiver_id` (`receiver_id`),
  KEY `fk_transactions_category` (`category_id`),
  CONSTRAINT `fk_transactions_category` FOREIGN KEY (`category_id`) REFERENCES `transaction_categories` (`category_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `Users` (`User_id`),
  CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`receiver_id`) REFERENCES `Users` (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES (1,4,5,1,200000.00,1000.00,250000.00,'Credit','SUCCESS','TX001','2026-01-23 18:56:00'),(3,2,3,3,17500.00,1000.00,51000.00,'Debit','SUCCESS','TX002','2026-01-23 19:04:00'),(4,2,1,4,37000.00,1000.00,76200.00,'Credit','SUCCESS','TX003','2026-01-23 19:08:00'),(5,4,2,5,9900.00,1000.00,12700.00,'Debit','SUCCESS','TX004','2026-01-23 19:09:00'),(6,2,3,6,122000.00,1000.00,150500.00,'Credit','SUCCESS','TX005','2026-01-23 19:10:00');
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_category_map`
--

DROP TABLE IF EXISTS `user_category_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_category_map` (
  `user_category_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `category_id` int DEFAULT NULL,
  PRIMARY KEY (`user_category_id`),
  KEY `user_id` (`user_id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `user_category_map_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`User_id`),
  CONSTRAINT `user_category_map_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `transaction_categories` (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_category_map`
--

LOCK TABLES `user_category_map` WRITE;
/*!40000 ALTER TABLE `user_category_map` DISABLE KEYS */;
INSERT INTO `user_category_map` VALUES (1,1,1),(2,2,3),(3,3,4),(4,4,5),(5,5,6);
/*!40000 ALTER TABLE `user_category_map` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-01-23 22:57:36
