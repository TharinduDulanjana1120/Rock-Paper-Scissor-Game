from tkinter import *

import grid as grid
from PIL import Image,ImageTk
from random import randint

#Main Interface
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="#FFE4C4")

#Images
rock_img = ImageTk.PhotoImage(Image.open("Rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("Paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("Scissor.png"))
rock_machine_img = ImageTk.PhotoImage(Image.open("Rock_Machine.png"))
paper_machine_img = ImageTk.PhotoImage(Image.open("Paper_Machine.png"))
scissor_machine_img = ImageTk.PhotoImage(Image.open("Scissor_Machine.png"))

#Inserting Images
user_label = Label(root,image=rock_img,bg="#FFE4C4")
machine_label = Label(root,image=rock_machine_img,bg="#FFE4C4")
user_label.grid(row=1,column=0)
machine_label.grid(row=1,column=4)

#Score Table
userScore = Label(root,text=0,font=100,bg="#FFE4C4",fg="BLACK")
machineScore = Label(root,text=0,font=100,bg="#FFE4C4",fg="BLACK")
userScore.grid(row=1,column=1)
machineScore.grid(row=1,column=3)

#Indicators
user_indicator = Label(root,font=50,text="USER",bg="#FFE4C4",fg="BLACK")
machine_indicator = Label(root,font=50,text="COMPUTER",bg="#FFE4C4",fg="BLACK")
user_indicator.grid(row=0,column=1)
machine_indicator.grid(row=0,column=3)

#Messages
msg = Label(root,font=50,bg="#FFE4C4",fg="BLACK")
msg.grid(row=3,column=2)

#Update Messages
def updateMessage(x):
    msg['text'] = x

#Update User Score
def updateUserScore():
    score = int(userScore["text"])
    score += 1
    userScore["text"] = str(score)

#Update Machine Score
def updateMachineScore():
    score = int(machineScore["text"])
    score += 1
    machineScore["text"] = str(score)

#Final Result
def checkWin(user,machine):
    if user == machine:
        updateMessage("Tie !")
    elif user == "rock":
        if machine == "paper":
            updateMessage("You Loose")
            updateMachineScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif user == "paper":
        if machine == "scissor":
            updateMessage("You Loose")
            updateMachineScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif user == "scissor":
        if machine == "rock":
            updateMessage("You Loose")
            updateMachineScore()
        else:
            updateMessage("You win")
            updateUserScore()
    else:
        pass


#Update Choices
choices = ["rock","paper","scissor"]

def updateChoice(x):
    #For Machine
    machineChoice = choices [randint(0,2)]
    if machineChoice == "rock":
        machine_label.configure(image=rock_machine_img)
    elif machineChoice == "paper":
        machine_label.configure(image=paper_machine_img)
    else:
        machine_label.configure(image=scissor_machine_img)
    #For User
    if x =="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkWin(x,machineChoice)


#Buttons
rock = Button(root,width=20,height=2,text="ROCK",bg="#CD1076",fg="white",command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="#FFC125",fg="white",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",bg="#00B2EE",fg="white",command=lambda:updateChoice("scissor")).grid(row=2,column=3)




root.mainloop()