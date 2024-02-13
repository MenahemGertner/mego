class Taxi:
    def __init__(self, taxi_id, driver_name, num_pass=4):
        self._taxi_id = taxi_id
        self._driver_name = driver_name
        self._num_pass = num_pass
        self.available = True

    def is_available(self):
        return self.available

    def is_busy(self):
        self.available = False

    @property
    def driver_name(self):
        return self._driver_name

    @driver_name.setter
    def driver_name(self, name):
        self._driver_name = name

    @property
    def taxi_id(self):
        return self._taxi_id

    @taxi_id.setter
    def taxi_id(self, id):
        self._taxi_id = id

    def get_num_pass(self):
        return self._num_pass

    def set_num_pass(self, num_p):
        self._num_pass = num_p


class Station:
    def __init__(self, station_name):
        self.station_name = station_name
        self.taxis = []

    def add_taxi(self, taxi_id, driver_name, num_pass=4):
        if len(self.taxis) < 80:
            self.taxis.append(Taxi(taxi_id, driver_name, num_pass))
        else:
            print("The station is full!")

    def get_taxi(self, num):
        space = 100
        suitable_taxi = None
        for taxi in self.taxis:
            if taxi.is_available() and num <= taxi.get_num_pass() and space > taxi.get_num_pass() - num:
                space = taxi.get_num_pass() - num
                suitable_taxi = taxi
        if suitable_taxi is not None:
            suitable_taxi.is_busy()
            return suitable_taxi


station = Station("hagivha")
station.add_taxi(6257, "avi")
station.add_taxi(6467, "ariel", 3)
station.add_taxi(8757, "moshe", 5)
station.add_taxi(5464, "shlomo")
while True:
    passenger = station.get_taxi(int(input("\nEnter number of passengers: ")))
    if passenger:
        print(f"your driver is: {passenger.driver_name}")
    else:
        print("There is no taxi available")
