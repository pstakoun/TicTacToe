board = list(range(9))
c = "Y"

def getMove():
    global c
    if c == "X":
        c = "Y"
    elif c == "Y":
        c = "X"
        
    i = input(c + "'s move: ")
    while True:
        try:
            i = int(i)
            if not (i > 0 and i < 10) or not board[i-1] == " ":
                i = input("Invalid move! ")
                continue
        except ValueError:
            i = input("Invalid move! ")
            continue
        return i-1
    
def boardFull():
    for i in range(9):
        if board[i] == " ":
            return False
    return True

def gameOver():
    if boardFull():
        print("Draw!")
        return True
    # Rows
    if not board[0] == " " and board[0] == board[1] and board[1] == board[2]:
        print(board[0], "wins!")
        return True
    if not board[3] == " " and board[3] == board[4] and board[4] == board[5]:
        print(board[3], "wins!")
        return True
    if not board[6] == " " and board[6] == board[7] and board[7] == board[8]:
        print(board[6], "wins!")
        return True
    # Columns
    if not board[0] == " " and board[0] == board[3] and board[3] == board[6]:
        print(board[0], "wins!")
        return True
    if not board[1] == " " and board[1] == board[4] and board[4] == board[7]:
        print(board[1], "wins!")
        return True
    if not board[2] == " " and board[2] == board[5] and board[5] == board[8]:
        print(board[2], "wins!")
        return True
    # Diagonals
    if not board[0] == " " and board[0] == board[4] and board[4] == board[8]:
        print(board[0], "wins!")
        return True
    if not board[2] == " " and board[2] == board[4] and board[4] == board[6]:
        print(board[2], "wins!")
        return True

def init():
    print(" 7 | 8 | 9 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 1 | 2 | 3 ")
    for i in range(9):
        board[i] = " "
    start()

def start():
    while True:
        print("")
        print("",board[6],"|",board[7],"|",board[8],"")
        print("-----------")
        print("",board[3],"|",board[4],"|",board[5],"")
        print("-----------")
        print("",board[0],"|",board[1],"|",board[2],"")
        if gameOver():
            break
        i = getMove()
        board[i] = c

init()
