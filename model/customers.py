

class Customers:
    def __init__(self, user_id, first_name, last_name, email, phone, wechat, preferences, notes):
        self._customer_id = None
        self._user_id = user_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._wechat = wechat
        self._preferences = preferences
        self._notes = notes

    ##getters
    @property
    def customer_id(self):
        return self._customer_id
    @property
    def user_id(self):
        return self._user_id
    @property
    def first_name(self):
        return self._first_name
    @property
    def last_name(self):
        return self._last_name
    @property
    def email(self):
        return self._email
    @property
    def phone(self):
        return self._phone
    @property
    def wechat(self):
        return self._wechat
    @property
    def preferences(self):
        return self._preferences
    @property
    def notes(self):
        return self._notes
    
    ##setters
    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @first_name.setter
    def first_name(self, value):
        self._first_name = value
    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    @email.setter
    def email(self, value):
        self._email = value
    @phone.setter
    def phone(self, value):
        self._phone = value
    @wechat.setter
    def wechat(self, value):
        self._wechat = value
    @preferences.setter
    def preferences(self, value):
        self._preferences = value
    @notes.setter
    def notes(self, value):
        self._notes = value

