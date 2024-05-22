from src.simulator import Simulator
import unittest


class TestSimulator(unittest.TestCase):
    def test_usage(self):
        Simulator(3, 5)


if __name__ == "__main__":
    unittest.main()



