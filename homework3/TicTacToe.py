from typing import List

# крестики-нолики с использованием ООП


class Board:
    """
    Реализация класса игрового поля.
    При создании объекта, конструктор будет инициализировтаь пустые клетки на поле.
    """

    def __init__(self):
        self.cells = [" " for _ in range(9)]

    # метод выводит на экран границы игрового поля
    def display(self):
        print(f"{self.cells[0]} | {self.cells[1]} | {self.cells[2]}")
        print("---------")
        print(f"{self.cells[3]} | {self.cells[4]} | {self.cells[5]}")
        print("---------")
        print(f"{self.cells[6]} | {self.cells[7]} | {self.cells[8]}")


class Player:
    """
    реализация класса под игрока. Конструктор принимает для инициализации объекта имя(name) и знак,(symbol)
    для помечания хода игрока на поле.
    """

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    # метод реализующий ход игрока на игровом поле
    def move(self, board: Board) -> Board:
        while True:
            cell = input(
                f"{self.name}({self.symbol}), введите номер клетки от 1 до 9, для осуществления хода: "
            )
            if cell.isdigit() and 1 <= int(cell) <= 9:
                cell = int(cell) - 1
                # 'game' здесь - это ссылка на объект класса TicTacToe, который мы создали для начала игры
                if board.cells[cell] == " ":
                    board.cells[cell] = self.symbol
                    break
                else:
                    print("Клетка занята. Выберите иное поле.")
            else:
                print(
                    "Неверный ввод данных. Введите повторно номер клетки от 1 до 9, для осуществления хода."
                )


class TicTacToe:
    """
    реализация класса игровой сессии. Конструктор принимает для инициализации игроков их имена, затем создает пустые клетки для поля,
    посредством создания экземпляра класса Board.
    """

    def __init__(self, player1_name, player2_name):
        self.board = Board()
        self.player1 = Player(player1_name, "X")
        self.player2 = Player(player2_name, "O")

    # метод play активирует игровую сессию, путем вызова методов создания игрового поля,
    # осуществелия хода и проверок на победу\ничью
    def play(self):
        # создания активного на текущий ход игрока
        current_player = self.player1
        while True:
            self.board.display()
            current_player.move(self.board)
            if self.check_win(current_player):
                print(f"Игрок {current_player.name}({current_player.symbol}) победил!")
                self.board.display()
                break
            elif self.check_draw():
                print("Ничья!")
                self.board.display()
                break
            current_player = (
                self.player2 if current_player == self.player1 else self.player1
            )

    # метод запускается после хода игрока, чтоыб проверить, не произошла ли победа
    def check_win(self, current_player: Player) -> Player:
        win_conditions = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        )
        for el in win_conditions:
            if all(self.board.cells[cell] == current_player.symbol for cell in el):
                return True
        return False

    # метод запускается после хода игрока, чтобы проверить, не произошла ли ничья в игре
    def check_draw(self):
        return all(cell != " " for cell in self.board.cells)


# создание игровой сессии
game = TicTacToe("Вася", "Василиса")
# запуск игровой сессии
game.play()
