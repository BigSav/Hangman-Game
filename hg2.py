#Hangman Game - CSI

#imports
from turtle import *
from random import randint
import math
from time import sleep
import time

#wordlist
wordList = ['Phalanx' , 'Arachne' , 'Supreme' , 'Brevity' , 'Bolster' , \
            'Clout' , 'Culmination' , 'Desolate' , 'Disdain' , 'Fantasy' , \
            'Envy' , 'Greed' , 'Evoke' , 'Exacerbate' , 'Galvanizing' , \
            'Ignominious' , 'Soccer' , 'Assault' , 'Communist' , 'Hostile' , \
            'Rotation', 'Pogba', 'Yankees', 'Zombie', 'Mind', 'Venerable' , \
            'Chronicle' , 'Apple' , \
            'Chipotle' , 'Warhammer' , 'God' , 'Civilization' , \
            'Shuriken' , 'New York' , 'Coca-Cola' , \
            'Lions' , 'England' , 'Mini']

#Shows the randomized word (Hide when full game is running by user)
print(len(wordList))

#variables
sw = 700
sh = 800
s=getscreen()
s.setup(sw,sh)
s.bgcolor('#20f9f9')
t1=getturtle()
t1.speed(0)

#new turtle
tWriter = Turtle()
tWriter.hideturtle()

#Bad Letter Turtle
tBadLetters = Turtle()
tBadLetters.hideturtle()

#In-Game Variables
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettersWrong = "" #start empty
lettersCorrect = ""
secretWord = ""
displayWord = ""
guessesLeft = 6 #number of guesses left
fontS = int(sh*0.025)
gameDone = False

def chooseSecretWord():
    global secretWord
    secretWord = wordList[randint(0,len(wordList)-1)]
    print("The secret word is " + secretWord)

def displayText(newText):
    tWriter.clear()
    tWriter.penup()
    tWriter.goto(-int(sw*.4), -int(sh*.4))
    tWriter.write(newText, font=("Arial", fontS, "bold"))

def displayBadLetters(newText):
    tBadLetters.clear()
    tBadLetters.penup()
    tBadLetters.goto(-int(sw*.4), int(sh*.4))
    tBadLetters.write(newText, font=("Arial", fontS, "bold"))

def makeWordString():
    global displayWord, alpha
    displayWord= ""
    for l in secretWord:
        if str(l) in alpha:
            if str(l).lower() in lettersCorrect.lower():
                displayWord += str(l) + " "
            else:
                displayWord += "_" + " "
        else:
            displayWord += str(l) + " "
    
#Run Game
def getGuess():
    boxTitle="Letters Used: " + lettersWrong
    guess = s.textinput(boxTitle, "Enter a guess type $$ to Guess the word")
    return guess
def updateHangman():
    global guessesLeft
    if guessesLeft == 5:
        drawHead()
    if guessesLeft == 4:
        drawTorso()
    if guessesLeft == 3:
        drawRLeg()
        drawLLeg()
    if guessesLeft == 2:
        drawRArm()
        drawLArm()
    if guessesLeft == 1:
        drawSPTopHat()
        drawTopHat()
    if guessesLeft == 0:
        drawSPCane()
        drawCane()
        
    
def checkWordGuess():
    global guessesLeft, gamedone
    boxTitle="Word Guess"
    guess = s.textinput(boxTitle, "Guess the word!")
    if guess == secretWord:
        displayText("Yes, that's the word! " + secretWord + "! Congratulations!")
        gameDone = True
    else:
        displayText("No, the word is not: " + guess)
        time.sleep(1)
        displayText(displayWord)
        guessesLeft -=1
        updateHangman()

def restartGame():
    global guessesLeft, lettersCorrect, lettersWrong, gameDone
    boxTitle="Want to play again"
    guess = s.textinput(boxTitle, "Type Y or Yes to play again!")

    if guess.lower()=='y' or guess.lower() == 'yes':
        lettersCorrect = ""
        lettersWrong = ""
        t1.clear()
        drawGallows()
        chooseSecretWord()
        displayText("Guess a Letter")
        displayBadLetters("Not in word:[" + lettersWrong + "]")
        time.sleep(1)
        makeWordString()
        displayText(displayWord)
        guessesLeft = 6
        gameDone = False
    else:
        displayBadLetters("Ok, see you later!")
def playGame():
    global gameDone, guessesLeft, lettersCorrect, lettersWrong
    while gameDone == False and guessesLeft > 0:
        #get input
        guess = getGuess()
        #gets out of loop
        #gameDone = True
        if guess == "$$":
            print("Let them guess word")
            checkWordGuess()
        elif len(guess) > 1 or guess =="":
                displayText("Sorry I need a letter, guess again!")
                time.sleep(1)
                displayText(displayWord)
        elif guess not in alpha:
                displayText(theGuess + " is not a letter, guess again.")
                time.sleep(1)
                displayText(displayWord)
        elif guess.lower() in secretWord.lower():
            lettersCorrect += guess.lower()
            makeWordString()
            displayText(displayWord)
        else:
            lettersWrong += guess.lower()
            guessesLeft -= 1
            displayText(guess + " is not in the word")
            time.sleep(1)
            updateHangman()
            displayText(displayWord)
            displayBadLetters("Not in word:[" + lettersWrong + "]")
        if "_" not in displayWord:
            displayText("You win! The word was " + secretWord + "!")
            gameDone = True
        if guessesLeft <= 0:
            displayText("You're out of guesses! The word is: " + secretWord)
            gameDone = True
        if gameDone == True:
            restartGame()
 
            
        




#Gallows
def drawGallows():
    t1.setheading(0)
    t1.goto(-int(sw/6), -int(sh*.3))
    t1.width(5)
    t1.color('black')
    t1.penup()
    t1.goto(-int(sw/4), -int(sh/4))
    t1.pendown()
    t1.forward(int(sw/2))
#backwards
    t1.left(180)
    t1.forward(sw/7)
#vert-1
    t1.right(90)
    t1.forward(sw/1.5)
#horizontal-2
    t1.left(90)
    t1.forward(sw/6)
#veret-2
    t1.left(90)
    t1.forward(sw/12)
#drawHead
def drawHead():
    hR = int(sw*0.06)
    t1.penup()
    t1.goto(t1.xcor()-hR, t1.ycor()-hR)
    t1.pendown()
    t1.circle(hR)
    t1.penup()
    t1.goto(t1.xcor()+hR, t1.ycor()-hR)
#torso
def drawTorso():
    t1.pendown()
    t1.forward(int(sw*0.2))
    t1.penup()
#Right Leg
def drawRLeg():
    t1.pendown()
    t1.right(25)
    t1.forward(int(sw*.15))
    t1.left(180)
    t1.forward(int(sw*.15))
    t1.right(130)
    t1.penup()
#Left Leg
def drawLLeg():
    t1.pendown()
    t1.forward(int(sw*.15))
    t1.left(180)
    t1.forward(int(sw*.15))
    t1.right(25)
    t1.forward(int(sw*.14))
    t1.penup()
#Right Arm
def drawRArm():
    t1.pendown()
    t1.right(60)
    t1.forward(int(sw*.12))
    t1.left(180)
    t1.forward(int(sw*.12))
    t1.right(60)
    t1.penup()
#Left Arm
def drawLArm():
    t1.pendown()
    t1.forward(int(sw*.12))
    t1.left(180)
    t1.forward(int(sw*.12))
    t1.left(120)
    t1.penup()
#Start Position Top Hat
def drawSPTopHat():
    t1.forward(int(sw*.18))
    t1.pendown()
    t1.penup()
#Top Hat
def drawTopHat():
    t1.pendown()
    t1.begin_fill()
    t1.left(90)
    t1.forward(int(sw*.09))
    t1.right(90)
    t1.forward(int(sw*.02))
    t1.right(90)
    t1.forward(int(sw*.06))
    t1.left(90)
    t1.forward(int(sw*.09))
    t1.right(90)
    t1.forward(int(sw*.06))
    t1.right(90)
    t1.forward(int(sw*.09))
    t1.left(90)
    t1.forward(int(sw*.06))
    t1.right(90)
    t1.forward(int(sw*.02))
    t1.right(90)
    t1.forward(int(sw*.09))
    t1.end_fill()
    t1.penup()
#Starting Position Cane
def drawSPCane():
    t1.penup()
    t1.left(90)
    t1.forward(int(sw*.18))
    t1.right(90)
    t1.forward(int(sw*.10))
    t1.pendown()
    t1.penup()
#Cane
def drawCane():
    t1.pendown()
    t1.right(90)
    t1.forward(int(sw*.10))
    t1.left(180)
    t1.forward(int(sw*.32))
    t1.penup()
    

#Game starts here
drawGallows()
drawHead()
drawTorso()
drawRLeg()
drawLLeg()
drawRArm()
drawLArm()
drawSPTopHat()
drawTopHat()
drawSPCane()
drawCane()

#Game set-up/loading (Clears all and resets)
time.sleep(1)
t1.clear()
drawGallows()
chooseSecretWord()
displayText("Guess a Letter")
displayBadLetters("Not in word:[" + lettersWrong + "]")
time.sleep(1)
makeWordString()
displayText(displayWord)
playGame()

