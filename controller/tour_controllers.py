from model.tours import Tours

class TourController:
    @staticmethod
    def get_all_tours():
        return Tours.get_all_tours()
