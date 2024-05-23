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

    

if __name__ == "__main__":
    unittest.main()



