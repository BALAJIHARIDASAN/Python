import turtle   #allow us to turtle library

cn = turtle.Screen() #create the graphic window

alex=turtle.Turtle()   #create the name alex/dictionary
alex.forward(150)    #tell the turtle to move forward by 150/method
alex.right(90)      # to turn right
alex.forward(250)
alex.right(90)

###############################################################################


wn = turtle.Screen() #create the graphic window
wn.bgcolor('yellow')   #background color

bala=turtle.Turtle()   #create the name alex
bala.pencolor('green')  #pencolor
bala.pensize(10)   #penwidth
bala.color('red') #pen color
bala.shape('turtle')  #shape of the pen
# To make the rectangle
bala.forward(150)    #tell the turtle to move forward by 150
bala.right(90)      # to turn right
bala.forward(250)
bala.right(90)
bala.forward(150)
bala.right(90)
bala.forward(250)


wn.exitonclick() #click on window to exit the program

#################################################################

# for loop - iteration is done mutliple times

bn= turtle.Screen() #create the graphic window
bn.bgcolor('green')   #background color
bn = turtle.Turtle()

dis = 50
for _ in range(10):
    bn.forward(dis)
    bn.right(90)
    dis =dis+10


#################################################################333



