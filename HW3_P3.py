#Problem 3_3
#layout of the board
row1 = [" "," "," "," "," "," "," "]
row2 = [" "," "," "," "," "," "," "]
row3 = [" "," "," "," "," "," "," "]
row4 = [" "," "," "," "," "," "," "]
row5 = [" "," "," "," "," "," "," "]
row6 = [" "," "," "," "," "," "," "]
board = [row1,row2,row3,row4,row5,row6]

k = 0
gamestart = 0
r = 0
c = 0
row = [5,5,5,5,5,5,5]

while gamestart == 0:
    while k < 6:
        print (board[k],end = "\n")
        k = k+1
    P1 = input("Player X >> ") 
    while P1.isdigit() == False: 
        print ("invaild input, Try again[0-6]")
        P1 = input("Player X >> ")
    P1 = int(P1)
    while P1 < 0 or P1 > 6: 
        print("Out of range.Try again[0-6]")
        P1 = input("Player X >> ")
        while P1.isdigit() == False:
            print ("invaild input, Try again[0-6]")
            P1 = input("Player X >> ")
        P1 = int(P1)
    while row[P1] < 0: 
        print ("This column is full. Try another column.")
        P1 = input("Player X >> ")
        while P1.isdigit() == False:
            print ("invaild input. Try again[0-6]")
            P1 = input("Player X >> ")
        P1 = int(P1)

    board[row[P1]][P1] = "X" 
    row[P1] -= 1 
    k = 0
    while k < 6: 
        print (board[k],end = "\n")
        k = k+1
    
    while r <= 6: 
        while c <= 2:
            if board[c][r] == board[c+1][r] == board[c+2][r] == board[c+3][r] == "X":
                print ("Winner: X")
                exit()

            c = c + 1
        c = 0
        r = r + 1
    r = 0
    c = 0
    
    while c <= 5: 
        while r <= 2:
            if board[c][r] == board[c][r+1] == board[c][r+2] == board[c][r+3] == "X":
                print ("Winner: X") 
                exit()

            r = r + 1
        r = 0
        c = c + 1
    r = 0
    c = 0

    while c <= 2: 
        while r <= 3:
            if board[c][r] == board[c+1][r+1] == board[c+2][r+2] == board[c+3][r+3] == "X":
                print ("Winner: X") 
                exit()

            r = r + 1
        r = 0
        c = c + 1
    r = 0
    c = 0

    while c <= 2: 
        while r <= 3:
            if board[5-c][r] == board[4-c][r+1] == board[3-c][r+2] == board[2-c][r+3] == "X":
                print ("Winner: X")
                exit()

            r = r + 1
        r = 0
        c = c + 1
    r = 0
    c = 0
    
    P2 = input("Player O >> ")
    while P2.isdigit() == False:
        print ("invaild input, Try again[0-6]")
        P2 = input("Player O >> ")
    P2 = int(P2)
    while P2 < 0 or P2 > 6:
        print("Out of range, Try again[0-6]")
        P2 = input("Player O >> ")
        while P2.isdigit() == False:
            print ("invaild input. Try again[0-6]") 
            P2 = input("Player O >> ")
        P2 = int(P2)
    while row[P2] < 0:
        print ("This column is full. Try another column.")
        P2 = input("Player 0 >> ")
        while P2.isdigit() == False:
            print ("invaild input. Try again[0-6]") 
            P2 = input("Player O >> ")
        P2 = int(P2)
    board[row[P2]][P2] = "O"
    row[P2] -= 1
    k = 0
    while k < 6:
        print (board[k],end = "\n")
        k = k+1

    while r <= 6:
        while c <= 2:
            if board[c][r] == board[c+1][r] == board[c+2][r] == board[c+3][r] == "O":
                print ("Winner: O") 
                exit()
                
            c = c + 1
        c = 0
        r = r + 1
    r = 0
    c = 0

    while c <= 5:
        while r <= 2:
            if board[c][r] == board[c][r+1] == board[c][r+2] == board[c][r+3] == "O":
                print ("Winner: O") 
                exit()
            r = r + 1
        r = 0
        c = c + 1        
    r = 0
    c = 0

    while c <= 2:
        while r <= 3:
            if board[c][r] == board[c+1][r+1] == board[c+2][r+2] == board[c+3][r+3] == "O":
                print ("Winner: O") 
                exit()

            r = r + 1
        r = 0
        c = c + 1
    r = 0
    c = 0

    while c <= 2:
        while r <= 3:
            if board[5-c][r] == board[4-c][r+1] == board[3-c][r+2] == board[2-c][r+3] == "O":
                print ("Winner: O") 
                exit()

            r = r + 1
        r = 0
        c = c + 1
    r = 0
    c = 0
    
    if row == [-1,-1,-1,-1,-1,-1,-1]:
        print ("Draw")
        exit()