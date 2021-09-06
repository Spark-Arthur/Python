from random import randint

class Matrix:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        self.list_g = []
        self.list_g_sum = []
        for i in range(self.num_1):
            self.list = []
            for i in range(self.num_2):
                self.list.append(randint(-10, 90))

            self.list_g.append(self.list)

        for i in range(len(self.list_g)):
            for ix in range(len(self.list_g[i])):
                self.list_g_sum.append(self.list_g[i][ix])
                ix += 1

    def __str__(self):
        num_list = ''
        for i in range(len(self.list_g)):
            for ix in range(len(self.list_g[i])):
                if ix == self.num_2 - 1:
                    num_list += f'{self.list_g[i][ix]} \n'
                    ix += 1
                else:
                    num_list += f'{self.list_g[i][ix]} '
                    ix += 1
        return f'{num_list}'
    def __add__(self, other):
        answer = ''
        if len(self.list_g) == len(other.list_g):
            for l_1, l_2 in zip(self.list_g, other.list_g):
                if len(l_1) != len(l_2):
                    return 'Problem'
                s_l = [x + y for x, y in zip(l_1, l_2)]
                answer += ' '.join(map(str, s_l)) + '\n'
        else:
            return 'Problem'
        return answer

matrix1 = Matrix(3, 2)
matrix2 = Matrix(3, 3)
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
