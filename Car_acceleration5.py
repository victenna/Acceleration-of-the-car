import turtle,time,math
wn=turtle.Screen()
wn.setup(1300,800)
wn.bgpic('_background_.gif')
FONT=('Times New Roman',20,'bold')
turtle.tracer(2)
t4=turtle.Turtle('square')
t4.up()
t4.hideturtle()
t4.shapesize(1,200)
t4.color('brown')
t4.goto(-500,-143)
t4.showturtle()
turtle.tracer(3)

images=['image_0.gif','image_11_.gif','image_12_.gif',\
        'image_13_.gif','image4.gif']
for i in range(5):
    wn.addshape(images[i])
    
car=turtle.Turtle()
car.up()
car.goto(-450,0)
car.shape(images[0])
t1=turtle.Turtle('turtle')
t1.hideturtle()
t1.penup()
t1.begin_poly()
t1.fd(110)
t1.left(90)
t1.circle(15.358)
t1.fd(4)
t1.left(90)
t1.fd(110)
t1.end_poly()
wn.addshape('pend',t1.get_poly())
t2=turtle.Turtle(shape='pend')
t2.up()
t2.color('blue')
t2.goto(-480,100)
t2.hideturtle()
t3=turtle.Turtle()
t3.up()
t3.goto(300,280)
t3.shape(images[4])

t4=turtle.Turtle()
t4.up()
t4.hideturtle()
t4.goto(-11,-279)




FONT=('Times New Roman',20,'bold')
a=float(wn.textinput('Движение с ускорением',\
                         'Введите величину a/g '))
a1=a*180/3.14159
teta=math.atan(float(a))
teta=teta*180/3.14
teta1=round(teta,1)

t4.write(teta1,font=FONT)
print('Teta=',teta)
t2.hideturtle()

t2.rt(teta)

n=0
q=0
q1=0
wn.bgpic('_background_1.gif')
for j in range(3):
    t2.hideturtle()
    t2.goto(-480,100)
    t2.showturtle()
    car.goto(-450,0)
    x=0
    while x<900:
        
        t2.sety(100)
        
        for i in range(5):
            q=q+1
            n=n+1
            car.shape(images[3])
            car.fd(a*(2*n-1)/200)
            t2.setposition(-480+a*((q*q-q1*q1)/200),105)
            time.sleep(0.001)           
        for i in range(5):
            q=q+1
            n=n+1
            car.shape(images[2])
            car.fd(a*(2*n-1)/200)
            t2.setposition(-480+a*((q*q-q1*q1)/200),105)
            time.sleep(0.001)
           
        for i in range(5):
            q=q+1
            n=n+1
            car.shape(images[1])
            car.fd(a*(2*n-1)/200)
            t2.setposition(-480+a*((q*q-q1*q1)/200),105)
            time.sleep(0.001)
        
        x=car.xcor()
        
    q1=q
t4.clear()
wn.bgpic('_background_2.gif')   
    

        
   






