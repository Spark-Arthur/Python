class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num - other.num > 0:
            return self.num - other.num
        else:
            return 'Error'

    def __mul__(self, other):
        return self.num * other.num

    def __floordiv__(self, other):
        return round(self.num / other.num)

    def make_order(self, other):
        star = ''
        for i in range(self.num // other):
            star += str('*' * other) + '\n'
        star += str('*' * (self.num % other))
        return star

cell_1 = Cell(44)
cell_2 = Cell(22)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(20))

