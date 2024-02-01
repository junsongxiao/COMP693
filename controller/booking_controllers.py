from model.bookings import Bookings

class BookingController:

    @staticmethod
    def add_inquiry(**kwargs):
        return Bookings.add_inquiry(**kwargs)
    # @staticmethod
    # def get_agent_inquiries(agent_id):
    #     return Bookings.get_agent_inquiries(agent_id)
    @staticmethod
    def get_all_inquiries():
        return Bookings.get_all_inquiries()
    
    @staticmethod
    def get_bookings_by_user(user_id):
        return Bookings.get_bookings_by_user(user_id)
    # @staticmethod
    # def update_inquiry_status(booking_id, new_status):
    #     return Bookings.update_inquiry_status(booking_id, new_status)
    # @staticmethod
    # def quote_inquiry(booking_id, quoted_prices, note):
    #     # Logic to update the quoted prices and note in the booking
    #     Bookings.quote_inquiry(booking_id, quoted_prices, note)

    @staticmethod
    def get_inquiry_details(booking_id):
        # Logic to retrieve a single inquiry's details
        return Bookings.get_inquiry_details(booking_id)
    
    # @staticmethod
    # def update_quoted_prices(booking_id, quoted_prices):
    #         return Bookings.update_quoted_prices(booking_id, **quoted_prices)
    # @staticmethod
    # def get_agent_inquiries(agent_id):
    #     return Bookings.get_agent_inquiries(agent_id)
    
    @staticmethod
    def get_all_quotes():
        return Bookings.get_all_quotes()


    @staticmethod
    def get_agent_quotes(agent_id):
        return Bookings.get_agent_quotes(agent_id)

    # @staticmethod
    # def update_booking_status(booking_id, new_status):
    #     return Bookings.update_booking_status(booking_id, new_status)
    
    @staticmethod
    def process_inquiry_details(booking_id):
        return Bookings.get_inquiry_details(booking_id)

   

    # @staticmethod
    # def process_update_quoted_prices_and_notes(booking_id, quoted_adult_price, quoted_child_price, quoted_infant_price, quoted_family_price, notes):
    #     return Bookings.update_quoted_prices_and_notes(booking_id, quoted_adult_price, quoted_child_price, quoted_infant_price, quoted_family_price, notes)
    @staticmethod
    def process_quote(booking_id, adult_quote, child_quote, infant_quote, family_quote, notes):
        return Bookings.insert_or_update_quote(booking_id, adult_quote, child_quote, infant_quote, family_quote, notes)
    
    @staticmethod
    def get_quote_details(booking_id):
        return Bookings.get_quote_by_id(booking_id)
    
    @staticmethod
    def update_status(booking_id, new_status):
        return Bookings.update_status(booking_id, new_status)
    
    @staticmethod
    def get_all_bookings_except_inquiry_quote():
        return Bookings.get_all_bookings_except_inquiry_quote()
    
    
    @staticmethod
    def get_agent_bookings(agent_id):
        return Bookings.get_agent_bookings(agent_id)

    @staticmethod
    def get_customer_bookings(customer_id):
        return Bookings.get_customer_bookings(customer_id)
    
    @staticmethod
    def update_booking(booking_id, tour_date, adult_num, child_num, infant_num, family_num, pick_up_location, note, booking_account_name, booking_names, confirmation_num, adult_quote, child_quote, infant_quote, family_quote):
        return Bookings.update_booking(booking_id, tour_date, adult_num, child_num, infant_num, family_num, pick_up_location, note, booking_account_name, booking_names, confirmation_num, adult_quote, child_quote, infant_quote, family_quote)
    @staticmethod
    def get_booking_details(booking_id):
        return Bookings.get_booking_by_id(booking_id)
    @staticmethod
    def add_booking(customer_id, tour_id, tour_date, adult_num, child_num, infant_num, family_num, pickup_location, note):
        return Bookings.add_booking(customer_id, tour_id, tour_date, adult_num, child_num, infant_num, family_num, pickup_location, note)
    



