class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'
    def get_total_income(self):
        self.sum = 0
        for i in self._income:
            self.sum += self._income[i]
        return self.sum

position = Position('Arthur', 'Tsoktoev', 'Proger', 150000, 50000)

print(position.get_full_name())
print(position.get_total_income())