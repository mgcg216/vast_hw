from src.simulator import Simulator
import unittest


class TestSimulator(unittest.TestCase):

    # Test normal usage
    def test_usage(self):
        simulator = Simulator(3, 5)
        simulator.start()

    # Test Debug usage
    def test_debug(self):
        simulator = Simulator(1, 1, debug=True)
        # 1 Truck, 1 Unload spot, 1 hour 
        expected_data = {'Truck 0': 225}
        self.assertEqual(simulator.start(), expected_data)

    # Test negative number of trucks
    def test_negative_trucks(self):
        with self.assertRaises(ValueError):
            simulator = Simulator(1, -1)
            simulator.start()

    # Test negative number of stations
    def test_negative_stations(self):
        simulator = Simulator(-1, 1)
        with self.assertRaises(ValueError):
            simulator.start()

if __name__ == "__main__":
    unittest.main()



