

class Payments:
    def __init__(self, amount, payment_status):
        self._payment_id = None
        self._amount = amount
        self._payment_status = payment_status

    @property
    def payment_id(self):
        return self._payment_id
    @property
    def amount(self):
        return self._amount
    @property
    def payment_status(self):
        return self._payment_status
    
    @payment_id.setter
    def payment_id(self, value):
        self._payment_id = value
    @amount.setter
    def amount(self, value):
        self._amount = value
    @payment_status.setter
    def payment_status(self, value):
        self._payment_status = value
