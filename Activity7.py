import turtle
import tkinter.simpledialog as simpledialog

#diagram 1:
turtle.speed(1)
turtle.pensize(3)
turtle.pencolor('blue')
turtle.forward (100)
turtle.right (90)
turtle.forward (50)
turtle.left (90)

#changing location
turtle.penup()
turtle.forward (60)

#diagram 2:circle
turtle.pendown()
turtle.speed(10) 
turtle.circle (25)
turtle.dot (10, "blue")
turtle.setheading(0)

turtle.hideturtle()
turtle.speed(1)   #changing the speed to the slowest 
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

import time
time.sleep(2)
turtle.clear()
turtle.reset()
turtle.hideturtle()
turtle.showturtle()
turtle.speed(1)
turtle.write("Hi! What's your name?")

time.sleep(2) #dealy the popup by 2 second
name= turtle.textinput('Input','Enter your name')
turtle.clearscreen()
turtle.write(f'Bye {name}!')
turtle.mainloop() #to make the window close only after you have clicked 
