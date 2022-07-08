import unittest
from battery.nubbin_battery import NubbinBattery
from datetime import date

class nubbinBatteryTest(unittest.TestCase):
    def testNbBatteryTrue(self):
        current_date = date.fromisoformat("2022-05-15")
        last_service_date = date.fromisoformat("2018-05-14")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
    
    def testNbBatteryFalse(self):
        current_date = date.fromisoformat("2022-05-15")
        last_service_date = date.fromisoformat("2018-05-15")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())