import simpy
import random
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for max limits wasn't a requirement but made restrictions anyway
MAX_TRUCKS = 1_000_000
MAX_STATIONS = 1_000_000

class MiningUnloadStation:
    def __init__(self, env: simpy.Environment, number_of_stations: int) -> None:
        if number_of_stations < 1 or number_of_stations > MAX_STATIONS:
            raise ValueError(f"Number of unload stations must be between 1 and {MAX_STATIONS}")
        self.env = env
        self.stations = simpy.Resource(env, capacity=number_of_stations)

class MiningTruck:
    def __init__(self, env: simpy.Environment, name: str, unload_station: MiningUnloadStation, debug: bool = False) -> None:
        self.env = env
        self.name = name
        self.unload_station = unload_station
        self.total_mining_time = 0
        self.total_unload_time = 0
        self.action = env.process(self.run())
        self.debug = debug
        self.miningDuration = 1

    def run(self) -> simpy.events.Process:
        while True:
            # Mine for 1-5 hours
            mining_duration = self.getMiningDuration()
            self.total_mining_time += mining_duration
            logging.info(f'{self.name} starts mining at {self.env.now} for {mining_duration} hours')
            yield self.env.timeout(mining_duration * 60)  # convert hours to minutes

            # Travel to unload station
            travel_duration = 30  # 30 minutes travel time
            logging.info(f'{self.name} travels to unload station at {self.env.now}')
            yield self.env.timeout(travel_duration)

            # Unload Helium-3
            with self.unload_station.stations.request() as request:
                yield request
                unload_duration = 5  # 5 minutes to unload
                self.total_unload_time += unload_duration
                logging.info(f'{self.name} starts unloading at {self.env.now}')
                yield self.env.timeout(unload_duration)
                logging.info(f'{self.name} finishes unloading at {self.env.now}')

    def getMiningDuration(self, min: int = 1, max: int = 5) -> int:
        if not self.debug:
            return random.randint(min, max)
        else:
            return self.miningDuration

    def setMiningDuration(self, value: int) -> None:
        if 0 < value:
            self.miningDuration = value

class Simulator:
    def __init__(self, m: int, n: int, duration: int = 4320, *, debug: bool = False) -> None:
        if m < 1 or m > MAX_STATIONS:
            raise ValueError(f"Number of unload stations must be between 1 and {MAX_STATIONS}")
        if n < 1 or n > MAX_TRUCKS:
            raise ValueError(f"Number of trucks must be between 1 and {MAX_TRUCKS}")

        self.env = simpy.Environment()
        self.number_of_unload_stations = m
        self.number_of_trucks = n
        self.simulation_duration = duration
        self.debug = debug

    def setup(self) -> None:
        self.unload_station = MiningUnloadStation(self.env, self.number_of_unload_stations)
        self.trucks = [MiningTruck(self.env, f'Truck {i}', self.unload_station, debug=self.debug) for i in range(self.number_of_trucks)]

    def run(self) -> None:
        self.env.run(until=self.simulation_duration)

    def collect_statistics(self) -> Dict[str, Dict[str, int]]:
        truck_stats = {}
        for truck in self.trucks:
            logging.info(f'{truck.name} mined for {truck.total_mining_time} hours and spent {truck.total_unload_time} minutes unloading.')
            truck_stats[truck.name] = {
                'total_mining_time': truck.total_mining_time,
                'total_unload_time': truck.total_unload_time
            }
        return truck_stats

    def start(self) -> Dict[str, Dict[str, int]]:
        logging.info('Lunar Helium-3 mining operation simulation')
        logging.info(f"Number of Trucks: {self.number_of_trucks}, Number of Stations: {self.number_of_unload_stations}")
        self.setup()
        self.run()
        return self.collect_statistics()

