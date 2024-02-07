-- select * from bookings;
-- SELECT UserID FROM Users;
-- SELECT UserID FROM Customers;
-- SELECT UserID FROM Agents;


-- Create ezi_booking_sys schema
CREATE SCHEMA IF NOT EXISTS `ezt_booking_sys` DEFAULT CHARACTER SET utf8 ;
USE `ezt_booking_sys`;

-- Users Table
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(255) UNIQUE,
    PasswordHash VARCHAR(255),
    Type ENUM('Admin', 'Agent', 'Customer', 'Guest')    
);

-- Admin Table
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
  CONSTRAINT `admins_ibfk_1`
  FOREIGN KEY (`UserID`) REFERENCES `users` (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Customers Table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    UserID INT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    Phone VARCHAR(20),
    Wechat VARCHAR(100),
    Preferences VARCHAR(500),
    Notes TEXT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Agents Table
CREATE TABLE Agents (
    AgentID INT PRIMARY KEY AUTO_INCREMENT,
    UserID INT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    Phone VARCHAR(20),
    Wechat VARCHAR(100),
    AgencyName VARCHAR(255),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Operators Table
CREATE TABLE Operators (
    OperatorID INT PRIMARY KEY AUTO_INCREMENT,
    OperatorName VARCHAR(255),
    ContactName VARCHAR(255),
    Email VARCHAR(255),
    Phone VARCHAR(20),
    Address VARCHAR(255)
);

-- Tours Table
CREATE TABLE Tours (
    TourID INT PRIMARY KEY AUTO_INCREMENT,
    OperatorID INT,
    TourName VARCHAR(255),
    City VARCHAR(255),
    Region VARCHAR(255),
    TourDescription VARCHAR(255),
    AdultPrice DECIMAL(10, 2),
    ChildPrice DECIMAL(10, 2),
    InfantPrice DECIMAL(10, 2),
    FamilyPrice DECIMAL(10, 2),
    TourTime TIME,
    ReportTime TIME,
    Terms TEXT,
    ReportingAdd VARCHAR(255),
    TourAdd VARCHAR(255),
    CommissionRate DECIMAL(5, 2),
    FOREIGN KEY (OperatorID) REFERENCES Operators(OperatorID)
);

-- Payments Table
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,
    Amount DECIMAL(10,2),
    PaymentStatus ENUM('Paid','Pending','Refunded')
);

-- Bookings Table
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,
    TourID INT,
    CustomerID INT,
    AgentID INT,
    BookingAccountName VARCHAR(255),
    BookingNames VARCHAR(255),
    TourDate Date,
    ConfirmationNum VARCHAR(100),
    BookingNum VARCHAR(100),
    AdultNum INT,
    ChildNum INT,
    InfantNum INT,
    FamilyNum INT,
    QuotedAdultPrice DECIMAL(10, 2),
    QuotedChildPrice DECIMAL(10, 2),
    QuotedInfantPrice DECIMAL(10, 2),
    QuotedFamilyPrice DECIMAL(10, 2),
    PickUpLocation VARCHAR(255),
    Note VARCHAR(255),  
    PaymentID INT,
    BookingStatus ENUM('Inquiry', 'Quote', 'Pending Payment', 'Pending Confirmation', 'Confirmed', 'Cancelled and Refunded', 'Cancelled and Charged'),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (AgentID) REFERENCES Agents(AgentID),
    FOREIGN KEY (TourID) REFERENCES Tours(TourID),
    FOREIGN KEY (PaymentID) REFERENCES Payments(PaymentID)
);

-- Adding Indexes for Performance
CREATE INDEX idx_customerid ON Customers(CustomerID);
CREATE INDEX idx_agentid ON Agents(AgentID);
CREATE INDEX idx_userid ON Users(UserID);
CREATE INDEX idx_tourid ON Tours(TourID);
CREATE INDEX idx_bookingid ON Bookings(BookingID);
CREATE INDEX idx_paymentid ON Payments(PaymentID);
CREATE INDEX idx_operatorid ON Operators(OperatorID);

-- Inserting Users
INSERT INTO Users (Username, PasswordHash, Type) VALUES
('johnDoe', 'hashedpassword1', 'Customer'),
('janeDoe', 'hashedpassword2', 'Agent'),
('bobSmith', '$2b$12$WJ0.dFRYsBmLobM2ah2V8euf3KNkcsJieb2170fo27pUD/TT2uUSa', 'Admin'),
('aliceJones', 'hashedpassword4', 'Guest'),
('charlieBrown', '$2b$12$UfdGqYIR0wpCnMcwRqxMKOk15rFg18.J7bBzIHuJs3oiI/p4AVCP6', 'Customer'),
('dianaPrince', 'hashedpassword6', 'Agent'),
('peterParker', '$2b$12$UfdGqYIR0wpCnMcwRqxMKOk15rFg18.J7bBzIHuJs3oiI/p4AVCP6', 'Customer'),
('clarkKent', 'hashedpassword8', 'Admin'),
('bruceWayne', 'hashedpassword9', 'Agent'),
('tonyStark', 'hashedpassword10', 'Guest');
('admin','$2b$12$WJ0.dFRYsBmLobM2ah2V8euf3KNkcsJieb2170fo27pUD/TT2uUSa','Admin'),
('customer','$2b$12$UfdGqYIR0wpCnMcwRqxMKOk15rFg18.J7bBzIHuJs3oiI/p4AVCP6','Customer');


-- Inserting Admins
INSERT INTO `admins` VALUES 
(1,11,'admin1','admin1','admin1@agency.com','9876543210','admin1wechat'),
(2,4,'admin2','admin2','admin2@agency.com','987654310','admin2wechat');

-- Inserting Customers
INSERT INTO Customers (UserID, FirstName, LastName, Email, Phone, Wechat, Preferences, Notes) VALUES
(1, 'John', 'Doe', 'john.doe@email.com', '1234567890', 'johnwechat', 'Window seat', 'No special notes'),
(5, 'Charlie', 'Brown', 'charlie.brown@email.com', '2345678901', 'charliewechat', 'Aisle seat', 'Allergic to nuts'),
(7, 'Peter', 'Parker', 'peter.parker@email.com', '3456789012', 'peterwechat', 'Extra legroom', 'Frequent traveler'),
(9, 'Clark', 'Kent', 'clark.kent@email.com', '4567890123', 'clarkwechat', 'Near exit', 'Prefers vegetarian meals');

-- Inserting Agents
INSERT INTO Agents (UserID, FirstName, LastName, Email, Phone, Wechat, AgencyName) VALUES
(2, 'Jane', 'Doe', 'jane.doe@agency.com', '9876543210', 'janewechat', 'Doe Travels'),
(6, 'Diana', 'Prince', 'diana.prince@agency.com', '8765432109', 'dianawechat', 'Amazon Tours'),
(8, 'Bruce', 'Wayne', 'bruce.wayne@agency.com', '7654321098', 'brucewechat', 'Wayne Enterprises'),
(10, 'Tony', 'Stark', 'tony.stark@agency.com', '6543210987', 'tonywechat', 'Stark Industries');

-- ... (The rest of your INSERT statements)

INSERT INTO Operators (OperatorName, ContactName, Email, Phone, Address) VALUES
('Happy Tours', 'Liam Smith', 'liam@happytours.com', '9876543210', '123 Happy St'),
('Adventure Co', 'Grace Lee', 'grace@adventureco.com', '8765432109', '456 Adventure Ave'),
('Nature Trips', 'Ethan Brown', 'ethan@naturetrips.com', '7654321098', '789 Nature St'),
('Cultural Voyages', 'Sophia Johnson', 'sophia@culturalvoyages.com', '6543210987', '321 Culture Rd'),
('City Tours', 'Noah Davis', 'noah@citytours.com', '5432109876', '123 City Lane'),
('Mountain Expeditions', 'Emma Wilson', 'emma@mountainexpeditions.com', '4321098765', '654 Mountain Pass'),
('Beach Getaways', 'Olivia Martinez', 'olivia@beachgetaways.com', '3210987654', '789 Ocean Blvd'),
('Historical Journeys', 'Liam Garcia', 'liam@historicaljourneys.com', '2109876543', '987 History Ln'),
('Space Adventures', 'Ava Lee', 'ava@spaceadventures.com', '1098765432', '321 Space Center Rd'),
('Wildlife Safari', 'Mia Brown', 'mia@wildlifesafari.com', '0987654321', '456 Animal St');

INSERT INTO Tours (OperatorID, TourName,City, Region,TourDescription, AdultPrice, ChildPrice, InfantPrice, FamilyPrice, TourTime, ReportTime, Terms, ReportingAdd, TourAdd, CommissionRate) VALUES
(3, 'Safari Adventure', 'Waikato', 'North Island','A thrilling safari experience with wildlife.', 250.00, 125.00, 60.00, 600.00, '06:00:00', '05:30:00', 'Terms apply.', '123 Safari Park', 'Wildlife Area', 15.00),
(4, 'Cultural Tour', 'Christchurch', 'South Island', 'Explore the rich cultural heritage of the city.', 150.00, 75.00, 0.00, 350.00, '10:00:00', '09:30:00', 'Terms apply.', '321 Culture Rd', 'Historic Center', 10.00),
(5, 'Mountain Hike', 'Queenstown', 'South Island', 'Conquer the peaks on this challenging hike.', 180.00, 90.00, 0.00, 400.00, '07:00:00', '06:30:00', 'Terms apply.', '654 Mountain Pass', 'Highpeak', 12.00),
(6, 'Beach Day Out', 'Queenstown', 'South Island', 'Relax and enjoy a day at the beautiful beach.', 120.00, 60.00, 0.00, 300.00, '11:00:00', '10:30:00', 'Terms apply.', '789 Ocean Blvd', 'Sunny Beach', 10.00),
(7, 'Historical Journey', 'Queenstown', 'South Island', 'Step back in time with a visit to historic sites.', 160.00, 80.00, 40.00, 380.00, '09:00:00', '08:30:00', 'Terms apply.', '987 History Ln', 'Oldtown', 11.00),
(8, 'Space Center Tour', 'Hamilton', 'North Island', 'Discover the wonders of space and science.', 220.00, 110.00, 55.00, 500.00, '08:00:00', '07:45:00', 'Terms apply.', '321 Space Center Rd', 'Starcity', 15.00),
(9, 'Wildlife Safari', 'Dunedin', 'South Island', 'Get close to nature with a guided safari.', 240.00, 120.00, 60.00, 550.00, '05:00:00', '04:45:00', 'Terms apply.', '456 Animal St', 'Wildlife Park', 18.00),
(10, 'Urban Exploration', 'Christchurch', 'North Island', 'Discover the secrets of the city.', 130.00, 65.00, 0.00, 320.00, '10:00:00', '09:45:00', 'Terms apply.', '123 City Lane', 'Downtown', 10.00);

INSERT INTO Payments (Amount, PaymentStatus) VALUES
(200.00, 'Paid'),
(450.00, 'Pending'),
(100.00, 'Refunded'),
(180.00, 'Paid'),
(400.00, 'Pending'),
(250.00, 'Refunded'),
(550.00, 'Paid'),
(300.00, 'Pending'),
(500.00, 'Refunded'),
(600.00, 'Paid');
INSERT INTO Bookings (
    TourID, CustomerID, AgentID, BookingAccountName, BookingNames, 
    TourDate, ConfirmationNum, BookingNum, AdultNum, ChildNum, 
    InfantNum, FamilyNum, PickUpLocation, Note, PaymentID, BookingStatus
) VALUES
(1, 1, 1, 'Steve Rogers', 'Steve and Friends', '2023-12-22', 'CN1003', 'BN2003', 3, 0, 0, 0, 'Campsite', 'Extra water', 1, 'Confirmed'),
(2, 2, 2, 'Bruce Banner', 'Bruce Banner', '2023-12-23', 'CN1004', 'BN2004', 1, 0, 0, 0, 'Science Center', 'Special dietary needs', 2, 'Pending Payment'),
(3, 3, 3, 'Natasha Romanoff', 'Natasha and Team', '2023-12-24', 'CN1005', 'BN2005', 4, 0, 0, 0, 'Hotel Elite', 'Requires early check-in', 3, 'Confirmed'),
(4, 4, 4, 'Tony Stark', 'Tony Stark', '2023-12-25', 'CN1006', 'BN2006', 1, 0, 0, 0, 'Stark Tower', 'VIP services', 4, 'Pending Confirmation'),
(5, 1, 1, 'Thor Odinson', 'Thor and Loki', '2023-12-26', 'CN1007', 'BN2007', 2, 0, 0, 0, 'Asgard Hotel', 'Special security needs', 5, 'Confirmed'),
(6, 2, 2, 'Loki Laufeyson', 'Loki Alone', '2023-12-27', 'CN1008', 'BN2008', 1, 1, 1, 0, 'Downtown Loft', 'Late night arrival', 6, 'Pending Payment'),
(7, 3, 3, 'Wanda Maximoff', 'Wanda and Vision', '2023-12-28', 'CN1009', 'BN2009', 2, 1, 0, 1, 'Beachside Resort', 'Requesting privacy', 7, 'Confirmed'),
(8, 4, 4, 'Peter Parker', 'Peter and MJ', '2023-12-29', 'CN1010', 'BN2010', 2, 0, 0, 0, 'City Hotel', 'Allergies to peanuts', 8, 'Pending Confirmation'),
(1, 1, 1, 'Scott Lang', 'Scott and Cassie', '2023-12-30', 'CN1011', 'BN2011', 1, 1, 0, 0, 'Country Inn', 'Needs extra bedding', 9, 'Confirmed'),
(2, 2, 2, 'Stephen Strange', 'Stephen Alone', '2023-12-31', 'CN1012', 'BN2012', 1, 0, 0, 0, 'Mystic Hotel', 'Late checkout requested', 10, 'Confirmed');
