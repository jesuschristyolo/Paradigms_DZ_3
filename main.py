from random import randint

#В этой программе человеку не нужно ходить за человека ход осуществляет тоже комп(он ставит ход челоека в первую свобожную клетку)
#Ход человека - это цифра 1
#А компьютер уже в свою очередь ставит ход в абсолютно рандомную клетку на поле
#Ход компьютера - это цифра 2
#
#





class Cell:
    def __init__(self, value=0):
        self.value = value

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)


    def __init__(self):
        self.pole = tuple([Cell() for i in range(3)] for j in range(3))
        self.__is_human_win = False
        self.__is_computer_win = False
        self.__is_draw = False

    @property
    def is_human_win(self):
        return self.__is_human_win

    @is_human_win.setter
    def is_human_win(self, value):
        self.__is_human_win = value

    @property
    def is_computer_win(self):
        return self.__is_computer_win

    @is_computer_win.setter
    def is_computer_win(self, value):
        self.__is_computer_win = value

    @property
    def is_draw(self):
        return self.__is_draw

    @is_draw.setter
    def is_draw(self, value):
        self.__is_draw = value


    def init(self):
        self.pole = tuple([Cell() for i in range(3)] for j in range(3))
        self.__is_human_win = False
        self.is_computer_win = False
        self.is_draw = False


    def show(self):
        print("=" * 20)
        for i in self.pole:
            for j in i:
                print(f" {j.value} |", end="")
            print()
            print("---|" * 3)
        print("=" * 20)

    def human_go(self):
        flag = False
        for i in self.pole:
            for j in i:
                if j.value == 0:
                    if flag == False:
                        j.value = 1
                        flag = True
        self.check_for_winner()

    def computer_go(self):
        boolean = True
        while boolean:
            hod = self.pole[randint(0, 2)][randint(0, 2)]
            if hod.value == 0:
                hod.value = 2
                boolean = False
        self.check_for_winner()

    def check_for_winner(self):
        for row in self.pole:
            if all(element.value == 1 for element in row):
                self.is_human_win = True
            if all(element.value == 2 for element in row):
                self.is_computer_win = True

        num_columns = len(self.pole[0])
        for col_index in range(num_columns):
            if all(row[col_index].value == 1 for row in self.pole):
                self.is_human_win = True
            if all(row[col_index].value == 2 for row in self.pole):
                self.is_computer_win = True

        if all(
            self.pole[i][i].value == 1 for i in range(min(len(self.pole), len(self.pole[0])))):
            self.is_human_win = True

        if all(
            self.pole[i][i].value == 2 for i in range(min(len(self.pole), len(self.pole[0])))):
            self.is_computer_win = True

        if all(
            self.pole[i][len(self.pole) - 1 - i].value == 1 for i in range(min(len(self.pole), len(self.pole[0])))):
            self.is_human_win = True

        if all(
            self.pole[i][len(self.pole) - 1 - i].value == 2 for i in range(min(len(self.pole), len(self.pole[0])))):
            self.is_computer_win = True


        for row in self.pole:
            if all(element.value == 1 or element.value == 2 for element in row):
                self.is_draw = True
            else:
                self.is_draw = False


        if self.is_computer_win or self.is_human_win or self.is_draw:
            return False
        else:
            return True

    def __bool__(self):
        if self.is_computer_win or self.is_human_win or self.is_draw:
            return False
        else:
            boolean = False
            for row in self.pole:
                if any(element.value == 0 for element in row):
                    boolean = True
            return boolean


    def __getitem__(self, item):
        try:
            if isinstance(self.pole[item[0]][item[1]], Cell):
                return self.pole[item[0]][item[1]].value
            else:
                return self.pole[item[0]][item[1]]
        except:
            raise IndexError('некорректно указанные индексы')

    def __setitem__(self, key, value):
        try:
            self.pole[key[0]][key[1]] = Cell(value = value)
        except:
            raise IndexError('некорректно указанные индексы')
        self.check_for_winner()




game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()
    print(game.is_human_win)
    print(bool(game))

    step_game += 1

game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!(вы победили)")
elif game.is_computer_win:
    print("Все получится, со временем(победил комп)")
else:
    print("Ничья.")






