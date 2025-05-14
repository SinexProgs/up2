class Counter:
    _value : int = 0

    def __init__(self, value = 0):
        self._value = value

    def increment(self):
        self._value += 1

    def decrement(self):
        self._value -= 1

    @property
    def value(self):
        return self._value


cur_counter = Counter()
for i in range(12):
    cur_counter.increment()
    print(cur_counter.value)

cur_counter = Counter(int(input("Enter counter value: ")))
for i in range(7):
    cur_counter.decrement()
    print(cur_counter.value)