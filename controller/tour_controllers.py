from model.tours import Tours

class TourController:
    @staticmethod
    def get_all_tours():
        return Tours.get_all_tours()
    
    @staticmethod
    def get_tour_details(tour_id):
        return Tours.get_tour_details(tour_id)

    @staticmethod
    def update_tour(tour_id, tour_name, city, region, description, adult_price, child_price, 
                    infant_price, family_price, tour_time, report_time, terms, reporting_add, 
                    tour_add, commission_rate):
        return Tours.update_tour(tour_id, tour_name, city, region, description, adult_price, 
                                     child_price, infant_price, family_price, tour_time, 
                                     report_time, terms, reporting_add, tour_add, commission_rate)
    @staticmethod
    def add_tour(operator_id, tour_name, city, region, description, adult_price, child_price, infant_price, family_price, tour_time, report_time, terms, reporting_add, tour_add, commission_rate):
        return Tours.add_tour(operator_id, tour_name, city, region, description, adult_price, child_price, infant_price, family_price, tour_time, report_time, terms, reporting_add, tour_add, commission_rate)
