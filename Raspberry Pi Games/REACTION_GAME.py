#STEFANO DANISI
#REACTION_GAME.py

import RPi.GPIO as GPIO
import time
import random
import string

GPIO.setmode(GPIO.BOARD)

#LED STATE
playerOneLed = False
playerTwoLed = False
reactionLed = False

#INITIAL BUTTON STATE
btnOnePress = True
btnTwoPress = True

#GAME STATAS
rounds = 1
playerOneScore = 0
playerTwoScore = 0
y = True
fin = False
x = ""
# GPIO PIN NUMBERS FOR PLAYERS LED (CHANGE GPIO PIN NUMBERS TO MATCH YOUR WIRING)
plyrOne = 18  
plyrTwo = 36 

# GPIO PIN NUMBERS FOR PLAYER BUTTON
btnPlyrOne = 16
btnPlyrTwo = 37

gameLed = 11                                                                                                                                                                                                                                                             

# Player 1 LED
GPIO.setup(plyrOne, GPIO.OUT)
# Player 2 LED
GPIO.setup(plyrTwo, GPIO.OUT)

# Player 1 Button
GPIO.setup(btnPlyrOne, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# Player Two Button
GPIO.setup(btnPlyrTwo, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Game LED
GPIO.setup(gameLed, GPIO.OUT)


while y == True:
    if rounds <= 5:
        x = input("\nAre you ready to play (Y/N)?")
        if x.lower() == "y":
            #START GAME
            print ("\nGET READY!")
            time.sleep(3)
            print ("\nGAME STARTING!")
            time.sleep(1)
            print ("WAIT FOR MIDDLE LED TO BLINK BEFORE PRESSING BUTTON")
            print ("\nROUND: " + str(rounds))
            time.sleep(1)
            #RANDOM TIME TO LIGHT UP MIDDLE LED
            time.sleep(random.randint(2,10))
            GPIO.output(gameLed, True)
            time.sleep(.10)
            GPIO.output(gameLed, False)
            print ("PRESS BUTTON!")
            #BUTTON INPUT TO SEE WHICH PLAYER PRESSED THE BUTTON FIRST
            while btnOnePress == True and btnTwoPress == True:
                btnOnePress = GPIO.input(btnPlyrOne)
                btnTwoPress = GPIO.input(btnPlyrTwo)
                if btnOnePress == False:
                    btnTwoPress = True
                    break
                elif btnTwoPress == False:
                    btnOnePress = True
                    break
                else:
                    #RESET BUTTONS ENCASE OF ERROR
                    passbtnPlayerOne = True
                    btnPlayerTwo = True
            #DISPLAY AND LIGHT UP LED OF ROUND WINNING PLAYER
            if btnOnePress == False:
                GPIO.output(plyrOne, True)
               # print ("\nPLAYER 1 WINS ROUND " + str(rounds))
               # print ("\nPLAYER ONE SCORE: "+ playerOneScore+ "\nPLAYER TWO SCORE: "+ playerTwoScore)
                time.sleep(4)
                GPIO.output(plyrOne, False)
                rounds += 1
                playerOneScore = playerOneScore + 1
                btnPlayerOne = True
                btnPlayerTwo = True
                x = ""
                btnOnePress = True
                btnTwoPress = True
            elif btnTwoPress == False:
                GPIO.output(plyrTwo, True)
                #print ("\nPLAYER 2 WINS ROUND " + str(rounds))
                #print ("\n PLAYER ONE SCORE: "+ playerOneScore+"\nPLAYER TWO SCORE: "+ playerTwoScore )
                time.sleep(4)
                GPIO.output(plyrTwo, False)
                rounds += 1
                playerTwoScore = playerTwoScore + 1
                btnOnePress = True
                btnTwoPress = True
                x = ""
            else:
                pass
        elif x.lower() == 'n':
            #QUIT GAME AND CLEAN UP
            print("\nEXITING GAME!")
            rounds = 6
            y = False
            fin = True
            break
    else:
        #END OF GAME AND DISPLAY WINNING PLAYER
        print ("\nGAME FINISHED")
        print ("\nSCORE FOR PLAYER ONE: "+ playerOneScore)
        print ("\nSCORE FOR PLAYER TWO: "+ playerTwoScore)
        if playerOneScore > plaerTwoScore:
            print ("\nPLAYER ONE WINS!")

        else:
            print ("\nPLAYER TWO WINS!")
        y = False
        fin = True
        rounds = 6
        break
#PROGRAM CLEAN UP WHEN EXITING
if fin == True:        
    rounds = 0
    playerOneScore = 0
    playerTwoScore = 0
    btnPlayerOne = True
    btnPlayerTwo = True
    GPIO.output(gameLed, False)
    GPIO.output(plyrOne, False)
    GPIO.output(plyrTwo, False)
    GPIO.cleanup()
else:
    rounds = 0
    playerOneScore = 0
    playerTwoScore = 0
    btnPlayerOne = True
    btnPlayerTwo = True
    GPIO.output(gameLed, False)
    GPIO.output(plyrOne, False)
    GPIO.output(plyrTwo, False)
    GPIO.cleanup()
