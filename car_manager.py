import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_NEW_CAR_POSITION = 300
Y_LIMIT_LOW = -250
Y_LIMIT_HIGH = 250

class CarManager:
    cars = []

    def __init__(self):
        self.cars = []

    def add_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(1,2)
        x = X_NEW_CAR_POSITION
        y = random.randint(Y_LIMIT_LOW, Y_LIMIT_HIGH)
        new_car.goto(x,y)
        self.cars.append(new_car)


    def move_cars(self):
        for car in (self.cars):
            x = car.xcor()- MOVE_INCREMENT
            y = car.ycor()
            car.goto(x,y)
            if x < -300:
                # print("Car to be removed")
                car.hideturtle()
                self.cars.remove(car)

    def check_collision(self, player):
        for car in (self.cars):
            #if abs(car.xcor()-x)<20 and abs(car.ycor()-y)<20:
            #print(f"Distance: {car.distance(player)}")
            if car.distance(player) < 20:
                return True
        return False


