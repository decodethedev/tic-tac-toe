DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8]
WINS = [
    # HORIZONTAL
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    # VERTICAL
    [2, 5, 8],
    [1, 4, 7],
    [0, 3, 6],
    # CROSS
    [2, 4, 6],
    [0, 4, 8],

]


class Board():
    def __init__(self):
        self.table = [
            ["0", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "8"]
        ]

    def print_Board(self):
        print("\t"+"="*15)
        for i in range(len(self.table)):
            for p in range(len(self.table[i])):
                if(p == 0):
                    print("\t(| " + self.table[i][p], end="")
                elif(p == 2):
                    print(self.table[i][p]+" |)")
                else:
                    print(f" | {self.table[i][p]} | ", end="")
        print("\t"+"="*15)

    def checkWin(self):
        for win in WINS:
            if self.checkIndex(win[0]) == ("X") or self.checkIndex(win[0]) == ("O"):
                if self.checkIndex(win[1]) == ("X") or self.checkIndex(win[1]) == ("O"):
                    if self.checkIndex(win[2]) == ("X") or self.checkIndex(win[2]) == ("O"):
                        if(self.checkIndex(win[0]) == "X" and self.checkIndex(win[1]) == "X" and self.checkIndex(win[2]) == "X"):
                            return ("X has won!")
                        elif (self.checkIndex(win[0]) == "O" and self.checkIndex(win[1]) == "O" and self.checkIndex(win[2]) == "O"):
                            return ("O has won!")
        return None

    def putInSlot(self, index, value):
        if(int(index) in DIGITS):
            count = 0
            for i in range(len(self.table)):
                for p in range(len(self.table[i])):
                    try:
                        if(count == index):
                            if(str(self.table[i][p]) != ("X" or "O") and int(self.table[i][p]) in DIGITS):
                                self.table[i][p] = value
                                return 200
                            else:
                                return "[ERROR] Slot Taken!"
                        count += 1
                    except:
                        if(count == index):
                            if(str(self.table[i][p]) != ("X" or "O") and (self.table[i][p]) in DIGITS):
                                self.table[i][p] = value
                                return 200
                            else:
                                return "[ERROR] Slot Taken!"
                        count += 1

        else:
            return "[ERROR] Please give a valid number from 0-8!"

    def checkIndex(self, index):
        if(int(index) in DIGITS):
            count = 0
            for i in range(len(self.table)):
                for p in range(len(self.table[i])):
                    if(count == index):
                        try:
                            if(int(self.table[i][p]) not in DIGITS):
                                return self.table[i][p]
                            else:
                                return False
                        except:
                            if((self.table[i][p]) not in DIGITS):
                                return self.table[i][p]
                            else:
                                return False
                    count += 1

    def checkTie(self):
        count = 0
        for row in self.table:
            for slot in row:
                try:
                    if(int(slot) in DIGITS):
                        count += 1
                except:
                    pass
        if(count == 0):
            return "Tie!"
        else:
            return False
