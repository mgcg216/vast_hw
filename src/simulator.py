import simpy
import random

class MiningUnloadStation:
    def __init__(self, env, number_of_stations):
        self.env = env
        self.stations = simpy.Resource(env, capacity=number_of_stations)

class MiningTruck:
    def __init__(self, env, name, unload_station):
        self.env = env
        self.name = name
        self.unload_station = unload_station
        self.total_mining_time = 0
        self.total_unload_time = 0
        self.action = env.process(self.run())

    def run(self):
        while True:
            # Mine for 1-5 hours
            mining_duration = random.randint(1, 5)
            self.total_mining_time += mining_duration
            print(f'{self.name} starts mining at {self.env.now} for {mining_duration} hours')
            yield self.env.timeout(mining_duration * 60)  # convert hours to minutes

            # Travel to unload station
            travel_duration = 30  # 30 minutes travel time
            print(f'{self.name} travels to unload station at {self.env.now}')
            yield self.env.timeout(travel_duration)

            # Unload Helium-3
            with self.unload_station.stations.request() as request:
                yield request
                unload_duration = 5  # 5 minutes to unload
                self.total_unload_time += unload_duration
                print(f'{self.name} starts unloading at {self.env.now}')
                yield self.env.timeout(unload_duration)
                print(f'{self.name} finishes unloading at {self.env.now}')

class Simulator:
    def __init__(self, m, n):
        # Setup and start the simulation
        print('Lunar Helium-3 mining operation simulation')
        env = simpy.Environment()
        number_of_unload_stations = m  # Define the number of unload stations
        unload_station = MiningUnloadStation(env, number_of_unload_stations)  # Initialize the unload stations

        # Create multiple mining trucks
        number_of_trucks = n
        trucks = [MiningTruck(env, f'Truck {i}', unload_station) for i in range(number_of_trucks)]

        # Run the simulation for 72 hours (4320 minutes)
        env.run(until=4320)

        # Collect and print statistics
        for truck in trucks:
            print(f'{truck.name} mined for {truck.total_mining_time} hours and spent {truck.total_unload_time} minutes unloading.')


if __name__ == "__main__":
    Simulator(3, 5)

