from tkinter import Canvas
from tkinter import Tk
from tkinter import *
import random
import time
import json
import math
choice = 1
global score
score = 0
# 1, 2, 3, 4
window = Tk()
window.title("Choose you own adventure | By Alfredo")

canvas = Canvas(window, width=1000, height=700,bg="white")
canvas.pack()

def make_text_correspondence(scene):
	canvas.delete("all")
	canvas.create_rectangle(250,500,750,650)
	canvas.create_rectangle(990,10,790,90)
	canvas.create_text(890,50,text="Retry", fill="black", font = ("Helvetica",40),anchor="center")
	
	
	if scene == 1: # fork in the road
		canvas.create_text(260,510,text="You are walking around and get lost in a forest. You ", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,535,text="spot a fork in the road. Go left or right.", fill="black", font = ("Helvetica",15),anchor="nw")
		make_choices(scene)
		make_background(scene)
	global score
	score = 69
	
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
		canvas.create_text(260,510,text="You pop the cactus and the kid pushes you off a cliff.  " ,fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,535,text="As you are falling you wonder how you failed to notice  ", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,560,text="the gigantic ledge that drops over 200 feet", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(500,250,text="YOU DIED!", fill="red", font = ("Helvetica",100),anchor="center")
	
	if scene == 9: # dont pop the cactus
		canvas.create_text(260,510,text="You decide that you dont want to pop the  ", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,535,text="cactus. You wonder where he got that ballon. Do you ", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,560,text=" investigate? ", fill="black", font = ("Helvetica",15),anchor="nw")
		make_choices(7)
		make_background(7)

	if scene == 10: # stay and talk
		canvas.create_text(260,510,text="You decide to stay and talk. The person catches up ", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,535,text="to you and asks you what you are doing here. He has", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,560,text="a pool noodle. You challenge him to a pool noodle ", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(258,585,text= "battle. Do you fight correctly and play fair or do", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(258,610,text= "put a metal bar in your pool noodle", fill="black", font = ("Helvetica",15),anchor="nw")
		make_choices(scene)
		make_background(scene)
		
	if choice == 11: # vamoose!
		canvas.create_text(260,510,text="You decide to run from the person. You see a big ", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,535,text=" cactus. for some reason,this cactus looks very", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,560,text="appealing. Hug the cactus?", fill="black", font = ("Helvetica",15),anchor="nw")
		make_choices(3)
		make_background(3)
		
	if choice == 12: # pool noodle
		canvas.create_text(260,510,text="You decide to fight correctly and charge at him with", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,535,text="your noodle. He dodges the first few blows but ", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,560,text="eventually you wear him out and land the finishing ", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(258,585,text= "blow. The spectators congratulate you because you", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(258,610,text= "have just won a 50% off McDonalds Coupon!", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(500,250,text="Ending #1", fill="light green", font = ("Helvetica",100),anchor="center")
		
	if choice == 13: # metal noodle
		canvas.create_text(260,510,text="You swing the pool noodle at your opponent. You miss " ,fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,535,text="them and swing around, smashing the tree with your   ", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,560,text="metal noodle, and your opponent is free to hit you. ", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,585,text="As they do, you realize you agreed that this pool ", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,610,text="noodle match was a pool noodle death match.", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(500,250,text="YOU DIED!", fill="red", font = ("Helvetica",100),anchor="center")
		
	if choice == 14: # waste of time	
		canvas.create_text(260,510,text="You decide that investigating is a waste of time, so you ", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,535,text="so you wander around until you find a rock. You remember", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,560,text="seeing a wanted poster for this rock with a totaling", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,585,text="reward of 4 dollars! Do you capture the rock and return", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,610,text= "it?", fill="black", font = ("Helvetica",15),anchor="nw")
		make_choices(scene)
		make_background(scene)
		
	if choice == 15: # investigate
		canvas.create_text(260,510,text="You decide to investige where he got the balloon, ", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,535,text="So you set off back into the deep dark woods. You", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,560,text="come across a balloon stand with a 99% discount.", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,585,text="Do you buy as many balloons you can for 1 cent to", fill="black", font = ("Helvetica",15),anchor="nw")
		canvas.create_text(260,610,text="spread the balloons to the people of the world?", fill="black", font = ("Helvetica",15),anchor="nw")
		make_choices(scene)
		make_background(scene)
		
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
	if choice == 10:
		canvas.create_text(795,540,text=" Metal ", fill="black", font = ("Helvetica",20),anchor="nw")
		canvas.create_text(830,565,text="Noodle!", fill="black", font = ("Helvetica",20),anchor="nw")
		canvas.create_text(85,540,text=" Pool ", fill="black", font = ("Helvetica",20),anchor="nw")
		canvas.create_text(120,565,text="Noodle!", fill="black", font = ("Helvetica",20),anchor="nw")
	if choice == 14:
		canvas.create_text(85,550,text="Capture!", fill="black", font = ("Helvetica",25),anchor="nw")
		canvas.create_text(820,540,text="Dont ", fill="black", font = ("Helvetica",20),anchor="nw")
		canvas.create_text(820,570,text="capture.", fill="black", font = ("Helvetica",20),anchor="nw")

		
	
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
	if 790 < event.x < 990 and 10 < event.y < 90:
		choice = 1
		
		event.x = 0
		event.y = 0
		make_text_correspondence(1) 
		
	
	990,10,790,90
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
		if 70 < event.x < 220 and 520 < event.y < 620: # stay and talk
			choice = 10
			make_text_correspondence(10)
			time.sleep(0.25)
		if 780 < event.x < 930 and 520 < event.y < 620: # Vamoose!
			choice = 11
			make_text_correspondence(11)
			time.sleep(0.25)
			
		event.x = 0
		event.y = 0
		
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
	
	if choice == 7:
		if 70 < event.x < 220 and 520 < event.y < 620: # waste of time
			choice = 14
			make_text_correspondence(14)
			time.sleep(0.25)
		if 780 < event.x < 930 and 520 < event.y < 620: # investigate
			choice = 15
			make_text_correspondence(15)
			time.sleep(0.25)
			
		event.x = 0
		event.y = 0	
		
	if choice == 10:
		if 70 < event.x < 220 and 520 < event.y < 620: # pool noodle
			choice = 12
			make_text_correspondence(12)
			time.sleep(0.25)
		if 780 < event.x < 930 and 520 < event.y < 620: # metal noodle
			choice = 13
			make_text_correspondence(13)
			time.sleep(0.25)
			
		event.x = 0
		event.y = 0
		
	if choice == 11:
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
		
	if choice == 7 or choice == 9:
		if 70 < event.x < 220 and 520 < event.y < 620: # waste of time
			choice = 14
			make_text_correspondence(14)
			time.sleep(0.25)
		if 780 < event.x < 930 and 520 < event.y < 620: # investigate
			choice = 15
			make_text_correspondence(15)
			time.sleep(0.25)
			
		event.x = 0
		event.y = 0

import rick_roll
rick_roll.rickroll()
		
window.bind("<Button-1>",mouse_was_clicked)
make_text_correspondence(1)
window.mainloop()
