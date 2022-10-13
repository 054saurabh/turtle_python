import turtle as t
import timer 
import random as r

sc=t.getscreen()
sc.bgcolor("black")
sc.title("project1")

chotu=t.Turtle()
chotu.hideturtle()
chotu.speed(6)
sc.tracer(4,10)


def pattern():
    for i in range(40):  
        chotu.color("red")     
        chotu.circle(4.5*i)
        chotu.color("yellow")
        chotu.circle(-4.5*i)
        chotu.color("green")
        chotu.left(15)
    chotu.up()
    chotu.home()
    chotu.down()

def star():
    for i in range(200):
        chotu.color("green")
        x=r.randint(-500,500)
        y=r.randint(-500,500)
        chotu.penup()
        chotu.goto(x,y)
        print(x,y)
        chotu.pendown()
        chotu.begin_fill()
        for i in range(5):
            chotu.fd(20)
            chotu.left(144)
        chotu.end_fill()
        print("one star is completed")
        
def star1():
    for i in range(300):
        chotu.color("white")
        x=r.randint(-1000,1000)
        y=r.randint(-1000,1000)
        chotu.penup()
        chotu.goto(x,y)
        print(x,y)
        chotu.pendown()
        chotu.begin_fill()
        for i in range(5):
            chotu.fd(20)
            chotu.left(144)
        chotu.end_fill()
        print("one star is completed")

def star2():
    for i in range(150):
        chotu.color("red")
        x=r.randint(-1000,1000)
        y=r.randint(-1000,1000)
        chotu.penup()
        chotu.goto(x,y)
        print(x,y)
        chotu.pendown()
        chotu.begin_fill()
        for i in range(5):
            chotu.fd(20)
            chotu.left(144)
        chotu.end_fill()
        print("one star is completed")


sc.listen()
pattern()
star()
star1()
star2()
sc.mainloop()

