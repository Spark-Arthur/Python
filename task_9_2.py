class Road:
    def __init__(self, length, width):
        self._lenght = length
        self._width = width
    def mass(self):
        return self._lenght * self._width * 25 * 5 / 1000

road = Road(20, 5000)

print(road.mass(), 'т')