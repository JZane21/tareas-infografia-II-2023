import arcade
import numpy as np
import random
from game_object import Object3D

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Projeccion 3d"


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
        # self.cube = Object3D(
        #     [
        #         (1, 1, 1),
        #         (1, 1, -1),
        #         (1, -1, 1),
        #         (1, -1, -1),
        #         (-1, 1, 1),
        #         (-1, 1, -1),
        #         (-1, -1, 1),
        #         (-1, -1, -1),
        #     ],
        #     [
        #         (0, 1),
        #         (1, 3),
        #         (2, 3),
        #         (2, 0),
        #         (4, 5),
        #         (5, 7),
        #         (6, 7),
        #         (6, 4),
        #         (0, 4),
        #         (1, 5),
        #         (2, 6),
        #         (3, 7)
        #     ],
        #     arcade.color.YELLOW
        # )
        # self.cube.translate(399, 399, 0)
        # self.cube.scale(100, 100, 100)
        # self.cube.rotate(0.1, "x")
        # self.cube.rotate(0.3, "y")
        # self.cube.rotate(0.1, "z")
        
        self.triangle = Object3D(
            [
                (1,2,0),
                (0,0,1),
                (2,0,1),
                (0,0,-1),
                (2,0,-1)
            ],
            [
                (0,1),
                (0,2),
                (0,3),
                (0,4),
                (1,2),
                (1,3),
                (4,3),
                (4,2)
            ],
            arcade.color.ROSE
        )
        self.triangle.translate(399, 399, 0)
        self.triangle.scale(100, 100, 100)
        self.triangle.rotate(0.1, "x")
        self.triangle.rotate(0.1, "y")
        self.triangle.rotate(0.1, "z")
    
    def on_update(self, delta_time: float):
        self.triangle.rotate(delta_time, "y")
        pass

    def on_draw(self):
        arcade.start_render()
        self.triangle.draw()
    
    
if __name__ == "__main__":
    app = App()
    arcade.run()