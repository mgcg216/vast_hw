from src.simulator import Simulator

# Example usage:
if __name__ == "__main__":
    try:
        simulator = Simulator(m=3, n=5, duration=4320, debug=False)
        stats = simulator.start()
        print(stats)
    except ValueError as e:
        print(f"Error: {e}")
