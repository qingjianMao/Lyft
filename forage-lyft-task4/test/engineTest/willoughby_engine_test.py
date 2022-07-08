import unittest
from engine.willoughby_engine import WilloughbyEngine

class testWilloughByEngine(unittest.TestCase):
    def testWbEngineTrue(self):
        engine = WilloughbyEngine(60001, 0)
        self.assertTrue(engine.needs_service())
    
    def testWbEngineFalse(self):
        engine = WilloughbyEngine(60000, 0)
        self.assertFalse(engine.needs_service())