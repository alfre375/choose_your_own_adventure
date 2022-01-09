from tkinter import Canvas
from tkinter import Tk
from tkinter import *
import random
import time
import json
import math
choice = 1
# 1, 2, 3, 4
window = Tk()
window.title("Choose you own adventure")

canvas = Canvas(window, width=1000, height=700,bg="white")
canvas.pack()

def make_text_correspondence(scene):
    canvas.delete("all")
    canvas.create_rectangle(250,500,750,650)

    if scene == 1: # fork in the road
        canvas.create_text(260,510,text="You are walking around and get lost in a forest. You ", fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(260,535,text="spot a fork in the road. Go left or right.", fill="black", font = ("Helvetica",15),anchor="nw")
        make_choices(scene)
        make_background(scene)
        
    if scene == 2: #press button or not
        canvas.create_text(260,510,text="You go left. You spot a mysterious red button. Do you ", fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(260,535,text="want to press it?", fill="black", font = ("Helvetica",15),anchor="nw")
        make_choices(scene)
        make_background(scene)
        
    if scene == 3: # you find a cactus
        canvas.create_text(260,510,text="You go right. You see a big cactus. for some reason,", fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(260,535,text="this cactus looks very appealing. Hug the cactus?", fill="black", font = ("Helvetica",15),anchor="nw")
        make_choices(scene)
        make_background(scene)
        
    if scene == 4: # pressed button # death
        canvas.create_text(260,510,text="Your curiousity got the best of you. That, and you ", fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(260,535,text="forgot to read the beware of explosion signs.", fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(500,250,text="YOU DIED!", fill="red", font = ("Helvetica",100),anchor="center")
        
    if scene == 5: # dont press button 
        canvas.create_text(260,510,text="You noticed a sign close to the button. You read it and  ", fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(260,535,text="it says \"Beware of explosions!\" you are very glad you ", fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(260,560,text="didnt press it. But you see someone running towards ", fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(260,585,text="you. Run away or stay and talk? ", fill="black", font = ("Helvetica",15),anchor="nw")
        make_choices(scene)
        make_background(scene)
        
    if scene == 6: # hug the cactus
        canvas.create_text(258,510,text="You hugged a cactus. You arent sure what your parents ", fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(258,535,text="did wrong to make you decide this was a decision ", fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(258,560,text="worth considering, but luckily it was just some kid's ", fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(258,585,text="balloon cactus. Do you pop the balloon cactus? ", fill="black", font = ("Helvetica",15),anchor="nw")
        make_choices(scene)
        make_background(scene)
        
    if scene == 7: # dont hug the cactus
        canvas.create_text(260,510,text="You decide not to hug it. You look closer and realize it ", fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(260,535,text="is a balloon cactus. You see a kid holding it and  ", fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(260,560,text="wonder where he got it from. do you investigate? ", fill="black", font = ("Helvetica",15),anchor="nw")
        make_choices(scene)
        make_background(scene)
        
    if scene == 8: # pop the balloon cactus
        canvas.create_text(260,510,text="You pop the cactus and he pushes you off a cliff. As " ,fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(260,535,text="you are falling you wonder how you failed to notice the ", fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(260,560,text="gigantic ledge that drops over 200 feet", fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(500,250,text="YOU DIED!", fill="red", font = ("Helvetica",100),anchor="center")
        
    if scene == 9: # dont pop the cactus
        canvas.create_text(260,510,text="You decide that you dont want to pop the  ", fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(260,535,text="cactus. You wonder where he got that ballon. Do you ", fill="black", font = ("Helvetica",15),anchor="nw")
        canvas.create_text(260,560,text=" investigate? ", fill="black", font = ("Helvetica",15),anchor="nw")
        make_choices(7)
        make_background(7)
        
        
        
def make_choices(choice):
    canvas.create_rectangle(780,520,930,620)
    canvas.create_rectangle(70,520,220,620)
    if choice == 1:
        canvas.create_text(100,540,text="Left", fill="black", font = ("Helvetica",40),anchor="nw")
        canvas.create_text(795,540,text="Right", fill="black", font = ("Helvetica",40),anchor="nw")
    if choice == 2:
        canvas.create_text(85,550,text="PRESS!", fill="black", font = ("Helvetica",25),anchor="nw")
        canvas.create_text(820,540,text="Dont ", fill="black", font = ("Helvetica",20),anchor="nw")
        canvas.create_text(820,570,text="press.", fill="black", font = ("Helvetica",20),anchor="nw")
    if choice == 3:
        canvas.create_text(85,550,text="HUG IT!", fill="black", font = ("Helvetica",25),anchor="nw")
        canvas.create_text(820,540,text="Dont ", fill="black", font = ("Helvetica",20),anchor="nw")
        canvas.create_text(820,570,text="hug it.", fill="black", font = ("Helvetica",20),anchor="nw")
    if choice == 4:
        pass # no choices here
    if choice == 5:
        canvas.create_text(100,540,text="Talk", fill="black", font = ("Helvetica",40),anchor="nw")
        canvas.create_text(795,550,text="Vamoose!", fill="black", font = ("Helvetica",20),anchor="nw")
    if choice == 6:
        canvas.create_text(85,550,text="POP IT!", fill="black", font = ("Helvetica",25),anchor="nw")
        canvas.create_text(820,540,text="Dont ", fill="black", font = ("Helvetica",20),anchor="nw")
        canvas.create_text(820,570,text="pop it.", fill="black", font = ("Helvetica",20),anchor="nw")
    if choice == 7:
        canvas.create_text(795,550,text="Investigate", fill="black", font = ("Helvetica",20),anchor="nw")
        canvas.create_text(85,540,text="Waste of ", fill="black", font = ("Helvetica",20),anchor="nw")
        canvas.create_text(120,565,text="time", fill="black", font = ("Helvetica",20),anchor="nw")
    
def make_background(choice):
    if choice == 1:
        canvas.create_line(550,200,550,500)
        canvas.create_line(450,200,450,500)
        canvas.create_line(0,200,450,200)
        canvas.create_line(1000,200,550,200)
        canvas.create_line(0,100,1000,100)
    if choice == 2:
        canvas.create_oval(425,175,575,325,fill = "gray")
        canvas.create_oval(450,200,550,300,fill = "red")
    
    if choice == 4: # no bg here
        pass

def mouse_was_clicked(event):
    global choice 
    if choice == 1:
        if 70 < event.x < 220 and 520 < event.y < 620: # left button
            choice = 2
            make_text_correspondence(2) 
            time.sleep(0.25)
        if 780 < event.x < 930 and 520 < event.y < 620: # right button
            choice = 3
            make_text_correspondence(3)
            time.sleep(0.25)  
        
        event.x = 0
        event.y = 0
        
    if choice == 2:
        if 70 < event.x < 220 and 520 < event.y < 620: # press button
            choice = 4
            make_text_correspondence(4)
            time.sleep(0.25)
        if 780 < event.x < 930 and 520 < event.y < 620: # dont press button
            choice = 5
            make_text_correspondence(5)
            time.sleep(0.25)
            
        event.x = 0
        event.y = 0
        
    if choice == 3:
        if 70 < event.x < 220 and 520 < event.y < 620: # hug cactus
            choice = 6
            make_text_correspondence(6)
            time.sleep(0.25)
        if 780 < event.x < 930 and 520 < event.y < 620: # dont hug cactus
            choice = 7
            make_text_correspondence(7)
            time.sleep(0.25)
            
        event.x = 0
        event.y = 0
        
    if choice == 5:
        if 70 < event.x < 220 and 520 < event.y < 620: # hug cactus
            choice = 10
            make_text_correspondence(10)
            time.sleep(0.25)
        if 780 < event.x < 930 and 520 < event.y < 620: # dont hug cactus
            choice = 11
            make_text_correspondence(11)
            time.sleep(0.25)
            
    if choice == 6:
        if 70 < event.x < 220 and 520 < event.y < 620: # pop cactus
            choice = 8
            make_text_correspondence(8)
            time.sleep(0.25)
        if 780 < event.x < 930 and 520 < event.y < 620: # dont pop cactus
            choice = 9
            make_text_correspondence(9)
            time.sleep(0.25)
            
        event.x = 0
        event.y = 0

window.bind("<Button-1>",mouse_was_clicked)
make_text_correspondence(1)
window.mainloop()
