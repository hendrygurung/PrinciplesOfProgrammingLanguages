import sys
import time

def rowno(i):
    return i // 9

def colno(i):
    return i % 9

def boxno(i):
    return (i // 9 // 3 )*3 + (i // 3) % 3

def getFileName():
    if sys.platform == "win32":
            filename = input("Filename? ")
    else:
            filename = sys.argv[-1]
    return filename

def isNeighbor(cell1, cell2):
    if rowno(cell1) == rowno(cell2):
        return True
    elif colno(cell1) == colno(cell2):
        return True 
    elif boxno(cell1) == boxno(cell2):
        return True
    else:
        return False


class Cell(object):
    def __init__(self, value):
        self.value = value
        if value == 0:
            self.candidates = [1,2,3,4,5,6,7,8,9]
        else:
            self.candidates = [value]

    def __str__(self):
        return str(self.value)

    def delCandidate(self, value):
        if value in self.candidates:
            self.candidates.remove(value)
        return
    
    def setvalue(self, value):
        self.value = value
        if value != 0:
            self.candidates = [value]


class Board(object):
    """docstring for Board"""
    def __init__(self, puzzle):
        self.list = []
        for x in range(81):
            self.list.append(Cell(0))
        for it in range(81):
            self.list[it].setvalue(int(puzzle[it]))
            for ti in range(81):
                if isNeighbor(ti, it) and ti != it:
                    self.list[ti].delCandidate(int(puzzle[it]))

    def __str__(self):
        out = ""
        for cell in self.list:
            out += str(cell)
        return out

    def notsolved(self):
        for x in range(81):
            if self.list[x].value == 0:
                return True
        
        return False


def solve(board):
    boardlist = [board]
    solist = [] 
    boardct = 1
    solct = 0
    while boardlist != [] and len(solist) < 2:
        arboard = boardlist.pop()
        if not arboard.notsolved():
            if arboard not in solist: 
                solist.append(arboard)
                solct += 1
            continue   
        minimum = 9
        for x in range(81):
            if arboard.list[x].value == 0 and len(arboard.list[x].candidates) < minimum:
                minimum = len(arboard.list[x].candidates)
                cell4 = arboard.list[x]
                index = x 
        for val in cell4.candidates:
            copybd = Board(str(arboard))
            copybd.list[index].setvalue(val)
            for x in range(81):
                if isNeighbor(index, x) and index != x:
                    copybd.list[x].delCandidate(val)
            boardlist.append(copybd)
            boardct +=1 
    print(board)
    print("Board generated: ", boardct)
    print("Solutions: ", solct)        
    for bd in solist:
        print(bd)



def main():
    filename = open(getFileName(), "r")
    puzzle = filename.read()
    puzzle = puzzle.replace("\n", "") 
    filename.close()
    board = Board(puzzle)
    
    before = time.clock()
    soln = solve(board)
    after = time.clock()
    print("Time: ", after-before, " sec.")

main()
