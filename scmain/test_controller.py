import unittest
from controller.romain import RO_AXIS_T, RO_CONFLICT
from controller.alfns import ALInitialize
from controller.cmdex import ex_EQUAL

class TestRomain(unittest.TestCase):
    def test_constants(self):
        """Test constants in romain.py"""
        self.assertEqual(RO_AXIS_T, 0x0001)
        self.assertEqual(RO_CONFLICT, 0x88)

class TestAlFns(unittest.TestCase):
    def test_al_initialize(self):
        """Test ALInitialize function in alfns.py"""
        result = ALInitialize(1, 0)  # Arguments: config flag, emulator mode
        self.assertEqual(result, 0)  # Expected simulated success (0)

class TestCmdEx(unittest.TestCase):
    def test_ex_equal(self):
        """Test ex_EQUAL function in cmdex.py"""
        result = ex_EQUAL("R10 = R11 + R12")  # Simulated input
        self.assertEqual(result, 0)  # Expected simulated success (0)

if __name__ == "__main__":
    unittest.main()
