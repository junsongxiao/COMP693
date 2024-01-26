from model.db import database_execute_query_fetchall



class Tours:
    def __init__(self, operator_id, tour_name, city, region, tour_description, adult_price, child_price, infant_price, family_price, tour_time, report_time, terms, reporting_add, tour_add, commission_rate):
        self._tour_id = None
        self._operator_id = operator_id
        self._tour_name = tour_name
        self._city = city
        self._region = region
        self._tour_description = tour_description
        self._adult_price = adult_price
        self._child_price = child_price
        self._infant_price = infant_price
        self._family_price = family_price
        self._tour_time = tour_time
        self._report_time = report_time
        self._terms = terms
        self._reporting_add = reporting_add
        self._tour_add = tour_add
        self._commission_rate = commission_rate
    ###getters
    @property
    def tour_id(self):
        return self._tour_id
    @property
    def operator_id(self):
        return self._operator_id
    @property
    def tour_name(self):
        return self._tour_name
    @property
    def city(self):
        return self._city
    @property
    def region(self):
        return self._region
    @property
    def tour_description(self):
        return self._tour_description
    @property
    def adult_price(self):
        return self._adult_price
    @property
    def child_price(self):
        return self._child_price
    @property
    def infant_price(self):
        return self._infant_price
    @property
    def family_price(self):
        return self._family_price
    @property
    def tour_time(self):
        return self._tour_time
    @property
    def report_time(self):
        return self._report_time
    @property
    def terms(self):
        return self._terms
    @property
    def reporting_add(self):
        return self._reporting_add
    @property
    def tour_add(self):
        return self._tour_add
    @property
    def commission_rate(self):
        return self._commission_rate
    ###setters
    @tour_id.setter
    def tour_id(self, value):
        self._tour_id = value
    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @tour_name.setter
    def tour_name(self, value):
        self._tour_name = value
    @city.setter
    def city(self, value):
        self._city = value
    @region.setter
    def region(self, value):
        self._region = value
    @tour_description.setter
    def tour_description(self, value):
        self._tour_description = value
    @adult_price.setter
    def adult_price(self, value):
        self._adult_price = value
    @child_price.setter
    def child_price(self, value):
        self._child_price = value
    @infant_price.setter
    def infant_price(self, value):
        self._infant_price = value
    @family_price.setter
    def family_price(self, value):
        self._family_price = value
    @tour_time.setter
    def tour_time(self, value):
        self._tour_time = value
    @report_time.setter
    def report_time(self, value):
        self._report_time = value
    @terms.setter
    def terms(self, value):
        self._terms = value
    @reporting_add.setter
    def reporting_add(self, value):
        self._reporting_add = value
    @tour_add.setter
    def tour_add(self, value):
        self._tour_add = value
    @commission_rate.setter
    def commission_rate(self, value):
        self._commission_rate = value


    @staticmethod
    def get_all_tours():
        query = "SELECT * FROM Tours"
        return database_execute_query_fetchall(query)

    