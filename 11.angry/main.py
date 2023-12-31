import math

import arcade
import pymunk

from game_object import Bird, Column, Pig

WIDTH = 1800
HEIGHT = 800
TITLE = "Angry birds"


class App(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.LIGHT_GREEN)
        # crear espacio de pymunk
        self.space = pymunk.Space()
        self.space.gravity = (0, -900)

        # agregar piso
        floor_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        floor_shape = pymunk.Segment(floor_body, [0, 50], [WIDTH, 50], 0.0)
        floor_shape.friction = 10
        self.space.add(floor_body, floor_shape)

        self.sprites = arcade.SpriteList()
        self.birds = arcade.SpriteList()
        self.world = arcade.SpriteList()
        self.add_columns()
        self.add_pigs()

        self.start_point = ()
        self.end_point = ()
        self.distance = 0
        self.draw_line = False

        # agregar un collision handler
        self.handler = self.space.add_default_collision_handler()
        self.handler.begin = self.coll_begin
        
    def coll_begin(self, arbiter, space, data):
        impulse_norm = arcade.get_distance(0, 0, arbiter.total_impulse.x, arbiter.total_impulse.y)
        # print(impulse_norm)
        if impulse_norm > 250:
            for o in self.world:
                if o.shape in arbiter.shapes:
                    print(o.shape)
                    o.remove_from_sprite_lists()
                    self.space.remove(o.shape, o.body)

        return True

    def add_columns(self):
        for x in range(WIDTH // 2, WIDTH, 50):
            column = Column(x, 100, self.space)
            self.sprites.append(column)
            self.world.append(column)

    def add_pigs(self):
        pig1 = Pig(WIDTH / 2, 100, self.space)
        self.sprites.append(pig1)
        self.world.append(pig1)

    def on_update(self, delta_time: float):
        self.space.step(1 / 60)
        self.sprites.update()
        for sprite in self.sprites:
            sprite.update()

    def update_collisions(self):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.start_point = (x,y)
            self.end_point = (x,y)
            print(f"START: ( {self.start_point[0]} , {self.start_point[1]} )")

    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int):
        if buttons == arcade.MOUSE_BUTTON_LEFT:
            self.end_point = (x,y)
            self.draw_line = True
            print(f"END: ( {self.end_point[0]} , {self.end_point[1]} )")

    def calcular_angulo(self,x1:int,y1:int,x2:int,y2:int):
        return math.atan((y2-y1)/(x2-x1))

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            print("release")
            X1 = self.start_point[0]
            Y1 = self.start_point[1]
            X2 = self.end_point[0]
            Y2 = self.end_point[1]
            self.draw_line = False
            angulo = self.calcular_angulo(
                X1 , Y1,
                X2 , Y2
            )
            bird = Bird("11.angry/assets/img/red-bird3.png", math.sqrt((X2-X1)**2 + (Y2-Y1)**2), angulo,
                        X1, Y1, self.space)
            self.sprites.append(bird)
            self.birds.append(bird)

    def on_draw(self):
        arcade.start_render()
        self.sprites.draw()
        if self.draw_line:
            arcade.draw_line(self.start_point[0], self.start_point[1], self.end_point[0], self.end_point[1], arcade.color.BROWN, 5)


def main():
    app = App()
    arcade.run()


if __name__ == "__main__":
    main()
