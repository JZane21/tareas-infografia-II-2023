import arcade
import numpy as np

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Matrices de transformacion"


class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        
    def on_draw(self):
        arcade.start_render()
        vertices = [(100, 100), (100, 200), (200, 200), (200, 100)]
        arcade.draw_polygon_outline(vertices, arcade.color.YELLOW, 5)
        new_vertices = self.translate2(vertices, 200, 200)
        arcade.draw_polygon_outline(new_vertices, arcade.color.CYBER_YELLOW, 5)

    def translate(self, vertices, dx, dy):
        new_vertices = [(v[0] + dx, v[1] + dy) for v in vertices]
        return new_vertices
    
    def rotate(self,vertices,ang):
        # x_prime = (np.cos(ang),-np.sin(ang))
        # y_prime = (np.sin(ang),np.cos(ang))
        # matrix = np.array([x_prime.index(0),x_prime.index(1),0],
        #                   [y_prime.index(0),y_prime.index(0),0],
        #                   [0,0,1])
        
        xc , yc = self.get_center(vertices)
        
        Mt1 = np.array([
            [1,0,-xc],
            [0,1,-yc],
            [0,0,1]
        ])
        
        Mr = np.array([
            [np.cos(ang), -np.sin(ang),0],
            [np.sin(ang),np.cos(ang),0],
            [0,0,1],
        ])
        
        Mt2 = np.array([
            [1,0,xc],
            [0,1,yc],
            [0,0,1]
        ])
        
        matrix = np.dot(Mt2, np.dot(Mr, Mt1))
        
        return self.apply_tr_matrix(vertices,matrix)
    
    def apply_tr_matrix(vertices,tr_matrix):
        v_array = np.array([[v[0], v[1], 1] for v in vertices])
        v_array = np.transpose(v_array)
        # aplicar transformacion
        new_vertices_array = np.dot(tr_matrix, v_array)
        new_vertices = np.transpose(new_vertices_array[0:2, :])
        new_vertices = new_vertices.tolist()
        return new_vertices
    
    def scale(self,vertices,sx,sy):
        TM = np.array([sx,  0,   0],
                      [0,  sy,   0],
                      [0,  0,   1])
        
        return self.apply_tr_matrix(vertices,TM)
    
    def get_center(self,vertices):
        return np.mean(np.array([
            
        ]))
    
    def translate2(self, vertices, dx, dy):
        TM = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
        return self.apply_tr_matrix(vertices,TM)



if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()