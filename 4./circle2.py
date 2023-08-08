def get_circle(xc, yc, r):
  x = 0
  y = r
  p_k = 3 - 2 * r
  points = [(xc,yc),(x,y)]

  while x <= y:
    x += 1
    if p_k < 0:
      p_k += (4*x) + 6
    else:
      p_k -= ((-4)*(x-y))+10
      y -= 1
    points.append((x,y))

  return points
