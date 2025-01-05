import random, sys

HWin = 0
CWin = 0
RPSTie = 0
Rock = 'rock'
Paper = 'paper'
Scissors = 'scissors'
#generate

Game = 0

while Game < 5: 
    Guess = ''
    print ('Welcome to Rock Paper Scissors! Whats your pick?')
    Guess = input().lower()
    if Guess == 'rock':
        Guess = 0
    elif Guess == 'scissors':
        Guess = 1
    elif Guess == 'paper':
        Guess = 2
    else:
        print("type in Rock, Paper, or Scissors")

    Comprand = random.randint(0,2)

    if Comprand == 0:
        if Guess == 1:
            print ('Scissors against Rock')
            print ('You LOSE')
            CWin = CWin + 1
            print ('Your Wins ' + str(HWin) + ', Computer wins ' + str(CWin)+ ' Ties ' + str(RPSTie))
            Game = Game + 1
              
        elif Guess == Comprand:  
            print ('Rock against Rock')
            print ('Its a TIE')
            RPSTie = RPSTie + 1
            print ('Your Wins ' + str(HWin) + ', Computer wins ' + str(CWin)+ ' Ties ' + str(RPSTie))
            Game = Game + 1
            

        elif Guess == 2:
            print ('Paper against Rock')
            print ('You WIN')
            HWin = HWin + 1
            print ('Your Wins ' + str(HWin) + ', Computer wins ' + str(CWin)+ ' Ties ' + str(RPSTie)) 
            Game = Game + 1   

    elif Comprand == 1: 

        if Guess == 0:
            print ('Rock against Scissors')
            print ('You WIN')
            HWin = HWin + 1
            print ('Your Wins ' + str(HWin) + ', Computer wins ' + str(CWin)+ ' Ties ' + str(RPSTie))
            Game = Game + 1
        
        elif Guess == 2:  
            print ('Paper against Scissors')
            print ('You LOSE')
            CWin = CWin + 1
            print ('Your Wins ' + str(HWin) + ', Computer wins ' + str(CWin) + ' Ties ' + str(RPSTie))
            Game = Game + 1

        elif Guess == Comprand:
            print ('Scissors against Scissors')
            print ('Its a TIE')    
            RPSTie = RPSTie + 1
            print ('Your Wins ' + str(HWin) + ', Computer wins ' + str(CWin)+ ' Ties ' + str(RPSTie))
            Game = Game + 1

    elif Comprand == 2:

        if Guess == Comprand:
            print ('Paper against Paper')
            print ('Its a TIE')
            RPSTie = RPSTie + 1
            print ('Your Wins ' + str(HWin) + ', Computer wins ' + str(CWin)+ ' Ties ' + str(RPSTie))
            Game = Game + 1

        elif Guess == 1:  
            print ('Scissors against Paper')
            print ('You WIN')
            HWin = HWin + 1
            print ('Your Wins ' + str(HWin) + ', Computer wins ' + str(CWin)+ ' Ties ' + str(RPSTie))
            Game = Game + 1

        elif Guess == 0:
            print ('Rock against Paper')
            print ('You LOSE')
            CWin = CWin + 1
            print ('Your Wins ' + str(HWin) + ', Computer wins ' + str(CWin)+ ' Ties' + str(RPSTie)) 
            Game = Game + 1

print ('Thanks for playing!')


