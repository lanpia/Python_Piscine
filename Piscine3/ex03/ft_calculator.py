class calculator:
    def __init__(self, values):
        self.values = values
    def __add__(self, object) -> None:
        self.values = [x + object for x in self.values]
        return print(self.values)
    def __sub__(self, object) -> None:
        self.values = [x - object for x in self.values]
        return print(self.values)
    def __mul__(self, object) -> None:
        self.values = [x * object for x in self.values]
        return print(self.values)
    def __truediv__(self, object) -> None:
        if object == 0:
            print("Division by zero error")
            return
        self.values = [x / object for x in self.values]
        return print(self.values)

v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5