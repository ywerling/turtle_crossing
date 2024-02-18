import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()
score = Scoreboard()
loops = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Road Trip")
screen.tracer(0)
screen.onkey(player.up,"Up")
screen.update()
screen.listen()

car_manager.add_car()

game_is_on = True
while game_is_on:
    car_manager.move_cars()
    loops += 1
    if (loops % 6) == 0:
        car_manager.add_car()
    collision = car_manager.check_collision(player)
#    collision = car_manager.check_collision(player.xcor(), player.ycor())
    if collision:
        print("Game over!")
        score.game_over()
        game_is_on = False
    time.sleep(0.1)
    if player.ycor()>280:
        player.start()
        score.next_level()
    screen.update()

screen.exitonclick()
