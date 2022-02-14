from turtle import Screen
from Paddle import Bats
import time
from ball import Ball
from scoreboard import score
r_paddle = Bats((350, 0))
l_paddle = Bats((-350, 0))
Game_ball = Ball()
Game_screen = Screen()
Game_score = score()
Game_screen.setup(height=600, width=800)
Game_screen.bgcolor("black")
Game_screen.title("Pong")
Game_screen.tracer(0)

Game_screen.listen()
Game_screen.onkey(r_paddle.go_up, "Up")
Game_screen.onkey(r_paddle.go_down, "Down")
Game_screen.onkey(l_paddle.go_up, "w")
Game_screen.onkey(l_paddle.go_down, "s")
Game_is_on = True

while Game_is_on:
    Game_screen.update()
    time.sleep(Game_ball.move_speed)
    Game_ball.move()

    if Game_ball.ycor()>280 or Game_ball.ycor() <-280:
        Game_ball.bounce_y()

    if Game_ball.distance(r_paddle)<50 and Game_ball.xcor()>330 or Game_ball.distance(l_paddle)<50 and Game_ball.xcor()<-330:
        Game_ball.bounce_x()

    if Game_ball.xcor()>380:
        Game_score.l_point()
        Game_ball.reset_ball()

    if Game_ball.xcor()<-380:
        Game_score.r_point()
        Game_ball.reset_ball()


Game_screen.exitonclick()
