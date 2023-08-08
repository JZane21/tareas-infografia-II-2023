def algoritmo_dda(x_0,y_0,x_1,y_1):
  x_r = x_1 - x_0
  x_r_mod = abs(x_r)
  y_r = y_1 - y_0
  y_r_mod = abs(y_r)
  
  longitud = 0
  
  if (x_r_mod >= y_r_mod):
    longitud = x_r_mod
  else:
    longitud = y_r_mod
  
  x_d = x_r / longitud
  y_d = y_r / longitud
  
  x = x_0 + 0.5 * ((-1) if x_d < 0 else 1)
  y = y_0 + 0.5 * ((-1) if x_d < 0 else 1)
  
  k = 1
  
  points_list = [(x_0, y_0)]
  
  while k <= longitud:
    point = (x,y)
    points_list.append(point)
    x += x_d
    y += y_d
    k += 1
  
  return points_list

if __name__ == "__main__":
  print(algoritmo_dda(5,7,10,3))