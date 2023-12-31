import numpy as np
import arcade
import math
import random

def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )

class Polygon2D:
    def __init__(self, vertices, color, rot_speed=0):
        self.vertices = vertices
        self.color = color
        self.rot_speed = rot_speed

    def translate(self, dx, dy):
        TM = np.array([
            [1, 0, dx], 
            [0, 1, dy], 
            [0, 0, 1]
        ])

        return self.apply_transform(TM)
    
    def rotate(self, theta, pivot=None):
        xc, yc = pivot if pivot is not None else self.get_center()

        Mt1 = np.array([
            [1, 0, -xc], 
            [0, 1, -yc], 
            [0, 0, 1]
        ])
        Mr = np.array([
            [np.cos(theta), -np.sin(theta), 0], 
            [np.sin(theta), np.cos(theta), 0], 
            [0, 0, 1]
        ])
        Mt2 = np.array([
            [1, 0, xc], 
            [0, 1, yc], 
            [0, 0, 1]
        ])

        TM = np.dot(Mt2, np.dot(Mr, Mt1))
  
        return self.apply_transform(TM)

    def scale(self, sx, sy, pivot=None):
        xc, yc = pivot if pivot is not None else self.get_center()
        Mt1 = np.array([
            [1, 0, -xc], 
            [0, 1, -yc], 
            [0, 0, 1]
        ])
        Ms = np.array([
            [sx, 0, 0], 
            [0, sy, 0], 
            [0, 0, 1]
        ])
        Mt2 = np.array([
            [1, 0, xc], 
            [0, 1, yc], 
            [0, 0, 1]
        ])

        TM = np.dot(Mt2, np.dot(Ms, Mt1))
  
        return self.apply_transform(TM)

    def apply_transform(self, tr_matrix):
        v_array = np.transpose(np.array(
            [[v[0], v[1], 1] for v in self.vertices]
        ))

        self.vertices = np.transpose(
            np.dot(tr_matrix, v_array)[0:2, :]
        ).tolist()

    def get_center(self):
        return np.mean(np.array(self.vertices), axis=0)

    def draw(self):
        arcade.draw_polygon_outline(self.vertices, self.color, 5)


class Tank:
    def __init__(self, x, y, SCREEN_WIDTH, SCREEN_HEIGHT,color) -> None:
        self.color = color
        self.x = x
        self.y = y
        self.original_x = x
        self.original_y = y
        self.speed = 0
        self.angular_speed = 0
        self.theta = 0
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.lifes = 5
        self.big_bullet = []
        
        self.body_distance = 30
        self.body = Polygon2D([
            (-self.body_distance + x, self.body_distance + y),
            (self.body_distance + x, self.body_distance + y),
            (self.body_distance + x, -self.body_distance + y),
            (-self.body_distance + x, -self.body_distance + y),
            (-self.body_distance + x, self.body_distance + y)
        ] + [
            (-self.body_distance + x + i, self.body_distance + y - j)
            for i in range(0,60,59) for j in range(0,60,1)
        ], color)
        self.cannon = Polygon2D([
            (30+x,10+y),
            (90+x,10+y),
            (90+x,-10+y),
            (30+x,-10+y),
            (90+x,-10+y),
        ] + [
            (30+ x + i,10 + y - j)
            for i in range(0,60,6) for j in range(0,20,1)
        ] + [
            (90+x,-10+y),
            (90+x,-20+y),
            (110+x,-20+y),
            (110+x,20+y),
            (90+x,20+y),
            (90+x,10+y)
        ] + [
            (90+x+i,20+y-j)
            for i in range(0,20,2) for j in range(0,40,1)
        ],color)
        
        self.shield = Polygon2D(
            self.get_circle(x, y, 35),
            get_random_color()
        )
        
        self.left_track = Polygon2D(
            [
                (-40 + x, -30 + y), 
                (60 + x, -30 + y),
                (60 + x, -60 + y),
                (-40 + x, -60 + y), 
            ],
            color
        )
        self.right_track = Polygon2D(
            [
                (-40 + x, 30 + y), 
                (60 + x, 30 + y),
                (60 + x, 60 + y),
                (-40 + x, 60 + y), 
            ],
            color
        )
        self.wheel_radious = 10
        
        self.wheels_positions = [
            (-30+x,60+y),
            (-10+x,60+y),
            (10+x,60+y),
            (30+x,60+y),
            (50+x,60+y),
            (-30+x,-60+y),
            (-10+x,-60+y),
            (10+x,-60+y),
            (30+x,-60+y),
            (50+x,-60+y),
        ]
        self.wheels = [
            Polygon2D(
                self.get_circle(i[0],i[1],self.wheel_radious),
                color
            ) for i in self.wheels_positions
        ]
        self.bullets = []
        
    def get_symetry_points(self,x0,y0,x1,y1):
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
        
    def detect_attack(self, tank):
        index = 0
        for bullet in tank.bullets:
            if self.distance_to(bullet) <= self.body_distance + 1:
                tank.bullets[index:index+1]=[]
                self.lifes -= 1
                break
            index += 1

        index = 0
        for bigger in tank.big_bullet:
            if self.distance_to(bigger) <= self.body_distance + 1:
                tank.big_bullet[index:index+1]=[]
                self.lifes -= 3
                tank.big_bullet.append((0, 0, 0, 0))
                tank.big_bullet.append((0, 0, 0, 0))
                break
            index += 1

    def distance_to(self, bullet):
        xb, yb, tb, sb = bullet
        return math.sqrt((xb - self.x)**2 + (yb - self.y)**2)

    def get_circle(self,xc, yc, r):
        x = 0
        y = r
        Pk = 3 - 2 * r
        points = []
        points += self.get_symetry_points(xc,yc,x,y)
        while x <= y:
            x += 1
            if Pk < 0:
                Pk += (4 * x) + 6
            else:
                Pk += 4 * (x - y) + 10
                y -= 1
            points += self.get_symetry_points(xc,yc,x,y)
        return points
    
    def shoot(self, type_shoot):
        if type_shoot == "normal":
            self.bullets.append((self.x, self.y, self.theta, 20))
        if type_shoot == "bigger" and len(self.big_bullet) == 0:
            self.big_bullet.append((self.x, self.y, self.theta, 20))

    def update(self, delta_time: float):
        dtheta = self.angular_speed * delta_time
        dx = self.speed * math.cos(self.theta)
        dy = self.speed * math.sin(self.theta)
        self.theta += dtheta
        self.x += dx
        self.y += dy
        
        if (self.x > 0 and self.x < self.SCREEN_WIDTH) and (self.y > 0 and self.y < self.SCREEN_HEIGHT-100):
            self.body.translate(dx, dy)
            self.left_track.translate(dx, dy)
            self.right_track.translate(dx, dy)
            self.cannon.translate(dx,dy)
            self.shield.translate(dx,dy)
            for i in self.wheels:
                i.translate(dx,dy)
            self.original_x = self.x
            self.original_y = self.y
        else:
            self.x = self.original_x
            self.y = self.original_y
        
        self.body.rotate(dtheta, pivot=(self.x, self.y))
        self.left_track.rotate(dtheta, pivot=(self.x, self.y))
        self.right_track.rotate(dtheta, pivot=(self.x, self.y))
        self.cannon.rotate(dtheta, pivot=(self.x, self.y))
        for i in self.wheels:
            i.rotate(dtheta, pivot=(self.x, self.y))

        self.update_bullets(delta_time)

    def update_bullets(self, delta_time):
        for i, (x, y, theta, speed) in enumerate(self.bullets):
            new_x = x + speed * math.cos(theta)
            new_y = y + speed * math.sin(theta)
            self.bullets[i] = (new_x, new_y, theta, speed)
        
        for _, (x, y, theta, speed) in enumerate(self.big_bullet):
            new_x = x + speed * math.cos(theta)
            new_y = y + speed * math.sin(theta)
            self.big_bullet[0] = (new_x, new_y, theta, speed)

    def draw(self):
        if self.lifes>0:
            self.body.draw()
            self.left_track.draw()
            self.right_track.draw()
            for i in self.wheels:
                i.draw()
            self.cannon.draw()
            self.shield.draw()
            
            if (self.x > 0 and self.x < self.SCREEN_WIDTH) and (self.y > 0 and self.y < self.SCREEN_HEIGHT-100):
                arcade.draw_point(self.x, self.y, arcade.color.RED, 4)
        for bx, by, theta, speed in self.bullets:
            if (bx > 0 and by < self.SCREEN_WIDTH) and (by > 0 and by < self.SCREEN_HEIGHT-100):
                arcade.draw_point(bx, by, self.color, 7)
        for bx, by, theta, speed in self.big_bullet:
            if (bx > 0 and by < self.SCREEN_WIDTH) and (by > 0 and by < self.SCREEN_HEIGHT-100):
                arcade.draw_point(bx, by, self.color, 12)


class HidePlace:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    
    def detect_collision(self, tank: Tank):
        index = 0
        for bullet in tank.bullets:
            if self.distance_to(bullet) <= self.r:
                tank.bullets[index:index+1]=[]
                break
            index += 1

        index = 0
        for bigger in tank.big_bullet:
            if self.distance_to(bigger) <= self.r:
                tank.big_bullet[index:index+1]=[]
                self.lifes -= 3
                tank.big_bullet.append((0, 0, 0, 0))
                tank.big_bullet.append((0, 0, 0, 0))
                break
            index += 1
    
    def distance_to(self, bullet):
        xb, yb, tb, sb = bullet
        return math.sqrt((xb - self.x)**2 + (yb - self.y)**2)

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, arcade.color.RED_DEVIL)