import unittest
from engine.capulet_engine import CapuletEngine

class testCapuletengine(unittest.TestCase):
    def testCpEngineTrue(self):
        engine = CapuletEngine(30001, 0)
        self.assertTrue(engine.needs_service())
    
    def testCpEngineFalse(self):
        engine = CapuletEngine(30000, 0)
        self.assertFalse(engine.needs_service())
