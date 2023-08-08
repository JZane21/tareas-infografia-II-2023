
def get_line(x0, y0, x1, y1):
  d_x = x1 - x0
  d_x *= (1 if d_x>=0 else -1)
  d_y = y1 - y0 
  d_y *= (1 if d_y>=0 else -1)
  x_k = x0
  y_k = y0
  x_increment = 1 if x1 > x0 else -1
  y_increment = 1 if y1 > y0 else -1
  points = [(x0, y0)]

  if d_x >= d_y:
    p_k = 2 * d_y - d_x
    for i in range(d_x):
      x_k += x_increment
      p_k += 2 * d_y if p_k < 0 else 2 * (d_y - d_x)
      y_k += 0 if p_k < 0 else  y_increment
      points.append((x_k, y_k))
  else:
    p_k = 2 * d_x - d_y
    for i in range(d_y):
      y_k += y_increment
      p_k += 2 * d_x if p_k < 0 else 2 * (d_x - d_y)
      x_k += 0 if p_k < 0 else x_increment
      points.append((x_k, y_k))
  return points

if __name__ == "__main__":
    print(get_line(2, 2, 10, 5))