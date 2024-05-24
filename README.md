### Description
This project simulates a lunar Helium-3 mining operation using the simpy library. The simulation manages and tracks the efficiency of mining trucks and unload stations over a continuous 72-hour operation. Below is a brief overview of the main components and their functionalities:

- MiningUnloadStation: This class represents the unload stations where mining trucks unload the mined Helium-3. It ensures that the number of unload stations is within the allowed range.

- MiningTruck: This class simulates a mining truck's operations, including mining, traveling to an unload station, and unloading Helium-3. It tracks the total mining and unloading times for each truck. The class also supports a debug mode, allowing for fixed durations during testing.

- Simulator: This class sets up and runs the simulation. It initializes the environment, creates the specified number of mining trucks and unload stations, and runs the simulation for the given duration. It also collects and logs statistics on the total mining and unloading times for each truck.

Key Features:
- Dynamic Simulation: The mining and travel durations are randomly generated within specified ranges, simulating realistic operations.
- Logging: The simulation logs detailed information about the activities of each truck.
- Debug Mode: Allows fixed durations for consistent testing and debugging.
- Statistics Collection: Collects and returns statistics on the performance of each truck.
This setup provides a flexible and extensible framework for simulating and analyzing the efficiency of mining operations in a controlled environment.
## Setup

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)

### Steps

1. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    ```

2. **Activate the virtual environment:**

    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

3. **Upgrade pip:**

    ```bash
    pip install --upgrade pip
    ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Example Script

After setting up the environment, you can run the example script to see the simulation in action:

```
python -m examples.example01
```

## Running Tests
To run the tests using pytest, ensure the virtual environment is activated and run:

```
pytest
```
This command will discover and run all the tests in the tests directory.



