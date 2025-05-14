class Worker:
    _name = None
    _surname = None
    _rate = None
    _days = None

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def rate(self):
        return self._rate

    @property
    def days(self):
        return self._days

    def __init__(self, name, surname, rate, days):
        self._name = name
        self._surname = surname
        self._rate = rate
        self._days = days

    def get_salary(self):
        return self.rate * self.days


cur_worker = Worker(input("Enter worker's name: "), input("Enter worker's surname: "),
                    int(input("Enter worker's rate: ")), int(input("Enter the number of days worked: ")))
print(f"{cur_worker.name} {cur_worker.surname}'s salary: {cur_worker.get_salary()}")