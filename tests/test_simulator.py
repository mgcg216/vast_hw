from src.simulator import Simulator
from src.simulator import MAX_TRUCKS, MAX_STATIONS
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
        expected_data = {'Truck 0': {'total_mining_time': 46, 'total_unload_time': 225}}
        self.assertEqual(simulator.start(), expected_data)

    # Test Setters
    def test_timeout_setters(self):
        simulator = Simulator(1, 1, debug=True)

    # Test invalid inputs
    def test_negative_trucks(self):
        with self.assertRaises(ValueError):
            Simulator(1, -1)

    def test_negative_stations(self):
        with self.assertRaises(ValueError):
            Simulator(-1, 1)

    # Test maximum limits
    def test_max_trucks(self):
        with self.assertRaises(ValueError):
            Simulator(1, MAX_TRUCKS + 1)

    def test_max_stations(self):
        with self.assertRaises(ValueError):
            Simulator(MAX_STATIONS + 1, 1)

    # Test large number of trucks and vehicles
    def test_large_trucks_stations(self):
        try:
            sim = Simulator(10_000, 10_000)
            sim.start()
        except Exception as e:
            self.fail(f"clear raised {type(e).__name__} unexpectedly!")


if __name__ == "__main__":
    unittest.main()

