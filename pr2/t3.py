class TwoNumbers:
    _a : int = 0
    _b : int = 0

    def print(self):
        print(f"A: {self._a}, B: {self._b}")

    def set(self, a, b):
        self._a = a
        self._b = b

    def sum(self):
        return self._a + self._b

    def max(self):
        return max(self._a, self._b)


nums = TwoNumbers()
nums.set(int(input("Enter A: ")), int(input("Enter A: ")))
nums.print()
nums_sum = nums.sum()
print(nums_sum)
nums.set(nums_sum, 16)
print(nums.max())