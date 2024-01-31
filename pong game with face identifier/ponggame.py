import arcade

from ball import Ball
from rocket import Rocket

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=500, title= "Pong 2023 🏓")
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.rocket1=Rocket(40, self.height//2, arcade.color.RED, "MARYAM")
        self.rocket2=Rocket(self.width-40, self.height//2, arcade.color.BLUE_GREEN, "YOUSOF")
        self.ball=Ball(self)



    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(self.width//2, self.height//2, self.width-30,
                                     self.height-30, arcade.color.WHITE, border_width=10)
        
        #arcade.draw_line(self.width//2, 30, self.width//2, self.height-30,
        #                arcade.color.WHITE, line_width=10)

        for i in range(19):
            arcade.draw_line(self.width//2, 20+25*i, self.width//2, 40+25*i, arcade.color.WHITE, line_width=10)


        self.rocket1.draw()
        self.rocket2.draw()
        self.ball.draw()

        arcade.draw_text(f"{self.rocket1.name}'s Score: {self.rocket1.score}", 2*self.width//10, 25 , arcade.color.RED, 10, bold= True)
        arcade.draw_text(f"{self.rocket2.name}'s Score: {self.rocket2.score}", 7*self.width//10, 25 , arcade.color.BLUE_GREEN, 10, bold= True)
        
        arcade.finish_render()


    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if 2*self.rocket1.height//3 < y < self.height-2*self.rocket1.height//3:
            self.rocket1.center_y=y

    def on_update(self, delta_time: float):

        self.ball.move()
        self.rocket2.move(self, self.ball)

        if self.ball.center_y<30 or self.ball.center_y > self.height-30:
            self.ball.change_y *= -1

        if arcade.check_for_collision(self.ball, self.rocket1):
            self.ball.change_x = 1


        if arcade.check_for_collision(self.ball, self.rocket2):
            self.ball.change_x = -1

        if self.ball.center_x < 0:
            self.rocket2.score += 1
            print("Goal!")
            del self.ball
            self.ball=Ball(self)
            self.ball.change_x = +1

        if self.ball.center_x > self.width:
            self.rocket1.score += 1
            print("Goal!")
            del self.ball
            self.ball=Ball(self)
            self.ball.change_x = -1




        

# game=Game()
# arcade.run()