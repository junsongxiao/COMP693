
from model.db import database_execute_lastrowid, database_execute_query_fetchall, database_execute_action, database_execute_query_fetchone
from model.users import Users




class Bookings:
    def __init__(self, tour_id, customer_id, agent_id, booking_account_name, booking_names, tour_date, confirmation_num, booking_num, adult_num, child_num, infant_num, family_num, pick_up_location, note, payment_id, booking_status):
        self._booking_id = None
        self._tour_id = tour_id
        self._customer_id = customer_id
        self._agent_id = agent_id
        self._agent_id = agent_id
        self._booking_account_name = booking_account_name
        self._booking_names = booking_names
        self._tour_date = tour_date
        self._confirmation_num = confirmation_num
        self._booking_num = booking_num
        self._adult_num = adult_num
        self._child_num = child_num
        self._infant_num = infant_num
        self._family_num = family_num
        self._pick_up_location = pick_up_location
        self._note = note
        self._payment_id = payment_id
        self._booking_status = booking_status

    ##getters
    @property
    def booking_id(self):
        return self._booking_id
    @property
    def tour_id(self):
        return self._tour_id
    @property
    def customer_id(self):
        return self._customer_id
    @property
    def agent_id(self):
        return self._agent_id
    @property
    def booking_account_name(self):
        return self._booking_account_name
    @property
    def booking_names(self):
        return self._booking_names
    @property
    def tour_date(self):
        return self._tour_date
    @property
    def confirmation_num(self):
        return self._confirmation_num
    @property
    def booking_num(self):
        return self._booking_num
    @property
    def adult_num(self):
        return self._adult_num
    @property
    def child_num(self):
        return self._child_num
    @property
    def infant_num(self):
        return self._infant_num
    @property
    def family_num(self):
        return self._family_num
    @property
    def pick_up_location(self):
        return self._pick_up_location
    @property
    def note(self):
        return self._note
    @property
    def payment_id(self):
        return self._payment_id
    @property
    def booking_status(self):
        return self._booking_status
    
    ##setters
    @booking_id.setter
    def booking_id(self, value):
        self._booking_id = value
    @tour_id.setter
    def tour_id(self, value):
        self._tour_id = value
    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @booking_account_name.setter
    def booking_account_name(self, value):
        self._booking_account_name = value
    @booking_names.setter
    def booking_names(self, value):
        self._booking_names = value
    @tour_date.setter
    def tour_date(self, value):
        self._tour_date = value
    @confirmation_num.setter
    def confirmation_num(self, value):
        self._confirmation_num = value
    @booking_num.setter
    def booking_num(self, value):
        self._booking_num = value
    @adult_num.setter
    def adult_num(self, value):
        self._adult_num = value
    @child_num.setter
    def child_num(self, value):
        self._child_num = value
    @infant_num.setter
    def infant_num(self, value):
        self._infant_num = value
    @family_num.setter
    def family_num(self, value):
        self._family_num = value
    @pick_up_location.setter
    def pick_up_location(self, value):
        self._pick_up_location = value
    @note.setter
    def note(self, value):
        self._note = value
    @payment_id.setter
    def payment_id(self, value):
        self._payment_id = value
    @booking_status.setter
    def booking_status(self, value):
        self._booking_status = value

    # @staticmethod
    # def add_inquiry(tour_id, customer_id, tour_date):
    #     query = """
    #         INSERT INTO Bookings (TourID, CustomerID, TourDate, BookingStatus)
    #         VALUES (%s, %s, %s, 'Inquiry')
    #     """
    #     return database_execute_lastrowid(query, (tour_id, customer_id, tour_date))
    @staticmethod
    def add_inquiry(**kwargs):
        # Retrieve CustomerID using UserID
        customer_id = Users.get_customer_id_by_user_id(kwargs['user_id'])

        # Check if CustomerID is retrieved
        if not customer_id:
            
            return None

        query = """
            INSERT INTO Bookings (TourID, CustomerID, TourDate, AdultNum, ChildNum, InfantNum, FamilyNum, PickUpLocation, Note, BookingStatus, BookingAccountName, BookingNames)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 'Inquiry', %s, %s)
        """
        values = (kwargs['tour_id'], customer_id['CustomerID'], kwargs['selected_date'], kwargs['adult_num'], kwargs['child_num'], kwargs['infant_num'], kwargs['family_num'], kwargs['pickup_location'], kwargs['note'], kwargs['booking_account_name'], kwargs['booking_names'])

       
        return database_execute_lastrowid(query, values)
    
    @staticmethod
    def get_customer_inquiries(customer_id):
        query = """
            SELECT
            Bookings.BookingID, 
            Bookings.BookingStatus,
            Bookings.TourDate,
            Bookings.AdultNum,
            Bookings.ChildNum,
            Bookings.InfantNum,
            Bookings.FamilyNum,
            Bookings.PickUpLocation,
            Bookings.Note,
            -- Add or remove any columns you need from Bookings
            Tours.TourName AS TourName,
            Tours.TourID,
            Tours.OperatorID,
            Operators.OperatorID,
            Operators.OperatorName AS OperatorName,
            Customers.FirstName,
            Customers.LastName
            
            FROM Bookings
            LEFT JOIN Tours ON Bookings.TourID = Tours.TourID
            LEFT JOIN Operators ON Tours.OperatorID = Operators.OperatorID
            LEFT JOIN Customers ON Bookings.CustomerID = Customers.CustomerID
            WHERE Bookings.CustomerID = %s AND Bookings.BookingStatus = 'Inquiry';

        """

        return database_execute_query_fetchall(query, (customer_id,))
        
    @staticmethod
    def get_all_inquiries():
        query = """
            SELECT Bookings.*, Tours.*, Operators.*,Customers.*
            FROM Bookings
            INNER JOIN Tours ON Bookings.TourID = Tours.TourID
            INNER JOIN Operators ON Tours.OperatorID = Operators.OperatorID
            INNER JOIN Customers ON Bookings.CustomerID = Customers.CustomerID
            WHERE Bookings.BookingStatus = 'Inquiry'
        """
        return database_execute_query_fetchall(query)
    
    @staticmethod
    def get_all_quotes():
        query = """
            SELECT Bookings.*, Tours.TourName, Operators.*, Customers.*,
            (Bookings.AdultQuote * Bookings.AdultNum) +
            (Bookings.ChildQuote * Bookings.ChildNum) +
            (Bookings.InfantQuote * Bookings.InfantNum) +
            (Bookings.FamilyQuote * Bookings.FamilyNum) AS TotalQuote
            FROM Bookings
            INNER JOIN Tours ON Bookings.TourID = Tours.TourID
            INNER JOIN Operators ON Tours.OperatorID = Operators.OperatorID
            INNER JOIN Customers ON Bookings.CustomerID = Customers.CustomerID
            WHERE Bookings.BookingStatus = 'Quote'
        """
        return database_execute_query_fetchall(query)




    @staticmethod
    def get_agent_quotes(agent_id):
        query = """
            SELECT Bookings.*, Tours.TourName
            FROM Bookings
            INNER JOIN Tours ON Bookings.TourID = Tours.TourID
            WHERE Bookings.AgentID = %s AND Bookings.BookingStatus = 'Quote'
        """
        return database_execute_query_fetchall(query, (agent_id,))
    
    
    @staticmethod
    def update_status(booking_id, new_status):
        query = "UPDATE Bookings SET BookingStatus = %s WHERE BookingID = %s"
        return database_execute_action(query, (new_status, booking_id))

    
    @staticmethod
    def insert_or_update_quote(booking_id, adult_quote, child_quote, infant_quote, family_quote, notes):
        # Check if a quote already exists
        existing_quote_query = "SELECT * FROM Bookings WHERE BookingID = %s AND BookingStatus = 'Quote'"
        existing_quote = database_execute_query_fetchone(existing_quote_query, (booking_id,))
        
        if existing_quote:
            # Update existing quote
            
            update_query = """
                UPDATE Bookings
                SET AdultQuote = %s, ChildQuote = %s, InfantQuote = %s, FamilyQuote = %s, Note = %s
                WHERE BookingID = %s
            """
            return database_execute_action(update_query, (adult_quote, child_quote, infant_quote, family_quote, notes, booking_id))
        else:
            # Insert new quote
            insert_query = """
                UPDATE Bookings
                SET AdultQuote = %s, ChildQuote = %s, InfantQuote = %s, FamilyQuote = %s, Note = %s, BookingStatus = 'Quote'
                WHERE BookingID = %s
            """
            return database_execute_action(insert_query, (adult_quote, child_quote, infant_quote, family_quote, notes, booking_id))

      

    @staticmethod
    def get_quote_by_id(booking_id):
        query = """
            SELECT Bookings.*, Customers.Email AS CustomerEmail, Customers.FirstName, Customers.LastName, Tours.TourName
            FROM Bookings
            INNER JOIN Customers ON Bookings.CustomerID = Customers.CustomerID
            INNER JOIN Tours ON Bookings.TourID = Tours.TourID
            
            WHERE Bookings.BookingID = %s AND Bookings.BookingStatus = 'Quote'
        """
        result=database_execute_query_fetchone(query, (booking_id,))
        
        return result


    @staticmethod
    def get_inquiry_details(booking_id):
       
        query = """
            SELECT * FROM Bookings
            INNER JOIN Tours ON Bookings.TourID = Tours.TourID
            INNER JOIN Customers ON Bookings.CustomerID = Customers.CustomerID
            INNER JOIN Operators ON Tours.OperatorID = Operators.OperatorID
            WHERE BookingID = %s
        """
        return database_execute_query_fetchone(query, (booking_id,))
    
    
    # @staticmethod
    # def get_bookings_by_user(user_id):
    #     query = """
    #         SELECT * FROM Bookings
    #         WHERE CustomerID = %s
    #     """
    #     return database_execute_query_fetchall(query, (user_id,))
    
    @staticmethod
    def get_all_bookings_except_inquiry_quote():
        query = """
            SELECT 
                Bookings.*, 
                Tours.TourName, 
                Customers.FirstName, 
                Customers.LastName, 
                Operators.OperatorName,
                (Bookings.AdultNum * Bookings.AdultQuote + 
                Bookings.ChildNum * Bookings.ChildQuote + 
                Bookings.InfantNum * Bookings.InfantQuote + 
                Bookings.FamilyNum * Bookings.FamilyQuote) AS TotalQuote
            FROM Bookings
            INNER JOIN Tours ON Bookings.TourID = Tours.TourID
            INNER JOIN Customers ON Bookings.CustomerID = Customers.CustomerID
            INNER JOIN Operators ON Tours.OperatorID = Operators.OperatorID
            WHERE Bookings.BookingStatus NOT IN ('Inquiry', 'Quote')
        """
        return database_execute_query_fetchall(query)

    # Method for agent bookings
    @staticmethod
    def get_agent_bookings(agent_id):
        query = """
            SELECT Bookings.*, Tours.*, Customers.*, Operators.*
            FROM Bookings
            INNER JOIN Tours ON Bookings.TourID = Tours.TourID
            INNER JOIN Operators ON Tours.OperatorID = Operators.OperatorID
            INNER JOIN Customers ON Bookings.CustomerID = Customers.CustomerID
            WHERE Bookings.AgentID = %s
        """
        return database_execute_query_fetchall(query, (agent_id,))

    # Method for customer bookings
    @staticmethod
    def get_customer_bookings(customer_id):
        query = """
            SELECT Bookings.*, Tours.*, Customers.*,Operators.*
            FROM Bookings
            INNER JOIN Tours ON Bookings.TourID = Tours.TourID
            INNER JOIN Customers ON Bookings.CustomerID = Customers.CustomerID
            INNER JOIN Operators ON Tours.OperatorID = Operators.OperatorID
            WHERE Bookings.CustomerID = %s
        """
        return database_execute_query_fetchall(query, (customer_id,))
    
    @staticmethod
    def update_booking(booking_id, tour_date, adult_num, child_num, infant_num, family_num, pick_up_location, note, booking_account_name, booking_names, confirmation_num, adult_quote, child_quote, infant_quote, family_quote):
        query = """
            UPDATE Bookings
            SET TourDate = %s, AdultNum = %s, ChildNum = %s, InfantNum = %s, FamilyNum = %s, 
                PickUpLocation = %s, Note = %s, BookingAccountName = %s, BookingNames = %s, 
                ConfirmationNum = %s, AdultQuote = %s, ChildQuote = %s, InfantQuote = %s, FamilyQuote = %s
            WHERE BookingID = %s
        """
        return database_execute_action(query, (tour_date, adult_num, child_num, infant_num, family_num, pick_up_location, note, booking_account_name, booking_names, confirmation_num, adult_quote, child_quote, infant_quote, family_quote, booking_id))
    
    @staticmethod
    def update_quote(booking_id, tour_date, adult_num, child_num, infant_num, family_num, adult_quote, child_quote, infant_quote, family_quote, pickup_location, note):
        query = """
            UPDATE Bookings
            SET TourDate = %s, AdultNum = %s, ChildNum = %s, InfantNum = %s, FamilyNum = %s, 
                AdultQuote = %s, ChildQuote = %s, InfantQuote = %s, FamilyQuote = %s, 
                PickUpLocation = %s, Note = %s
            WHERE BookingID = %s
        """
        return database_execute_action(query, (tour_date, adult_num, child_num, infant_num, family_num, adult_quote, child_quote, infant_quote, family_quote, pickup_location, note, booking_id))
   


    @staticmethod
    def get_booking_by_id(booking_id):
        query = """
        SELECT Bookings.*, Tours.TourName, Operators.*, Customers.*,
            (Bookings.AdultQuote * Bookings.AdultNum) +
            (Bookings.ChildQuote * Bookings.ChildNum) +
            (Bookings.InfantQuote * Bookings.InfantNum) +
            (Bookings.FamilyQuote * Bookings.FamilyNum) AS TotalQuote,
            ((Bookings.AdultQuote * Bookings.AdultNum) +
            (Bookings.ChildQuote * Bookings.ChildNum) +
            (Bookings.InfantQuote * Bookings.InfantNum) +
            (Bookings.FamilyQuote * Bookings.FamilyNum)) * Tours.CommissionRate / 100 AS TotalCommission
            FROM Bookings
            INNER JOIN Tours ON Bookings.TourID = Tours.TourID
            INNER JOIN Operators ON Tours.OperatorID = Operators.OperatorID
            INNER JOIN Customers ON Bookings.CustomerID = Customers.CustomerID
            WHERE Bookings.BookingID = %s AND (Bookings.BookingStatus != 'Quote' OR Bookings.BookingStatus != 'Inquiry')   
            """
        return database_execute_query_fetchone(query, (booking_id,))
    
    @staticmethod
    def add_booking(customer_id, tour_id, tour_date, adult_num, child_num, infant_num, family_num, pickup_location, note):
        query = """
            INSERT INTO Bookings (CustomerID, TourID, TourDate, AdultNum, ChildNum, InfantNum, FamilyNum, PickUpLocation, Note)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (customer_id, tour_id, tour_date, adult_num, child_num, infant_num, family_num, pickup_location, note)
        
        return database_execute_lastrowid(query, values)
    
    @staticmethod
    def get_customer_inquiries(customer_id):
        query = """
            SELECT * FROM bookings
            WHERE CustomerID = %s AND BookingStatus = 'Inquiry'
        """
        return database_execute_query_fetchall(query, (customer_id,))
        
    

    
