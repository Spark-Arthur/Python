import random
import turtle
from time import sleep

screen = turtle.getscreen()

class LotoGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer
        self._NUMBERS_COUNT = 90
        MAX_NUMBER = 90

        self._numbers_in_bag = random.sample(range(1, MAX_NUMBER + 1), self._NUMBERS_COUNT)

    def _get_number(self):
        return self._numbers_in_bag.pop()

    def start(self):
        for i in range(self._NUMBERS_COUNT):
            turtle.ht()
            turtle.penup()
            turtle.goto(-70, 100)
            turtle.write(self._player, font=('Helvetica', 18, 'bold'))
            turtle.goto(-70, -50)
            turtle.write(self._computer, font=('Helvetica', 18, 'bold'))
            number = self._get_number()
            turtle.goto(-190, -100)
            turtle.write('Новый бочонок {}, осталось {}'.format(number, len(self._numbers_in_bag)), font=('Helvetica', 18, 'bold'))

            choice = turtle.textinput('Ответ', 'Хотите зачеркуть? y/n:')

            if choice == 'y':
                if not self._player.try_stroke_number(number):
                    screen.clearscreen()
                    turtle.ht()
                    turtle.penup()
                    turtle.goto(-170, 100)
                    turtle.color('red')
                    turtle.write('Игрок проиграл!', font=('Helvetica', 30, 'bold'))
                    sleep(2)
                    break
            elif self._player.has_number(number):
                screen.clearscreen()
                turtle.ht()
                turtle.penup()
                turtle.goto(-170, 100)
                turtle.color('red')
                turtle.write('Игрок проиграл!', font=('Helvetica', 30, 'bold'))
                sleep(2)
                break

            if self._computer.has_number(number):
                self._computer.try_stroke_number(number)
            screen.clearscreen()

class LotoCard:

    def __init__(self, player_type):
        self.player_type = player_type
        self._card = [[],
                      [],
                      []]
        self._MAX_NUMBER = 90
        self._MAX_NUMBERS_IN_CARD = 15
        self._numbers_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5

        self._numbers = random.sample(range(1, self._MAX_NUMBER + 1), self._MAX_NUMBERS_IN_CARD)

        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append('     ')
            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())

        def check_sort_item(item):
            if isinstance(item, int):
                return item
            return random.randint(1, self._MAX_NUMBER)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)

    def has_number(self, number):
        for line in self._card:
            if number in line:
                return True
        return False

    def try_stroke_number(self, number):
        for index, line in enumerate(self._card):
            for num_index, number_in_card in enumerate(line):
                if number == number_in_card:
                    self._card[index][num_index] = '--'
                    self._numbers_stroked += 1
                    if self._numbers_stroked >= self._MAX_NUMBERS_IN_CARD:
                        screen.clearscreen()
                        turtle.ht()
                        turtle.penup()
                        turtle.goto(-170, 100)
                        turtle.color('green')
                        turtle.write('{} победил!'.format(self.player_type), font=('Helvetica', 30, 'bold'))
                        sleep(2)
                        raise Exception
                    return True
        return False

    def __str__(self):
        MAX_FIELD_LENGTH = 3
        header = '\n{}:\n--------------------------------------'.format(self.player_type)
        body = '\n'
        for line in self._card:
            for field in line:
                body += str(field).ljust(MAX_FIELD_LENGTH)
            body += '\n'

        return header + body

human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')

game = LotoGame(human_player, computer_player)
game.start()




