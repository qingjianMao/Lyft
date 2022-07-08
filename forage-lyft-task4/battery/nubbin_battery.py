from battery.battery import Battery
from battery.add_year import addYear

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        return addYear(self.last_service_date, 4) <= self.current_date