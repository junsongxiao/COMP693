




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

    
