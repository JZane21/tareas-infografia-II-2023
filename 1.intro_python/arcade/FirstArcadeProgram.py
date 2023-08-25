import arcade
import subprocess
comando = "clear"
subprocess.run(comando, shell=True, capture_output=False, text=False)

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Holiwis Arcade :D"

# def Bresenham():
#   pass

def get_line(x0, y0, x1, y1):
  points = [(x0, y0)]
  d_x = x1 - x0
  d_y = y1 - y0
  
  x_k = x0
  y_k = y0
  
  p_k = 2 * d_x - d_y
  
  while x_k < x1:
    x_k += 1
    if p_k < 0:
      p_k += 2 * d_y
    else:
      y_k += 1
      p_k +=2 * d_y - 2 * d_x
    points.append((x_k,y_k))
  return points

if __name__ == "__main__":

  print(get_line(0,0,7,2))
  # arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
  
  # #fondo de pantalla
  # arcade.set_background_color(arcade.color.WHITE)
  # #iniciar render
  # arcade.start_render()

  # #para dibujar
  # arcade.draw_circle_filled(100, 100, 50, arcade.color.RED)
  # arcade.draw_rectangle_filled(450, 300, 50, 50, arcade.color.AERO_BLUE)
  # arcade.draw_ellipse_filled(400, 500, 100, 50, arcade.color.AFRICAN_VIOLET)
  # arcade.draw_ellipse_outline(400, 500, 200, 50, arcade.color.BLACK_LEATHER_JACKET, 1, 0, -1)
  # arcade.finish_render()

  # arcade.run()