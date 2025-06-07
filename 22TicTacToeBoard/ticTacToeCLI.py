


def checkTieCondition():
    if (box1 != " " and box2 != " " and box3 != " "
        and box4 != " " and box5 != " " and box6 != " "
        and box7 != " " and box8 != " " and box9 != " "):

        print("this match has ended in a tie")
        return True
    return False


def checkPlayer2Won():
    if (box1 == "X" and box2 == "X" and box3 == "X"
            or box4 == "X" and box5 == "X" and box6 == "X"
            or box7 == "X" and box8 == "X" and box9 == "X"
            or box1 == "X" and box4 == "X" and box7 == "X"
            or box2 == "X" and box5 == "X" and box8 == "X"
            or box3 == "X" and box6 == "X" and box9 == "X"
            or box1 == "X" and box5 == "X" and box9 == "X"
            or box3 == "X" and box5 == "X" and box7 == "X"
    ):
        print("player2 has won")
        return True
    return False

def checkPlayer1Won():
    if (box1 == "O" and box2 == "O" and box3 == "O"
            or box4 == "O" and box5 == "O" and box6 == "O"
            or box7 == "O" and box8 == "O" and box9 == "O"
            or box1 == "O" and box4 == "O" and box7 == "O"
            or box2 == "O" and box5 == "O" and box8 == "O"
            or box3 == "O" and box6 == "O" and box9 == "O"
            or box1 == "O" and box5 == "O" and box9 == "O"
            or box3 == "O" and box5 == "O" and box7 == "O"
    ):
        print("player1 has won")
        return True
    return False




def displayBoard():
    print(box1 + " | " + box2 + " | " + box3)
    print("----------")
    print(box4 + " | " + box5 + " | " + box6)
    print("----------")
    print(box7 + " | " + box8 + " | " + box9)

def player1Input():
    global box1, box2, box3, box4, box5, box6, box7, box8, box9

    if player1Move == 1:
        box1 = "O"
    elif player1Move == 2:
        box2 = "O"
    elif player1Move == 3:
        box3 = "O"
    elif player1Move == 4:
        box4 = "O"
    elif player1Move == 5:
        box5 = "O"
    elif player1Move == 6:
        box6 = "O"
    elif player1Move == 7:
        box7 = "O"
    elif player1Move == 8:
        box8 = "O"
    elif player1Move == 9:
        box9 = "O"

def player2Input():
    global box1, box2, box3, box4, box5, box6, box7, box8, box9

    if player2Move == 1:
        box1 = "X"
    elif player2Move == 2:
        box2 = "X"
    elif player2Move == 3:
        box3 = "X"
    elif player2Move == 4:
        box4 = "X"
    elif player2Move == 5:
        box5 = "X"
    elif player2Move == 6:
        box6 = "X"
    elif player2Move == 7:
        box7 = "X"
    elif player2Move == 8:
        box8 = "X"
    elif player2Move == 9:
        box9 = "X"


if __name__ == '__main__':
    box1 = " "
    box2 = " "
    box3 = " "
    box4 = " "
    box5 = " "
    box6 = " "
    box7 = " "
    box8 = " "
    box9 = " "
    # shows blank board
    displayBoard()

    while True:

        # code that represents player 1 move
        while True:
            print("player1 make your move type a number between 1-9")
            player1Move = int(input())
            if (player1Move == 1 and box1 != " "
                or player1Move == 2 and box2 != " "
                or player1Move == 3 and box3 != " "
                or player1Move == 4 and box4 != " "
                or player1Move == 5 and box5 != " "
                or player1Move == 6 and box6 != " "
                or player1Move == 7 and box7 != " "
                or player1Move == 8 and box8 != " "
                or player1Move == 9 and box9 != " "):
                print("the box is already taken")


            elif player1Move <= 0 or player1Move >= 10:
                print("your input is invalid")
            else:
                print("that is a valid move")
                break


        player1Input()
        displayBoard()
        # check if player 1 won
        if checkPlayer1Won() or checkTieCondition():
            break



        # if not, player 2 goes
        while True:
            print("player2 make your move type a number between 1-9")
            player2Move = int(input())
            if (player2Move == 1 and box1 != " "
                or player2Move == 2 and box2 != " "
                or player2Move == 3 and box3 != " "
                or player2Move == 4 and box4 != " "
                or player2Move == 5 and box5 != " "
                or player2Move == 6 and box6 != " "
                or player2Move == 7 and box7 != " "
                or player2Move == 8 and box8 != " "
                or player2Move == 9 and box9 != " "):
                print("the box is already taken")

            elif player2Move <= 0 or player2Move >= 10:
                print("your input is invalid")
            else:
                print("that is a valid move")
                break

        player2Input()
        displayBoard()
        if checkPlayer2Won():
            break




        # if not loop back to player 1.

