import simpy
import random
import logging

# Configure logging
# Not currently saving logs
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class MiningUnloadStation:
    def __init__(self, env, number_of_stations):
        self.env = env
        self.stations = simpy.Resource(env, capacity=number_of_stations)

class MiningTruck:
    def __init__(self, env, name, unload_station, debug=False):
        self.env = env
        self.name = name
        self.unload_station = unload_station
        self.total_mining_time = 0
        self.total_unload_time = 0
        self.action = env.process(self.run())

        # For Testing
        self.debug = debug
        self.miningDuration = 1

    def run(self):
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

    def getMiningDuration(self, min=0, max=5):
        if not self.debug:
            return random.randint(min, max)
        else:
            return self.miningDuration

    def setMiningDuration(self, value):
        if 0 < value:
            self.miningDuration = value

class Simulator:
    def __init__(self, m, n, duration=4320, *, debug=False):
        self.env = simpy.Environment()
        self.number_of_unload_stations = m
        self.number_of_trucks = n
        self.simulation_duration = duration

        self.debug = debug

    def setup(self):
        self.unload_station = MiningUnloadStation(self.env, self.number_of_unload_stations)
        self.trucks = [MiningTruck(self.env, f'Truck {i}', self.unload_station, debug=self.debug) for i in range(self.number_of_trucks)]

    def run(self):
        self.env.run(until=self.simulation_duration)

    def collect_statistics(self):
        truck_stats = {}
        for truck in self.trucks:
            logging.info(f'{truck.name} mined for {truck.total_mining_time} hours and spent {truck.total_unload_time} minutes unloading.')
            truck_stats[truck.name] = truck.total_unload_time
        return truck_stats

    def start(self):
        logging.info('Lunar Helium-3 mining operation simulation')
        self.setup()
        self.run()
        return self.collect_statistics()

