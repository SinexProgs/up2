class Worker:
    _name = None
    _surname = None
    _rate = None
    _days = None

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_rate(self):
        return self._rate

    def get_days(self):
        return self._days

    def __init__(self, name, surname, rate, days):
        self._name = name
        self._surname = surname
        self._rate = rate
        self._days = days

    def get_salary(self):
        return self.get_rate() * self.get_days()


cur_worker = Worker(input("Enter worker's name: "), input("Enter worker's surname: "),
                    int(input("Enter worker's rate: ")), int(input("Enter the number of days worked: ")))
print(f"{cur_worker.get_name()} {cur_worker.get_surname()}'s salary: {cur_worker.get_salary()}")