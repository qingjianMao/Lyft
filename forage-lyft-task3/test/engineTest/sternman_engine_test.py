import unittest
from engine.sternman_engine import SternmanEngine

class testSternmanEngine(unittest.TestCase):
    def testStEngineTrue(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())
    
    def testStEngineFalse(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())