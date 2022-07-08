from Tires.tire import Tire

class OctoprimeTires(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    
    def needs_service(self):
        sum(self.tire_wear) >= 3.0