from datetime import datetime


class Train:
    _destination = None
    _number = None
    _departure_time = None

    def __init__(self, destination, number, departure_time):
        self._destination = destination
        self._number = number
        self._departure_time = departure_time

    def print_if_matching(self, number):
        if self._number == number:
            print(f"Destination: {self._destination}")
            print(f"Number: {self._number}")
            print(f"Departure time: {self._departure_time}")


cur_train = Train("Томск 1", 9, datetime(2025, 6, 1, 12, 30))

cur_train.print_if_matching(int(input("Enter desired train's number: ")))