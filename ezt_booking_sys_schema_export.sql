CREATE DATABASE  IF NOT EXISTS `ezt_booking_sys` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ezt_booking_sys`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: ezt_booking_sys
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bookings`
--

DROP TABLE IF EXISTS `bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookings` (
  `BookingID` int NOT NULL AUTO_INCREMENT,
  `TourID` int DEFAULT NULL,
  `CustomerID` int DEFAULT NULL,
  `BookingAccountName` varchar(255) DEFAULT NULL,
  `BookingNames` varchar(255) DEFAULT NULL,
  `TourDate` date DEFAULT NULL,
  `ConfirmationNum` varchar(100) DEFAULT NULL,
  `BookingNum` varchar(100) DEFAULT NULL,
  `AdultNum` int DEFAULT NULL,
  `AdultPrice` decimal(10,2) DEFAULT NULL,
  `ChildNum` int DEFAULT NULL,
  `ChildPrice` decimal(10,2) DEFAULT NULL,
  `InfantNum` int DEFAULT NULL,
  `InfantPrice` decimal(10,2) DEFAULT NULL,
  `FamilyNum` int DEFAULT NULL,
  `FamilyPrice` decimal(10,2) DEFAULT NULL,
  `PaymentID` int DEFAULT NULL,
  `BookingStatus` enum('Inquiry','Quote','Pending Payment','Pending Confirmation','Confirmed','Cancelled and Refunded','Cancelled and Charged') DEFAULT NULL,
  PRIMARY KEY (`BookingID`),
  KEY `CustomerID` (`CustomerID`),
  KEY `TourID` (`TourID`),
  KEY `PaymentID` (`PaymentID`),
  CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `customers` (`CustomerID`),
  CONSTRAINT `bookings_ibfk_2` FOREIGN KEY (`TourID`) REFERENCES `tours` (`TourID`),
  CONSTRAINT `bookings_ibfk_3` FOREIGN KEY (`PaymentID`) REFERENCES `payments` (`PaymentID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings`
--

LOCK TABLES `bookings` WRITE;
/*!40000 ALTER TABLE `bookings` DISABLE KEYS */;
INSERT INTO `bookings` VALUES (1,1,1,'John Doe','John and Family','2024-01-15','CN123','BN456',2,100.00,1,50.00,0,0.00,0,0.00,1,'Confirmed'),(2,2,2,'Jane Smith','Jane Smith','2024-02-20','CN789','BN101',1,80.00,0,0.00,0,0.00,0,0.00,2,'Pending Payment');
/*!40000 ALTER TABLE `bookings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `CustomerID` int NOT NULL AUTO_INCREMENT,
  `UserID` int DEFAULT NULL,
  `FirstName` varchar(255) DEFAULT NULL,
  `LastName` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Wechat` varchar(255) DEFAULT NULL,
  `Phone` varchar(20) DEFAULT NULL,
  `Note` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`CustomerID`),
  UNIQUE KEY `Email` (`Email`),
  KEY `idx_userid` (`UserID`),
  CONSTRAINT `customers_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `users` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,3,'John','Doe','johndoe@email.com','johndoe_wechat','1234567890',NULL),(2,4,'Jane','Smith','janesmith@email.com','janesmith_wechat','0987654321',NULL);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `PaymentID` int NOT NULL AUTO_INCREMENT,
  `Amount` decimal(10,2) DEFAULT NULL,
  `PaymentStatus` enum('Paid','Pending','Refunded') DEFAULT NULL,
  PRIMARY KEY (`PaymentID`),
  KEY `idx_paymentid` (`PaymentID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES (1,150.00,'Paid'),(2,80.00,'Pending'),(3,200.00,'Refunded');
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `touroperators`
--

DROP TABLE IF EXISTS `touroperators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `touroperators` (
  `OperatorID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `ContactName` varchar(255) DEFAULT NULL,
  `ContactEmail` varchar(255) DEFAULT NULL,
  `ContactPhone` varchar(20) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`OperatorID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `touroperators`
--

LOCK TABLES `touroperators` WRITE;
/*!40000 ALTER TABLE `touroperators` DISABLE KEYS */;
INSERT INTO `touroperators` VALUES (1,'Great Adventures','Alice Smith','alice@greatadventures.com','0987654321','123 Adventure St'),(2,'Wild Journeys','Bob Johnson','bob@wildjourneys.com','1122334455','456 Journey Rd');
/*!40000 ALTER TABLE `touroperators` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tours`
--

DROP TABLE IF EXISTS `tours`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tours` (
  `TourID` int NOT NULL AUTO_INCREMENT,
  `OperatorID` int DEFAULT NULL,
  `TourName` varchar(255) DEFAULT NULL,
  `TourDescription` varchar(255) DEFAULT NULL,
  `AdultPrice` decimal(10,2) DEFAULT NULL,
  `ChildPrice` decimal(10,2) DEFAULT NULL,
  `CheckInTime` time DEFAULT NULL,
  `ReportTime` time DEFAULT NULL,
  `Terms` varchar(500) DEFAULT NULL,
  `ReportingAdd` varchar(255) DEFAULT NULL,
  `CheckinAdd` varchar(255) DEFAULT NULL,
  `CommissionRate` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`TourID`),
  KEY `OperatorID` (`OperatorID`),
  KEY `idx_tourid` (`TourID`),
  CONSTRAINT `tours_ibfk_1` FOREIGN KEY (`OperatorID`) REFERENCES `touroperators` (`OperatorID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours`
--

LOCK TABLES `tours` WRITE;
/*!40000 ALTER TABLE `tours` DISABLE KEYS */;
INSERT INTO `tours` VALUES (1,1,'Queenstown Adventure','Exciting adventure in Queenstown',100.00,50.00,'09:00:00','08:30:00','Terms and conditions','123 Queenstown Rd','456 Queenstown Spot',10.00),(2,2,'Auckland City Tour','Explore the beauty of Auckland',80.00,40.00,'10:00:00','09:30:00','Terms and conditions','789 City Rd','101 City Spot',12.00);
/*!40000 ALTER TABLE `tours` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `UserID` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(255) DEFAULT NULL,
  `PasswordHash` varchar(255) DEFAULT NULL,
  `Type` enum('Admin','Agent','Customer') DEFAULT NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `Username` (`Username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','hashed_password1','Admin'),(2,'agent1','hashed_password2','Agent'),(3,'customer1','hashed_password3','Customer'),(4,'customer2','hashed_password4','Customer');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-05 14:59:52
