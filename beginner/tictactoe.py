if __name__=="__main__":
    board=[ "-","-","-",
            "-","-","-",
            "-","-","-" ]
    resume=True
    current_player ='O'


    def printboard():
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("-"*10)
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("-"*10)
        print(board[6] + " | " + board[7] + " | " + board[8])

    def switch_player():
        global current_player

        if(current_player=='O'):
            current_player='X'
        else:
            current_player='O'

    def checkhor(board):
        global current_player,resume
        if(board[0]==board[1] and board[1]==board[2] and board[0]!='-'):
            printboard()
            print(f"The winner of this game is {current_player}")
            resume=False
        elif(board[3]==board[4] and board[4]==board[5] and board[3]!='-'):
            printboard()
            print(f"The winner of this game is {current_player}")
            resume=False
        elif(board[6]==board[7] and board[7]==board[8] and board[6]!='-'):
            printboard()
            print(f"The winner of this game is {current_player}")
            resume=False

    def checkver(board):
        global current_player,resume
        if(board[0]==board[3] and board[3]==board[6] and board[0]!='-'):
            printboard()
            print(f"The winner of this game is {current_player}")
            resume=False
        elif(board[1]==board[4] and board[4]==board[7] and board[1]!='-'):
            printboard()
            print(f"The winner of this game is {current_player}")
            resume=False
        elif(board[2]==board[5] and board[5]==board[8] and board[2]!='-'):
            printboard()
            print(f"The winner of this game is {current_player}")
            resume=False

    def checkdiag(board):
        global current_player,resume
        if(board[0]==board[4] and board[4]==board[8] and board[0]!='-'):
            printboard()
            print(f"The winner of this game is {current_player}")
            resume=False
        elif(board[2]==board[4] and board[4]==board[6] and board[2]!='-'):
            printboard()
            print(f"The winner of this game is {current_player}")
            resume=False
        
    def checktie(board):
        global current_player,resume
        if '-' not in board:
            printboard()
            print("This game is a tie")
            resume=False

    def checkwinner():
        checkdiag(board)
        checkhor(board)
        checkver(board)

    def enter_choice(board):
        global current_player,resume
        choice=int(input("Enter your choice (1-9) : "))
        if(board[choice-1]!='-'or choice<0 or choice>9):
            print("OOPS! enter a valid choice.")
        else:
            board[choice-1]=current_player

    while resume:
        printboard()
        enter_choice(board)
        checktie(board)
        checkwinner()
        switch_player()
