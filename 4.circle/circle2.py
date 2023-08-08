def get_symetry_points(x0,y0,x1,y1):
    return [
        (x0+x1,y0+y1),
        (x0+x1,y0-y1),
        (x0-x1,y0+y1),
        (x0-x1,y0-y1),
        (x0+y1,y0+x1),
        (x0+y1,y0-x1),
        (x0-y1,y0+x1),
        (x0-y1,y0-x1)
    ]

def get_circle(xc, yc, r):
    x = 0
    y = r
    Pk = 3 - 2 * r
    points = []
    points += get_symetry_points(xc,yc,x,y)
    while x <= y:
        x += 1
        if Pk < 0:
            Pk += (4 * x) + 6
        else:
            Pk += 4 * (x - y) + 10
            y -= 1
        points += get_symetry_points(xc,yc,x,y)
    # print(points)
    return points