class Calculation:
    _calculation_line = ""

    def set_calculation_line(self, new_line):
        self._calculation_line = new_line

    def set_last_symbol_calculation_line(self, symbol):
        self._calculation_line += symbol

    def get_calculation_line(self):
        return self._calculation_line

    def get_last_symbol(self):
        return self._calculation_line[-1]

    def delete_last_symbol(self):
        self._calculation_line = self._calculation_line[:-1]


cur_calculation = Calculation()
cur_calculation.set_calculation_line(input("Enter calculation line: "))
cur_calculation.set_last_symbol_calculation_line(input("Enter new last symbol: ")[0])
print(f"Current calculation line: {cur_calculation.get_calculation_line()}")
print(f"Current last symbol: {cur_calculation.get_last_symbol()}")
cur_calculation.delete_last_symbol()
print(f"Current calculation line: {cur_calculation.get_calculation_line()}")