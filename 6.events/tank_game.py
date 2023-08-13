import arcade
import random
from app_objects import Tank, Enemy, Polygon2D

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Tank Game"

SPEED = 10

def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.rot_speed = 0.5
        self.speed = 10
        self.tank = Tank(600, 600, SCREEN_WIDTH, SCREEN_HEIGHT,get_random_color())
        self.tank2 = Tank(200, 200, SCREEN_WIDTH, SCREEN_HEIGHT,get_random_color())
        self.enemies = [
            Enemy(
                random.randrange(0, SCREEN_WIDTH),
                random.randrange(0, SCREEN_HEIGHT-150),
                random.randrange(15, 60)
            )
            for _ in range(7)
        ]
        
    '''
    x: int
    y: int
    button: int
    modifiers: int
    '''
    def on_mouse_release(self, x, y, button, modifiers):
        # self.tank.shoot(20)
        if len(self.tank.bullets) >= 51:
            self.tank.bullets[0:1]=[]

    def on_mouse_press(self, x, y, button, modifiers):
        self.tank.shoot(20)

    '''
    symbol: int
    modifiers: int
    '''
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.tank.speed = SPEED
        if symbol == arcade.key.DOWN:
            self.tank.speed = -SPEED
        if symbol == arcade.key.LEFT:
            self.tank.angular_speed = 1.5
        if symbol == arcade.key.RIGHT:
            self.tank.angular_speed = -1.5
            
        if symbol == arcade.key.W:
            self.tank2.speed = SPEED
        if symbol == arcade.key.S:
            self.tank2.speed = -SPEED
        if symbol == arcade.key.A:
            self.tank2.angular_speed = 1.5
        if symbol == arcade.key.D:
            self.tank2.angular_speed = -1.5
        if symbol == arcade.key.Q or symbol == arcade.key.E:
            self.tank2.shoot(20)
    '''
    symbol: int
    modifiers: int
    '''
    def on_key_release(self, symbol, modifiers):
        if symbol in (arcade.key.UP, arcade.key.DOWN):
            self.tank.speed = 0
        if symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.tank.angular_speed = 0

        if symbol in (arcade.key.W, arcade.key.S):
            self.tank2.speed = 0
        if symbol in (arcade.key.A, arcade.key.D):
            self.tank2.angular_speed = 0
            
        if symbol in (arcade.key.Q, arcade.key.E):
            if len(self.tank2.bullets) >= 51:
                self.tank2.bullets[0:1] = []
    '''
    delta_time: float
    '''
    def on_update(self, delta_time):
        self.tank.update(delta_time)
        self.tank2.update(delta_time)
        for e in self.enemies:
            e.detect_collision(self.tank)
            e.detect_collision(self.tank2)
        
    def on_draw(self):
        arcade.start_render()
        limitGame = Polygon2D(
            [
                (2,698),
                (798,698),
                (798,2),
                (2,2)
            ],
            arcade.color.REDWOOD
        )
        lifeZoneOne = Polygon2D(
            [
                (2,790),
                (300,790),
                (300,710),
                (2,710),
            ],
            arcade.color.GREEN
        )
        lifeZoneTwo = Polygon2D(
            [
                (798,790),
                (490,790),
                (490,710),
                (798,710),
            ],
            arcade.color.GREEN
        )
        lifeZoneOne.draw()
        lifeZoneTwo.draw()
        limitGame.draw()
        
        self.tank.draw()
        self.tank2.draw()
        
        for e in self.enemies:
            e.draw()
    
    
if __name__ == "__main__":
    app = App()
    arcade.run()