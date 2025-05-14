class TwoProperties:
    _a = None
    _b = None

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    def __init__(self, a="A placeholder", b="B placeholder"):
        self._a = a
        self._b = b

    def __del__(self):
        print(f"TwoProperties object (with A: {self.a}, B: {self.b}) has been destroyed")


two_props = TwoProperties(input("Enter A: "), input("Enter B: "))
print(two_props.a)
print(two_props.b)
del two_props

two_props = TwoProperties()
del two_props