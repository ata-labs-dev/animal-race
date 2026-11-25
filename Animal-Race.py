import turtle
import random
from os import chdir,path
import time
import pygame
chdir(path.dirname(__file__))
#first character is turtle , second is rabbit , third is snail and the fourth is frog
#------------------------------------------- menu click handling
def click_handle(x,y):
    if -68<x<68 and 155<y<188:#2 player mode
        player2_mode_start()
    elif -68<x<68 and 60<y<86:#3 player mode 
        player3_mode_start()
    elif -68<x<68 and -37<y<-16:#4 player mode 
        player4_mode_start()
    elif -30<x<30 and -140<y<-120:#quit
        exit()
#--------------------------------------------------------

#------------------------------------------------2 player mode
def player2_mode_start():
    turn = 1
    def reset_screen():
        screen.clearscreen()
        screen.bgpic("images/background.png")
        pen = turtle.Turtle()
        menu_items = [("2 Player",150),("3 Player",50),("4 Player",-50),("Quit",-150)]
        for text, y in menu_items:
            pen.hideturtle()
            pen.penup()
            pen.pencolor("white")
            pen.goto(0,y)
            pen.write(text,align="center",font=("Arial",26,"bold"),)
            screen.onclick(click_handle)
    def roll_the_dice(x,y):
        nonlocal turn
        dice_sound = pygame.mixer.Sound("sounds/dice.mp3")
        dice_sound.play()
        addad = random.randint(1,6)
        screen.addshape(f"images/dice{addad}.gif")
        dice_image.shape(f"images/dice{addad}.gif")
        if turn == 1:
            t1.forward(addad * 10)
            turn += 1
        elif turn == 2:
            t2.forward(addad * 10)
            turn -= 1
            if (t1.xcor() >= 407) and (t2.xcor() >= 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("Draw",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif (t1.xcor() >= 407) and (t2.xcor() < 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("turtle won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif (t2.xcor() >= 407) and (t1.xcor() < 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("rabbit won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
    screen.clearscreen()
    screen.bgpic("images/background_withfinishline.png")
    t1 = turtle.Turtle()
    screen.addshape("images/turtle1.gif")
    t1.shape("images/turtle1.gif")
    t2 = turtle.Turtle()
    screen.addshape("images/rabbit1.gif")
    t2.shape("images/rabbit1.gif")
    screen.addshape("images/nondice.gif")
    dice_image = turtle.Turtle()
    dice_image.shape("images/nondice.gif")
    dice_image.penup()
    dice_image.goto(0,200)
    dice_image.pendown()
    #407 is the end of the race
    t1.penup()
    t1.goto(-425,-100)
    t2.penup()
    t2.goto(-425,-200)
    pygame.mixer.music.load("sounds/background.mp3")
    pygame.mixer.music.play(-1)
    dice_image.onclick(roll_the_dice)
#---------------------------------------------------------------

#------------------------------------------------3 player mode
def player3_mode_start():
    turn = 1
    def reset_screen():
        screen.clearscreen()
        screen.bgpic("images/background.png")
        pen = turtle.Turtle()
        menu_items = [("2 Player",150),("3 Player",50),("4 Player",-50),("Quit",-150)]
        for text, y in menu_items:
            pen.hideturtle()
            pen.penup()
            pen.pencolor("white")
            pen.goto(0,y)
            pen.write(text,align="center",font=("Arial",26,"bold"),)
            screen.onclick(click_handle)
    def roll_the_dice(x,y):
        nonlocal turn
        dice_sound = pygame.mixer.Sound("sounds/dice.mp3")
        dice_sound.play()
        addad = random.randint(1,6)
        screen.addshape(f"images/dice{addad}.gif")
        dice_image.shape(f"images/dice{addad}.gif")
        if turn == 1:
            t1.forward(addad * 10)    
            turn += 1
        elif turn == 2:
            t2.forward(addad * 10)
            turn += 1
        elif turn == 3:
            t3.forward(addad * 10)
            turn = 1
            if (t1.xcor() >= 407 and t2.xcor() >= 407 and t3.xcor() >= 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("all won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif (t1.xcor() >= 407 and t2.xcor() >= 407) and (t3.xcor() < 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("turtle and rabbit won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif (t1.xcor() >= 407 and t3.xcor() >= 407) and (t2.xcor() < 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("turtle and snail won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif (t2.xcor() >= 407 and t3.xcor() >= 407) and (t1.xcor() < 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("rabbit and snail won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif t1.xcor() >= 407 and (t2.xcor() < 407 and t3.xcor() < 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("turtle won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif t2.xcor() >= 407 and ((t1.xcor() < 407) and (t3.xcor() < 407)):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("rabbit won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif t3.xcor() >= 407 and (t1.xcor() < 407  and t2.xcor() < 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("snail won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
    screen.clearscreen()
    screen.bgpic("images/background_withfinishline.png")
    t1 = turtle.Turtle()
    screen.addshape("images/turtle1.gif")
    t1.shape("images/turtle1.gif")
    t2 = turtle.Turtle()
    screen.addshape("images/rabbit1.gif")
    t2.shape("images/rabbit1.gif")
    t3 = turtle.Turtle()
    screen.addshape("images/snail1.gif")
    t3.shape("images/snail1.gif")
    screen.addshape("images/nondice.gif")
    dice_image = turtle.Turtle()
    dice_image.shape("images/nondice.gif")
    dice_image.penup()
    dice_image.goto(0,200)
    dice_image.pendown()
    #407 is the end of the race
    t1.penup()
    t1.goto(-425,-100)
    t2.penup()
    t2.goto(-425,-150)
    t3.penup()
    t3.goto(-425,-200)
    pygame.mixer.music.load("sounds/background.mp3")
    pygame.mixer.music.play(-1)
    dice_image.onclick(roll_the_dice)
#---------------------------------------------------------------

#------------------------------------------------4 player mode
def player4_mode_start():
    turn = 1
    def reset_screen():
        screen.clearscreen()
        screen.bgpic("images/background.png")
        pen = turtle.Turtle()
        menu_items = [("2 Player",150),("3 Player",50),("4 Player",-50),("Quit",-150)]
        for text, y in menu_items:
            pen.hideturtle()
            pen.penup()
            pen.pencolor("white")
            pen.goto(0,y)
            pen.write(text,align="center",font=("Arial",26,"bold"),)
            screen.onclick(click_handle)
    def roll_the_dice(x,y):
        nonlocal turn
        dice_sound = pygame.mixer.Sound("sounds/dice.mp3")
        dice_sound.play()
        addad = random.randint(1,6)
        screen.addshape(f"images/dice{addad}.gif")
        dice_image.shape(f"images/dice{addad}.gif")
        if turn == 1:
            t1.forward(addad * 10)
            turn += 1
        elif turn == 2:
            t2.forward(addad * 10)
            turn += 1 
        elif turn == 3:
            t3.forward(addad * 10)
            turn += 1
        elif turn == 4:
            t4.forward(addad * 10)
            turn = 1
            if t1.xcor() >= 407 and t2.xcor() >= 407 and t3.xcor() >= 407 and t4.xcor() >= 407:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("all won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif(t1.xcor() >= 407 and t2.xcor() >= 407 and t3.xcor() >= 407) and t4.xcor()< 407:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("turtle , rabbit and snail won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif(t1.xcor() >= 407 and t2.xcor() >= 407 and t4.xcor() >= 407) and t3.xcor()< 407:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("turtle , rabbit and frog won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif(t1.xcor() >= 407 and t3.xcor() >= 407 and t4.xcor() >= 407) and t2.xcor()< 407:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("turtle , snail and frog won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif(t2.xcor() >= 407 and t3.xcor() >= 407 and t4.xcor() >= 407) and t1.xcor()< 407:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("rabbit , snail and frog won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif(t1.xcor() >= 407 and t2.xcor() >= 407) and (t3.xcor() < 407 and t4.xcor() < 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("turtle and rabbit won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif(t1.xcor() >= 407 and t3.xcor() >= 407) and (t2.xcor() < 407 and t4.xcor() < 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("turtle and snail won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif(t1.xcor() >= 407 and t4.xcor() >= 407) and (t2.xcor() < 407 and t3.xcor() < 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("turtle and frog won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif(t2.xcor() >= 407 and t3.xcor() >= 407) and (t1.xcor() < 407 and t4.xcor() < 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("rabbit and snail won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif(t2.xcor() >= 407 and t4.xcor() >= 407) and (t1.xcor() < 407 and t3.xcor() < 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("rabbit and frog won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif(t3.xcor() >= 407 and t4.xcor() >= 407) and (t1.xcor() < 407 and t2.xcor() < 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("snail and frog won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif(t1.xcor() >= 407) and (t2.xcor() < 407 and t3.xcor() < 407 and t4.xcor() < 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("turtle won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif(t2.xcor() >= 407) and (t1.xcor() < 407 and t3.xcor() < 407 and t4.xcor() < 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("rabbit won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif(t3.xcor() >= 407) and (t1.xcor() < 407 and t2.xcor() < 407 and t4.xcor() < 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("snail won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
            elif(t4.xcor() >= 407) and (t1.xcor() < 407 and t2.xcor() < 407 and t3.xcor() < 407):
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                writer = turtle.Turtle()
                writer.hideturtle()
                writer.penup()
                writer.goto(0,0)
                writer.write("frog won",align="center",font=("Arial",38,"bold"))
                #going back to the menu
                dice_image.onclick(None)
                screen.ontimer(reset_screen,4000)
                return
    screen.clearscreen()
    screen.bgpic("images/background_withfinishline.png")
    t1 = turtle.Turtle()
    screen.addshape("images/turtle1.gif")
    t1.shape("images/turtle1.gif")
    t2 = turtle.Turtle()
    screen.addshape("images/rabbit1.gif")
    t2.shape("images/rabbit1.gif")
    t3 = turtle.Turtle()
    screen.addshape("images/snail1.gif")
    t3.shape("images/snail1.gif")
    t4 = turtle.Turtle()
    screen.addshape("images/frog1.gif")
    t4.shape("images/frog1.gif")
    screen.addshape("images/nondice.gif")
    dice_image = turtle.Turtle()
    dice_image.shape("images/nondice.gif")
    dice_image.penup()
    dice_image.goto(0,200)
    dice_image.pendown()
    #407 is the end of the race
    t1.penup()
    t1.goto(-425,-75)
    t2.penup()
    t2.goto(-425,-125)
    t3.penup()
    t3.goto(-425,-175)
    t4.penup()
    t4.goto(-425,-225)
    pygame.mixer.music.load("sounds/background.mp3")
    pygame.mixer.music.play(-1)
    dice_image.onclick(roll_the_dice)
#---------------------------------------------------------------
pygame.mixer.init()
screen = turtle.Screen()
screen.setup(911,516)
screen.screensize(900,507)
screen.title("Animal-Race")
screen._root.resizable(False,False)
screen.bgpic("images/background.png")
pen = turtle.Turtle()
menu_items = [("2 Player",150),("3 Player",50),("4 Player",-50),("Quit",-150)]
for text, y in menu_items:
    pen.hideturtle()
    pen.penup()
    pen.pencolor("white")
    pen.goto(0,y)
    pen.write(text,align="center",font=("Arial",26,"bold"),)
#BUTTON PLACES /2= x:68,-68 y:188,155|3= x:68,-68 y:86,60|4= x:68,-68 y=-16,-37|quit=x:30,-30 y:-120,-140
screen.onclick(click_handle)
turtle.done()