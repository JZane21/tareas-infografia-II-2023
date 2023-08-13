import arcade
import random
from app_objects import Tank, HidePlace, Polygon2D

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
        self.tank = Tank(200, 200, SCREEN_WIDTH, SCREEN_HEIGHT,get_random_color())
        self.tank2 = Tank(600, 600, SCREEN_WIDTH, SCREEN_HEIGHT,get_random_color())
        self.hide_places = [
            HidePlace(
                random.randrange(0, SCREEN_WIDTH),
                random.randrange(0, SCREEN_HEIGHT-150),
                random.randrange(15, 60)
            )
            for _ in range(7)
        ]
        
        self.limitGame = Polygon2D(
            [
                (2,698),
                (798,698),
                (798,2),
                (2,2)
            ],
            arcade.color.REDWOOD
        )
        self.lifeZoneOne = Polygon2D(
            [
                (2,790),
                (300,790),
                (300,750),
                (2,750),
            ],
            arcade.color.GREEN
        )
        self.lifePositionsOne = [
            (50,770),
            (100,770),
            (150,770),
            (200,770),
            (250,770),
        ]
        
        self.lifeZoneTwo = Polygon2D(
            [
                (798,790),
                (490,790),
                (490,750),
                (798,750),
            ],
            arcade.color.GREEN
        )
        self.lifePositionsTwo = [
            (750,770),
            (700,770),
            (650,770),
            (600,770),
            (550,770),
        ]

    '''
    symbol: int
    modifiers: int
    '''
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.W:
            self.tank.speed = SPEED
        if symbol == arcade.key.S:
            self.tank.speed = -SPEED
        if symbol == arcade.key.A:
            self.tank.angular_speed = 1.5
        if symbol == arcade.key.D:
            self.tank.angular_speed = -1.5
        if  symbol == arcade.key.E:
            self.tank.shoot("normal")
        if symbol == arcade.key.Q:
            self.tank.shoot("bigger")
            
        if symbol == arcade.key.I:
            self.tank2.speed = SPEED
        if symbol == arcade.key.K:
            self.tank2.speed = -SPEED
        if symbol == arcade.key.J:
            self.tank2.angular_speed = 1.5
        if symbol == arcade.key.L:
            self.tank2.angular_speed = -1.5
        if symbol == arcade.key.U:
            self.tank2.shoot("normal")
        if symbol == arcade.key.O:
            self.tank2.shoot("bigger")
    '''
    symbol: int
    modifiers: int
    '''
    def on_key_release(self, symbol, modifiers):
        if symbol in (arcade.key.W, arcade.key.S):
            self.tank.speed = 0
        if symbol in (arcade.key.A, arcade.key.D):
            self.tank.angular_speed = 0
        if symbol == arcade.key.E:
            if len(self.tank.bullets) >= 61:
                self.tank.bullets[0:30] = []
                
        if symbol in (arcade.key.I, arcade.key.K):
            self.tank2.speed = 0
        if symbol in (arcade.key.J, arcade.key.L):
            self.tank2.angular_speed = 0
        if symbol == arcade.key.U:
            if len(self.tank2.bullets) >= 61:
                self.tank2.bullets[0:30] = []
                
    '''
    delta_time: float
    '''
    def on_update(self, delta_time):
        self.tank.update(delta_time)
        self.tank2.update(delta_time)
        for e in self.hide_places:
            e.detect_collision(self.tank)
            e.detect_collision(self.tank2)
        self.tank.detect_attack(self.tank2)
        self.tank2.detect_attack(self.tank)
        
    def on_draw(self):
        arcade.start_render()
        
        self.tank2.draw()
        self.tank.draw()
        
        for e in self.hide_places:
            e.draw()
        arcade.draw_rectangle_filled(2,750,1600,100,arcade.color.BLUEBERRY)
        self.lifeZoneOne.draw()
        index_one = 1
        if len(self.lifePositionsOne) > 0:
            for i in self.lifePositionsOne:
                if index_one <= self.tank.lifes:
                    arcade.draw_circle_filled(i[0],i[1],15,arcade.color.GREEN)
                else:
                    break
                index_one += 1
        # [
        #     (2,790),
        #     (300,790),
        #     (300,750),
        #     (2,750),
        # ],
        arcade.draw_text("Jugador 1",80,715,arcade.color.WHITE, font_size=20, anchor_x="center")
        
        self.lifeZoneTwo.draw()
        index_two = 1
        if len(self.lifePositionsTwo) > 0:
            for i in self.lifePositionsTwo:
                if index_two <= self.tank2.lifes:
                    arcade.draw_circle_filled(i[0],i[1],15,arcade.color.GREEN)
                else:
                    break
                index_two += 1
        
        arcade.draw_text("Jugador 2",720,715,arcade.color.WHITE, font_size=20, anchor_x="center")
        
        self.limitGame.draw()

        if self.tank.lifes <=0 or self.tank2.lifes <=0:
            arcade.draw_rectangle_filled(0,0,SCREEN_WIDTH*2,SCREEN_HEIGHT*2,arcade.color.BLACK)
            arcade.draw_text(f"¡Ganó el jugador {(1 if self.tank2.lifes <=0 else 2)}!",
                            SCREEN_WIDTH//2, SCREEN_HEIGHT//2,
                            arcade.color.ROSE, font_size=30, anchor_x="center")
            self.set_exclusive_keyboard(True)
    
if __name__ == "__main__":
    app = App()
    arcade.run()