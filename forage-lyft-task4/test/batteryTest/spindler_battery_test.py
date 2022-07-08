import unittest
from battery.spindler_battery import SpindlerBattery
from datetime import date

class spindlerBatteryTest(unittest.TestCase):
    def testSpBatteryTrue(self):
        current_date = date.fromisoformat("2022-05-15")
        last_service_date = date.fromisoformat("2019-05-14")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
    
    def testSpBatteryFalse(self):
        current_date = date.fromisoformat("2022-05-15")
        last_service_date = date.fromisoformat("2019-05-14")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
