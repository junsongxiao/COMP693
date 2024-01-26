from model.bookings import Bookings

class BookingController:
    # @staticmethod
    # def add_inquiry(tour_id, customer_id, tour_date):
    #     return Bookings.add_inquiry(tour_id, customer_id, tour_date)
    @staticmethod
    def add_inquiry(**kwargs):
        return Bookings.add_inquiry(**kwargs)
    # @staticmethod
    # def get_agent_inquiries(agent_id):
    #     return Bookings.get_agent_inquiries(agent_id)
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
    @staticmethod
    def get_agent_inquiries(agent_id):
        return Bookings.get_agent_inquiries(agent_id)

    @staticmethod
    def get_agent_quotes(agent_id):
        return Bookings.get_agent_quotes(agent_id)

    @staticmethod
    def update_booking_status(booking_id, new_status):
        return Bookings.update_booking_status(booking_id, new_status)
    
    @staticmethod
    def process_inquiry_details(booking_id):
        return Bookings.get_inquiry_details(booking_id)

    @staticmethod
    def process_update_quoted_prices_and_notes(booking_id, quoted_prices, notes):
        return Bookings.update_quoted_prices_and_notes(booking_id, quoted_prices, notes)