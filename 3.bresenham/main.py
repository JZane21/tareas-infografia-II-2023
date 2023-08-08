import arcade
from mod_bresenham import get_line
from alg_dda import algoritmo_dda

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# SCREEN_TITLE = "Lineas con bresenham"
SCREEN_TITLE = "Lineas con DDA"

class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pixel_size = 20

    def on_draw(self):
        arcade.start_render()
        points = get_line(5,7,10,3)
        self.draw_grid()
        self.draw_line_points(points, arcade.color.DARK_YELLOW)
        self.draw_scaled_line(5,7,10,3)

    def draw_grid(self):
        # lineas verticales
        for v_l in range(0, SCREEN_WIDTH, self.pixel_size):
            arcade.draw_line(
                v_l + self.pixel_size / 2, 
                0, 
                v_l + self.pixel_size / 2, 
                SCREEN_HEIGHT, 
                arcade.color.DARK_GRAY
            )

        for h_l in range(0, SCREEN_HEIGHT, self.pixel_size):
            arcade.draw_line(
                0, 
                h_l + self.pixel_size / 2, 
                SCREEN_WIDTH, 
                h_l + self.pixel_size / 2, 
                arcade.color.LIGHT_GRAY
            )

    def draw_line_points(self, points,  color):
        for p in points:
            arcade.draw_point(p[0] * self.pixel_size, p[1] * self.pixel_size, color, self.pixel_size)

    def draw_scaled_line(self, x0, y0, x1, y1):
        arcade.draw_line(
            x0 * self.pixel_size, 
            y0 * self.pixel_size, 
            x1 * self.pixel_size, 
            y1 * self.pixel_size,
            [100, 255, 40, 150],
            5
        )

'''
correo: eduardolaruta+tareas@gmail.com
Infografia_1_carrasco
Infografia_2_carrasco

Tarea 1:
debe ser un archivo.zip, donde debe tener el archivo estudiantes.py
Tarea 2:
// bresenham.py
'''

if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()
