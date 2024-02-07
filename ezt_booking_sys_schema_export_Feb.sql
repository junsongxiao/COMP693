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
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `AdminID` int NOT NULL AUTO_INCREMENT,
  `UserID` int DEFAULT NULL,
  `FirstName` varchar(255) DEFAULT NULL,
  `LastName` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Phone` varchar(20) DEFAULT NULL,
  `Wechat` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`AdminID`),
  UNIQUE KEY `Email` (`Email`),
  KEY `UserID` (`UserID`),
  CONSTRAINT `admins_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `users` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES (1,11,'admin1','admin1','admin1@agency.com','9876543210','admin1wechat'),(2,4,'admin2','admin2','admin2@agency.com','987654310','admin2wechat');
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `agents`
--

DROP TABLE IF EXISTS `agents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agents` (
  `AgentID` int NOT NULL AUTO_INCREMENT,
  `UserID` int DEFAULT NULL,
  `FirstName` varchar(255) DEFAULT NULL,
  `LastName` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Phone` varchar(20) DEFAULT NULL,
  `Wechat` varchar(100) DEFAULT NULL,
  `AgencyName` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`AgentID`),
  UNIQUE KEY `Email` (`Email`),
  KEY `UserID` (`UserID`),
  KEY `idx_agentid` (`AgentID`),
  CONSTRAINT `agents_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `users` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agents`
--

LOCK TABLES `agents` WRITE;
/*!40000 ALTER TABLE `agents` DISABLE KEYS */;
INSERT INTO `agents` VALUES (1,2,'Jane','Doe','jane.doe@agency.com','9876543210','janewechat','Doe Travels'),(2,6,'Diana','Prince','diana.prince@agency.com','8765432109','dianawechat','Amazon Tours'),(3,8,'Bruce','Wayne','bruce.wayne@agency.com','7654321098','brucewechat','Wayne Enterprises'),(4,10,'Tony','Stark','tony.stark@agency.com','6543210987','tonywechat','Stark Industries');
/*!40000 ALTER TABLE `agents` ENABLE KEYS */;
UNLOCK TABLES;

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
  `AgentID` int DEFAULT NULL,
  `BookingAccountName` varchar(255) DEFAULT NULL,
  `BookingNames` varchar(255) DEFAULT NULL,
  `TourDate` date DEFAULT NULL,
  `ConfirmationNum` varchar(100) DEFAULT NULL,
  `BookingNum` varchar(100) DEFAULT NULL,
  `AdultNum` int DEFAULT NULL,
  `ChildNum` int DEFAULT NULL,
  `InfantNum` int DEFAULT NULL,
  `FamilyNum` int DEFAULT NULL,
  `PickUpLocation` varchar(255) DEFAULT NULL,
  `Note` varchar(255) DEFAULT NULL,
  `PaymentID` int DEFAULT NULL,
  `BookingStatus` enum('Inquiry','Quote','Pending Payment','Pending Confirmation','Confirmed','Cancelled and Refunded','Cancelled and Charged') DEFAULT NULL,
  `AdultQuote` decimal(10,2) DEFAULT NULL,
  `ChildQuote` decimal(10,2) DEFAULT NULL,
  `InfantQuote` decimal(10,2) DEFAULT NULL,
  `FamilyQuote` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`BookingID`),
  KEY `CustomerID` (`CustomerID`),
  KEY `AgentID` (`AgentID`),
  KEY `TourID` (`TourID`),
  KEY `PaymentID` (`PaymentID`),
  KEY `idx_bookingid` (`BookingID`),
  CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `customers` (`CustomerID`),
  CONSTRAINT `bookings_ibfk_2` FOREIGN KEY (`AgentID`) REFERENCES `agents` (`AgentID`),
  CONSTRAINT `bookings_ibfk_3` FOREIGN KEY (`TourID`) REFERENCES `tours` (`TourID`),
  CONSTRAINT `bookings_ibfk_4` FOREIGN KEY (`PaymentID`) REFERENCES `payments` (`PaymentID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings`
--

LOCK TABLES `bookings` WRITE;
/*!40000 ALTER TABLE `bookings` DISABLE KEYS */;
INSERT INTO `bookings` VALUES (1,1,1,1,'Steve Rogers','Steve and Friends','2023-12-22','CN1003','BN2003',3,0,0,0,'Campsite','Extra water',1,'Inquiry',150.00,100.00,10.00,600.00),(2,2,2,2,'Bruce Banner','Bruce Banner','2023-12-23','CN1004','BN2004',1,0,0,0,'Science Center','Special dietary needs',2,'Quote',200.00,180.00,0.00,800.00),(3,3,3,3,'Natasha Romanoff','Natasha and Team','2023-12-24','CN1005','BN2005',4,0,0,0,'Hotel Elite','Requires early check-in',3,'Inquiry',130.00,80.00,10.00,300.00),(4,4,4,4,'Tony Stark','Tony Stark','2023-12-25','CN1006','BN2006',1,0,0,0,'Stark Tower','VIP services',4,'Inquiry',200.00,190.00,10.00,500.00),(5,5,1,1,'Thor Odinson','Thor and Loki','2023-12-26','CN1007','BN2007',2,0,0,0,'Asgard Hotel','Special security needs',5,'Quote',200.00,170.00,150.00,1000.00),(6,6,2,2,'Loki Laufeyson','Loki Alone','2023-12-27','CN1008','BN2008',1,1,1,0,'Downtown Loft','Late night arrivals',6,'Quote',200.00,150.00,0.00,500.00),(7,7,3,3,'Wanda Maximoff','Wanda and Vision','2023-12-28','CN1009','BN2009',2,1,0,1,'Beachside Resort','Requesting privacy',7,'Confirmed',99.00,80.00,10.00,400.00),(8,8,4,4,'Peter Parker','Peter and MJ','2023-12-29','CN1010','BN2010',2,0,0,0,'City Hotel','Allergies to peanuts',8,'Pending Confirmation',130.00,100.00,20.00,200.00),(9,1,1,1,'Scott Lang','Scott and Cassie','2023-12-30','CN1011','BN2011',1,1,0,0,'Country Inn','Needs extra bedding',9,'Quote',110.00,80.00,19.00,300.00),(10,2,2,2,'Stephen Strange','Stephen Alone','2023-12-31','CN1012','BN2012',1,0,0,0,'Mystic Hotel','Late checkout requested',10,'Confirmed',120.00,90.00,10.00,500.00),(13,1,5,NULL,NULL,NULL,'2024-02-01',NULL,NULL,1,2,0,0,'21 lincoln road','23',NULL,'Pending Payment',22.00,23.00,23.00,23.00),(14,1,5,NULL,'samuelx','Name1, name2','2024-02-02',NULL,NULL,2,1,0,0,'21 lincoln road','additional notes..',NULL,'Pending Confirmation',120.00,90.00,0.00,0.00),(15,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Inquiry',NULL,NULL,NULL,NULL);
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
  `Phone` varchar(20) DEFAULT NULL,
  `Wechat` varchar(100) DEFAULT NULL,
  `Preferences` varchar(500) DEFAULT NULL,
  `Notes` text,
  PRIMARY KEY (`CustomerID`),
  UNIQUE KEY `Email` (`Email`),
  KEY `UserID` (`UserID`),
  KEY `idx_customerid` (`CustomerID`),
  CONSTRAINT `customers_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `users` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,1,'John','Doe','words4sammy@gmail.com','1234567890','johnwechat','Window seat','No special notes'),(2,5,'Charlie','Brown','charlie.brown@email.com','2345678901','charliewechat','Aisle seat','Allergic to nuts'),(3,7,'Peter','Parker','peter.parker@email.com','3456789012','peterwechat','Extra legroom','Frequent traveler'),(4,9,'Clark','Kent','clark.kent@email.com','4567890123','clarkwechat','Near exit','Prefers vegetarian meals'),(5,12,'Sammy','Xiao','sammyxiao@gmail.com','0279505556','wechat123',NULL,NULL);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operators`
--

DROP TABLE IF EXISTS `operators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `operators` (
  `OperatorID` int NOT NULL AUTO_INCREMENT,
  `OperatorName` varchar(255) DEFAULT NULL,
  `ContactName` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Phone` varchar(20) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`OperatorID`),
  KEY `idx_operatorid` (`OperatorID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operators`
--

LOCK TABLES `operators` WRITE;
/*!40000 ALTER TABLE `operators` DISABLE KEYS */;
INSERT INTO `operators` VALUES (1,'None','None','example@example.com','None','Nones'),(2,'Adventure Co','Grace Lee','grace@adventureco.com','8765432109','456 Adventure Ave'),(3,'Nature Trips','Ethan Brown','ethan@naturetrips.com','7654321098','789 Nature St'),(4,'Cultural Voyages','Sophia Johnson','sophia@culturalvoyages.com','6543210987','321 Culture Rd'),(5,'City Tours','Noah Davis','noah@citytours.com','5432109876','123 City Lane'),(6,'Mountain Expeditions','Emma Wilson','emma@mountainexpeditions.com','4321098765','654 Mountain Pass'),(7,'Beach Getaways','Olivia Martinez','olivia@beachgetaways.com','3210987654','789 Ocean Blvd'),(8,'Historical Journeys','Liam Garcia','liam@historicaljourneys.com','2109876543','987 History Ln'),(9,'Space Adventures','Ava Lee','ava@spaceadventures.com','1098765432','321 Space Center Rd'),(10,'Wildlife Safari','Mia Brown','mia@wildlifesafari.com','0987654321','456 Animal St');
/*!40000 ALTER TABLE `operators` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES (1,200.00,'Paid'),(2,450.00,'Pending'),(3,100.00,'Refunded'),(4,180.00,'Paid'),(5,400.00,'Pending'),(6,250.00,'Refunded'),(7,550.00,'Paid'),(8,300.00,'Pending'),(9,500.00,'Refunded'),(10,600.00,'Paid');
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
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
  `City` varchar(255) DEFAULT NULL,
  `Region` varchar(255) DEFAULT NULL,
  `TourDescription` varchar(255) DEFAULT NULL,
  `AdultPrice` decimal(10,2) DEFAULT NULL,
  `ChildPrice` decimal(10,2) DEFAULT NULL,
  `InfantPrice` decimal(10,2) DEFAULT NULL,
  `FamilyPrice` decimal(10,2) DEFAULT NULL,
  `TourTime` time DEFAULT NULL,
  `ReportTime` time DEFAULT NULL,
  `Terms` varchar(500) DEFAULT NULL,
  `ReportingAdd` varchar(255) DEFAULT NULL,
  `TourAdd` varchar(255) DEFAULT NULL,
  `CommissionRate` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`TourID`),
  KEY `OperatorID` (`OperatorID`),
  KEY `idx_tourid` (`TourID`),
  CONSTRAINT `tours_ibfk_1` FOREIGN KEY (`OperatorID`) REFERENCES `operators` (`OperatorID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tours`
--

LOCK TABLES `tours` WRITE;
/*!40000 ALTER TABLE `tours` DISABLE KEYS */;
INSERT INTO `tours` VALUES (1,3,'Safari Adventure','Waikato','North Island','A thrilling safari experience with wildlife.',250.00,125.00,60.00,600.00,'06:00:00','05:30:00','Terms apply.','123 Safari Park','Wildlife Area',15.00),(2,4,'Cultural Tour','Christchurch','South Island','Explore the rich cultural heritage of the city.',150.00,75.00,0.00,350.00,'10:00:00','09:30:00','Terms apply.','321 Culture Rd','Historic Center',10.00),(3,5,'Mountain Hike','Queenstown','South Island','Conquer the peaks on this challenging hike.',180.00,90.00,0.00,400.00,'07:00:00','06:30:00','Terms apply.','654 Mountain Pass','Highpeak',12.00),(4,6,'Beach Day Out','Queenstown','South Island','Relax and enjoy a day at the beautiful beach.',120.00,60.00,0.00,300.00,'11:00:00','10:30:00','Terms apply.','789 Ocean Blvd','Sunny Beach',10.00),(5,7,'Historical Journey','Queenstown','South Island','Step back in time with a visit to historic sites.',160.00,80.00,40.00,380.00,'09:00:00','08:30:00','Terms apply.','987 History Ln','Oldtown',11.00),(6,8,'Space Center Tour','Hamilton','North Island','Discover the wonders of space and science.',220.00,110.00,55.00,500.00,'08:00:00','07:45:00','Terms apply.','321 Space Center Rd','Starcity',15.00),(7,9,'Wildlife Safari','Dunedin','South Island','Get close to nature with a guided safari.',240.00,120.00,60.00,550.00,'05:00:00','04:45:00','Terms apply.','456 Animal St','Wildlife Park',18.00),(8,10,'Urban Exploration','Christchurch','North Island','Discover the secrets of the city.',130.00,65.00,0.00,320.00,'10:00:00','09:45:00','Terms apply.','123 City Lane','Downtown',10.00),(9,1,'any','any','','description',120.00,100.00,0.00,0.00,'12:05:00','13:06:00','some text','address 1','address 2',15.00);
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
  `Type` enum('Admin','Agent','Customer','Guest') DEFAULT NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `Username` (`Username`),
  KEY `idx_userid` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'johnDoe','hashedpassword1','Customer'),(2,'janeDoe','hashedpassword2','Agent'),(3,'bobSmith','hashedpassword3','Admin'),(4,'aliceJones','hashedpassword4','Guest'),(5,'charlieBrown','hashedpassword5','Customer'),(6,'dianaPrince','hashedpassword6','Agent'),(7,'peterParker','hashedpassword7','Customer'),(8,'clarkKent','hashedpassword8','Admin'),(9,'bruceWayne','hashedpassword9','Agent'),(10,'tonyStark','hashedpassword10','Guest'),(11,'admin','$2b$12$WJ0.dFRYsBmLobM2ah2V8euf3KNkcsJieb2170fo27pUD/TT2uUSa','Admin'),(12,'customer','$2b$12$UfdGqYIR0wpCnMcwRqxMKOk15rFg18.J7bBzIHuJs3oiI/p4AVCP6','Customer');
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

-- Dump completed on 2024-02-06 10:40:33
