import random

class Core:
    """
    2048 game core
    """
    board_height = 4
    board_width = 4
    probability = 0.95  # probability that 2 will appear as a new tile, instead of 4
    initial_tiles = 2   # number of tiles at initiation
    spacing = 8         # width of space given to each tile, when printing to stdout

    def __init__(self):
        self.board = [ ]
        self.empty = Core.board_height * Core.board_width  # number of empty tiles
        self.score = 0                                     # current score
        self.best = 0                                      # best tile achieved
        self.gameover = False

        for i in range(Core.board_height):
            self.board.append([])
            for j in range(Core.board_width):
                self.board[i].append(0)

        for i in range(Core.initial_tiles):
            self.generate()

    def play(self, dir):
        """
        Receiving 1 integer argument direction, makes a move on 2048 board
        1 = towards left, 2 = towards top, 3 = towards right, 4 = towards bottom
        """
        if self.gameover:
            return

        isValid = False  # True if any tile moved

        if dir == 1:
            for i in range(Core.board_height):
                prev = -1
                index = 0
                for j in range(Core.board_width):
                    if self.board[i][j]:
                        if self.board[i][j] != prev:
                            prev = self.board[i][j]
                            if index != j:
                                self.board[i][index] = self.board[i][j]
                                isValid = True
                            index += 1
                        else:
                            self.board[i][index - 1] *= 2
                            self.empty += 1
                            self.score += self.board[i][index - 1]
                            if self.board[i][index - 1] > self.best:
                                self.best = self.board[i][index - 1]
                            isValid = True
                            prev = -1
                for j in range(index, Core.board_width):
                    self.board[i][j] = 0
        elif dir == 2:
            for j in range(Core.board_width):
                prev = -1
                index = 0
                for i in range(Core.board_height):
                    if self.board[i][j]:
                        if self.board[i][j] != prev:
                            prev = self.board[i][j]
                            if index != i:
                                self.board[index][j] = self.board[i][j]
                                isValid = True
                            index += 1
                        else:
                            self.board[index - 1][j] *= 2
                            self.empty += 1
                            self.score += self.board[index - 1][j]
                            if self.board[index - 1][j] > self.best:
                                self.best = self.board[index - 1][j]
                            isValid = True
                            prev = -1
                for i in range(index, Core.board_width):
                    self.board[i][j] = 0
        elif dir == 3:
            for i in range(Core.board_height):
                prev = -1
                index = Core.board_width - 1
                for j in range(Core.board_width - 1, -1, -1):
                    if self.board[i][j]:
                        if self.board[i][j] != prev:
                            prev = self.board[i][j]
                            if index != j:
                                self.board[i][index] = self.board[i][j]
                                isValid = True
                            index -= 1
                        else:
                            self.board[i][index + 1] *= 2
                            self.empty += 1
                            self.score += self.board[i][index + 1]
                            if self.board[i][index + 1] > self.best:
                                self.best = self.board[i][index + 1]
                            isValid = True
                            prev = -1
                for j in range(index, -1, -1):
                    self.board[i][j] = 0
        elif dir == 4:
            for j in range(Core.board_width):
                prev = -1
                index = Core.board_height - 1
                for i in range(Core.board_height - 1, -1, -1):
                    if self.board[i][j]:
                        if self.board[i][j] != prev:
                            prev = self.board[i][j]
                            if index != i:
                                self.board[index][j] = self.board[i][j]
                                isValid = True
                            index -= 1
                        else:
                            self.board[index + 1][j] *= 2
                            self.empty += 1
                            self.score += self.board[index + 1][j]
                            if self.board[index + 1][j] > self.best:
                                self.best = self.board[index + 1][j]
                            isValid = True
                            prev = -1
                for i in range(index, -1, -1):
                    self.board[i][j] = 0

        if isValid:
            self.generate()
        self.gameover = self.checkdefeat()

    def reset(self):
        for i in range(Core.board_height):
            for j in range(Core.board_width):
                self.board[i][j] = 0

        self.empty = 0
        self.score = 0
        self.gameover = False

        for i in range(Core.initial_tiles):
            self.generate()

    def generate(self):
        if self.gameover or self.empty <= 0:
            return

        count = 0
        position = int(random.random() * self.empty)
        num = (2, 4)[random.random() >= Core.probability]

        for i in range(Core.board_height):
            for j in range(Core.board_width):
                if self.board[i][j]:
                    continue
                elif count == position:
                    self.board[i][j] = num
                    self.empty -= 1
                    return
                else:
                    count += 1

    def checkdefeat(self):
        """
        Returns True if no more movement is possible
        """
        if empty != 0:
            return False

        for i in range(Core.board_height):
            prev = -1
            for j in range(Core.board_width):
                if prev != self.board[i][j]:
                    prev = self.board[i][j]
                else:
                    return False

        for j in range(Core.board_width):
            prev = -1
            for i in range(Core.board_height):
                if prev != self.board[i][j]:
                    prev = self.board[i][j]
                else:
                    return False

        return True

    def printboard(self):
        """
        Prints 2048 board in following format:

              Score: n        Best: m
             --------------------------------
              100000  100000  100000  100000

              100000  100000  100000  100000

              100000  100000  100000  100000

              100000  100000  100000  100000
             --------------------------------

        """
        string = ""
        width = Core.board_width * Core.spacing

        string += ("{:<" + str(int(width / 2)) + "}").format(" Score: " + str(self.score))
        string += ("{:<" + str(int(width / 2)) + "}").format(" Best: " + str(self.best))
        string += "\n"

        for i in range(width):
            string += "-"
        string += "\n"

        for i in range(Core.board_height):
            for j in range(Core.board_width):
                if self.board[i][j]:
                    string += ("{:^" + str(Core.spacing) + "d}").format(self.board[i][j])
                else:
                    string += ("{:^" + str(Core.spacing) + "}").format("-")
            string += "\n\n"
        string = string[:-1]

        for i in range(width):
            string += "-"
        string += "\n\n"

        print(string, end="")
