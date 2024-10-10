import tkinter as tk
from tkinter import *
import random
top=tk.Tk()
top.title("COLOR GAME")
top.geometry("500x500")
#list for colors
colors=['Red','Blue','Green','Yellow','Purple','Pink','Black','White','Orange','Brown']
score=0
timeleft=30
paused=False #to track whether the game is paused or not
#function that will start game
def startgame(event):
    if  timeleft==30 and not paused:
        #start countdown timer
        countdown()
    if not paused:
        nextcolour()
#function to choose and display  random color
def nextcolour():
    global score
    global timeleft
    if timeleft > 0 and not paused:
        e.focus_set()
        #if the color typed is equal to color of the text
        if e.get().lower()==colors[1].lower():
            score+=1#score=score+1
        #clear text entry box
        e.delete(0,END)
        random.shuffle(colors)
        label.config(fg = str(colors[1]), text = str(colors[0]))
        #update the score
        scorelabel.config(text="Score:"+str(score))
#function for timer
def countdown():
    global timeleft
    if timeleft>0 and not paused:
        timeleft-=1
        timelabel.config(text="Time left:"+str(timeleft))
        timelabel.after(1000,countdown)
    elif timeleft==0:
        finalscore()#when time is  up, end the game and show the final score



def finalscore():
    final_score_window=Toplevel(top)
    final_score_window.title("Final Score")
    final_score_window.geometry("250x250")
    final_label=Label(final_score_window,text=f"Your final Score is:{score}",font=("Helvetica",15))
    final_label.pack()
    restart_button=Button(final_score_window,text="Restart",command=restartgame)
    restart_button.pack()
    final_score_window.grab_set()#make sure the user ineracts only with this window until it's close



def restartgame():
    global timeleft,score
    timeleft=30#reset time left to 30 sec
    score=0#reset score to 0
    paused=False
    scorelabel.config(text="press enter to start")
    timelabel.config(text="Time Left:"+str(timeleft))
    label.config(text="",fg="black")#clear the color  label
    e.delete(0,END)#clear the entry box

def pause_game():
    global paused
    if paused:
        paused=False
        pause_button.config(text="pause")
        countdown()#resume the timeleft
        nextcolour()#resume game
    else:
        paused=True
        pause_button.config(text="Resume")




#label for instruction 
instruction=Label(top,text="Type in the color of the word and not the word text!")
instruction.pack()
#button for pause and resume
pause_button=Button(top,text="pause",command=pause_game)
pause_button.pack()
#label for score
scorelabel=Label(top,text="press enter to start")
scorelabel.pack()
#restart  button
restart_button=Button(top,text="Restart",command=restartgame)
restart_button.pack()

#label for timer
timelabel=Label(top,text="TIME LEFT:"+str(timeleft))
timelabel.pack()
#label for displaying colors
label=Label(top,font=('Helvetica',60))
label.pack()
#entry for user to enter answer
e=Entry(top)

#start the game when user pressed enter
top.bind('<Return>',startgame)
e.pack()
#set focus  until user types
e.focus_set()
top.mainloop()