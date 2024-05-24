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



