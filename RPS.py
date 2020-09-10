# This program will provide a way to play rock, paper, scissors against the computer

import tkinter as tk
from random import randint

# GUI window
window = tk.Tk()
window.title("Rock, Paper, Scissors!")
window.geometry("400x300+10+10")
window.resizable(width = False, height = False)

# Variables for score
score1 = 0
score2 = 0

# Variables to store user and cpu choice
userChoice = None
cpuChoice = None

# Function to start the gameplay loop
def MainMenu():
    # Remove any existing elements
    playAgain.place_forget()
    menuBtn.place_forget()
    lblResult.place_forget()
    
    # Configure GUI elements
    lblUserRock.configure(text = "ROCK", height = 3, width = 11, bd = 3, relief = "ridge", bg = "light gray")
    lblUserPaper.configure(text = "PAPER", height = 3, width = 11, bd = 3, relief = "ridge", bg = "light gray")
    lblUserScissors.configure(text = "SCISSORS", height = 3, width = 11, bd = 3, relief = "ridge", bg = "light gray")
    cpuRock.configure(text = "ROCK", height = 3, width = 11, bd = 3, relief = "ridge", bg = "light gray")
    cpuPaper.configure(text = "PAPER", height = 3, width = 11, bd = 3, relief = "ridge", bg = "light gray")
    cpuScissors.configure(text = "SCISSORS", height = 3, width = 11, bd = 3, relief = "ridge", bg = "light gray")
    
    # Unselect any buttons
    userRock.configure(text = "ROCK", height = 3, width = 10, bd = 3, bg = "light gray", command = RockChoice)
    userPaper.configure(text = "PAPER", height = 3, width = 10, bd = 3, bg = "light gray", command = PaperChoice)
    userScissors.configure(text = "SCISSORS", height = 3, width = 10, bd = 3, bg = "light gray", command = ScissorsChoice)
    
    # Place all GUI elements
    lblYou.place(x = 75, y = 25)
    lblCPU.place(x = 300, y = 25)
    lblUserRock.place(x = 50, y = 60)
    lblUserPaper.place(x = 50, y = 120)
    lblUserScissors.place(x = 50, y = 180)
    cpuRock.place(x = 275, y = 60)
    cpuPaper.place(x = 275, y = 120)
    cpuScissors.place(x = 275, y = 180)
    score.place(x = 175, y = 230)
    userScore.place(x = 160, y = 260)
    hyphen.place(x = 200, y = 250)
    cpuScore.place(x = 240, y = 260)
    playBtn.place(x = 178, y = 100)
    resetBtn.place(x = 160, y = 150)

# Function to start a round of rock, paper, scissors
def EnterGame():
    global userChoice
    global cpuChoice
    userChoice = None
    cpuChoice = None
    # Clear the buttons and labels for now
    resetBtn.place_forget()
    playBtn.place_forget()
    playAgain.place_forget()
    menuBtn.place_forget()
    lblResult.place_forget()
    
    # Ensure choice labels are fresh
    lblUserRock.configure(text = "ROCK", height = 3, width = 11, bd = 3, relief = "ridge", bg = "light gray")
    lblUserPaper.configure(text = "PAPER", height = 3, width = 11, bd = 3, relief = "ridge", bg = "light gray")
    lblUserScissors.configure(text = "SCISSORS", height = 3, width = 11, bd = 3, relief = "ridge", bg = "light gray")
    cpuRock.configure(text = "ROCK", height = 3, width = 11, bd = 3, relief = "ridge", bg = "light gray")
    cpuPaper.configure(text = "PAPER", height = 3, width = 11, bd = 3, relief = "ridge", bg = "light gray")
    cpuScissors.configure(text = "SCISSORS", height = 3, width = 11, bd = 3, relief = "ridge", bg = "light gray")
    
    # Ensure user buttons are unselected
    userRock.configure(text = "ROCK", height = 3, width = 10, bd = 3, bg = "light gray", command = RockChoice)
    userPaper.configure(text = "PAPER", height = 3, width = 10, bd = 3, bg = "light gray", command = PaperChoice)
    userScissors.configure(text = "SCISSORS", height = 3, width = 10, bd = 3, bg = "light gray", command = ScissorsChoice)
    
    # Clear user labels and replace them with buttons
    lblUserRock.place_forget()
    lblUserPaper.place_forget()
    lblUserScissors.place_forget()
    userRock.place(x = 50, y = 60)
    userPaper.place(x = 50, y = 120)
    userScissors.place(x = 50, y = 180)
    
    # Place instruction labels
    instruct1.place(x = 165, y = 75)
    instruct2.place(x = 155, y = 95)
    
    # Place ready button, initially disabled
    readyBtn.place(x = 178, y = 125)
    readyBtn.configure(state = tk.DISABLED)

# Function to start ready sequence
def Ready():
    global userChoice
    
    # Clear buttons
    instruct1.place_forget()
    instruct2.place_forget()
    readyBtn.place_forget()
    
    # Lock in user choice
    userRock.place_forget()
    userPaper.place_forget()
    userScissors.place_forget()
    
    # Highlight user choice
    if(userChoice == 1):
        lblUserRock.configure(text = "ROCK", height = 3, width = 11, bd = 3, relief = "ridge", bg = "dark gray")
        lblUserRock.place(x = 50, y = 60)
        lblUserPaper.place(x = 50, y = 120)
        lblUserScissors.place(x = 50, y = 180)
    elif(userChoice == 2):
        lblUserPaper.configure(text = "PAPER", height = 3, width = 11, bd = 3, relief = "ridge", bg = "dark gray")
        lblUserRock.place(x = 50, y = 60)
        lblUserPaper.place(x = 50, y = 120)
        lblUserScissors.place(x = 50, y = 180)
    elif(userChoice == 3):
        lblUserScissors.configure(text = "SCISSORS", height = 3, width = 11, bd = 3, relief = "ridge", bg = "dark gray")
        lblUserRock.place(x = 50, y = 60)
        lblUserPaper.place(x = 50, y = 120)
        lblUserScissors.place(x = 50, y = 180)
     
    # Make CPU choose and go to results screen
    cpuChoose()
    Results()
    
# Function to display results
def Results():
    global score1
    global score2
    
    # Decide who wins and place label based on winner
    if(userChoice == cpuChoice):
        # Decide which cpu label to light up
        # If it is a tie, light both up gray
        # If there is a winner, light up winner in green and loser in red
        if(cpuChoice == 1):
            cpuRock.configure(text = "ROCK", height = 3, width = 11, bd = 3, relief = "ridge", bg = "dark gray")
        elif(cpuChoice == 2):
            cpuPaper.configure(text = "PAPER", height = 3, width = 11, bd = 3, relief = "ridge", bg = "dark gray")
        elif(cpuChoice == 3):
            cpuScissors.configure(text = "SCISSORS", height = 3, width = 11, bd = 3, relief = "ridge", bg = "dark gray")
        lblResult.configure(text = "TIE", font = ("Bold", 20), fg = "Black")
        lblResult.place(x = 180, y = 60)
    elif(userChoice == 1 and cpuChoice == 2):
        lblUserRock.configure(text = "ROCK", height = 3, width = 11, bd = 3, relief = "ridge", bg = "Red")
        cpuPaper.configure(text = "PAPER", height = 3, width = 11, bd = 3, relief = "ridge", bg = "Green")
        lblResult.configure(text = "YOU LOSE", font = ("Bold", 18), fg = "red")
        lblResult.place(x = 140, y = 60)
        # Update score
        score2 += 1
        cpuScore.configure(text = score2)
    elif(userChoice == 1 and cpuChoice == 3):
        lblUserRock.configure(text = "ROCK", height = 3, width = 11, bd = 3, relief = "ridge", bg = "Green")
        cpuScissors.configure(text = "SCISSORS", height = 3, width = 11, bd = 3, relief = "ridge", bg = "Red")
        lblResult.configure(text = "YOU WIN", font = ("Bold", 18), fg = "dark green")
        lblResult.place(x = 150, y = 60)
        # Update score
        score1 += 1
        userScore.configure(text = score1)
    elif(userChoice == 2 and cpuChoice == 1):
        lblUserPaper.configure(text = "PAPER", height = 3, width = 11, bd = 3, relief = "ridge", bg = "Green")
        cpuRock.configure(text = "ROCK", height = 3, width = 11, bd = 3, relief = "ridge", bg = "Red")
        lblResult.configure(text = "YOU WIN", font = ("Bold", 18), fg = "dark green")
        lblResult.place(x = 150, y = 60)
        # Update score
        score1 += 1
        userScore.configure(text = score1)
    elif(userChoice == 2 and cpuChoice == 3):
        lblUserPaper.configure(text = "PAPER", height = 3, width = 11, bd = 3, relief = "ridge", bg = "Red")
        cpuScissors.configure(text = "SCISSORS", height = 3, width = 11, bd = 3, relief = "ridge", bg = "Green")
        lblResult.configure(text = "YOU LOSE", font = ("Bold", 18), fg = "red")
        lblResult.place(x = 140, y = 60)
        # Update score
        score2 += 1
        cpuScore.configure(text = score2)
    elif(userChoice == 3 and cpuChoice == 1):
        lblUserScissors.configure(text = "SCISSORS", height = 3, width = 11, bd = 3, relief = "ridge", bg = "Red")
        cpuRock.configure(text = "ROCK", height = 3, width = 11, bd = 3, relief = "ridge", bg = "Green")
        lblResult.configure(text = "YOU LOSE", font = ("Bold", 18), fg = "red")
        lblResult.place(x = 140, y = 60)
        # Update score
        score2 += 1
        cpuScore.configure(text = score2)
    elif(userChoice == 3 and cpuChoice == 2):
        lblUserScissors.configure(text = "SCISSORS", height = 3, width = 11, bd = 3, relief = "ridge", bg = "Green")
        cpuPaper.configure(text = "PAPER", height = 3, width = 11, bd = 3, relief = "ridge", bg = "Red")
        lblResult.configure(text = "YOU WIN", font = ("Bold", 18), fg = "dark green")
        lblResult.place(x = 150, y = 60)
        # Update score
        score1 += 1
        userScore.configure(text = score1)
        
    # Place buttons for end of game choices (either play again or go to main menu)
    playAgain.place(x = 165, y  = 100)
    menuBtn.place(x = 165, y = 150)
   
# Function for rock selection
def RockChoice():
    global userChoice
    userChoice = 1
    if(userChoice != None):
        userPaper['bg'] = "light gray"
        userScissors['bg'] = "light gray"
    userRock['bg'] = "dark gray"
    SwitchState()

# Function for paper selection
def PaperChoice():
    global userChoice
    userChoice = 2
    if(userChoice != None):
        userRock['bg'] = "light gray"
        userScissors['bg'] = "light gray"
    userPaper['bg'] = "dark gray"
    SwitchState()

# Function for scissors selection
def ScissorsChoice():
    global userChoice
    userChoice = 3
    if(userChoice != None):
        userRock['bg'] = "light gray"
        userPaper['bg'] = "light gray"
    userScissors['bg'] = "dark gray"
    SwitchState()
    
# Function to switch ready button state
def SwitchState():
    readyBtn['state'] = tk.NORMAL
   
# Function for cpu to make a choice
def cpuChoose():
    global cpuChoice
    cpuChoice = randint(1, 3)
   
# Function to reset score
def ResetScore():
    global score1
    global score2
    score1 = 0
    score2 = 0
    userScore.config(text = score1)
    cpuScore.config(text = score2)

# GUI element configuration
# Label for user side
lblYou = tk.Label(text = "YOU", font = "Bold")
# Label for CPU side
lblCPU = tk.Label(text = "CPU", font = "Bold")
# Rock button for user side
userRock = tk.Button(text = "ROCK", height = 3, width = 10, bd = 3, bg = "light gray", command = RockChoice)
# Paper button for user side
userPaper = tk.Button(text = "PAPER", height = 3, width = 10, bd = 3, bg = "light gray", command = PaperChoice)
# Scissors button for user side
userScissors = tk.Button(text = "SCISSORS", height = 3, width = 10, bd = 3, bg = "light gray", command = ScissorsChoice)
# Initial labels for user choices
lblUserRock = tk.Label(text = "ROCK", height = 3, width = 11, bd = 3, relief = "ridge")
# Paper label for user side
lblUserPaper = tk.Label(text = "PAPER", height = 3, width = 11, bd = 3, relief = "ridge")
# Scissors label for user side
lblUserScissors = tk.Label(text = "SCISSORS", height = 3, width = 11, bd = 3, relief = "ridge")
# Rock label for user side
cpuRock = tk.Label(text = "ROCK", height = 3, width = 11, bd = 3, relief = "ridge")
# Paper label for user side
cpuPaper = tk.Label(text = "PAPER", height = 3, width = 11, bd = 3, relief = "ridge")
# Scissors label for user side
cpuScissors = tk.Label(text = "SCISSORS", height = 3, width = 11, bd = 3, relief = "ridge")
# Label for score
score = tk.Label(text = "SCORE", font = "Bold")
# Label for user score
userScore = tk.Label(text = score1)
# Label for hyphen
hyphen = tk.Label(text = "-", font = ("Bold", 20))
# Label for cpu score
cpuScore = tk.Label(text = score2)
# Button for play
playBtn = tk.Button(text = "PLAY", height = 2, width = 6, bd = 3, command = EnterGame)
# Reset button
resetBtn = tk.Button(text = "RESET SCORE", height = 2, width = 11, bd = 3, command = ResetScore)
# Create labels for game instruction
instruct1 = tk.Label(text = "Make a choice")
instruct2 = tk.Label(text = "and select 'READY'")
# Create ready button
readyBtn = tk.Button(text = "READY", height = 2, width = 6, bd = 3, command = Ready)
# Create result label
lblResult = tk.Label()
# Button to play again
playAgain = tk.Button(text = "PLAY AGAIN", height = 2, width = 10, command = EnterGame)
# Button to go to main menu
menuBtn = tk.Button(text = "MAIN MENU", height = 2, width = 10, command = MainMenu)

# Start game
MainMenu()

window.mainloop()
