import pygame.draw as pgd
import math as m


class Vector:
    def __init__(self, coords):
        self.coords = list(coords)
        self.x = coords[0]
        self.y = coords[1]
        if self.coords == [0, 0]:
            self.length = 1
        else:
            self.length = (self.x**2+self.y**2)**(0.5)
        if self.y >= 0:
            self.angle = m.acos(self.x/self.length)
        else:
            self.angle = 2*m.pi - m.acos(self.x/self.length)
        
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector((new_x, new_y))
    
    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector((new_x, new_y))
    
    def rotate(self, angle_deg, point_vector, direction='clockwise'):
        angle_rad = (2*m.pi)*((angle_deg%360)/360)
        in_point_sys = self - point_vector
        length = in_point_sys.length
        if direction == 'clockwise':
            angle = in_point_sys.angle + angle_rad
        elif direction == 'counterclockwise':
            angle = in_point_sys.angle - angle_rad
        else:
            angle = in_point_sys.angle + angle_rad
        new_x = length * m.cos(angle)
        new_y = length * m.sin(angle)
        return Vector((new_x, new_y)) + point_vector
    
    
class Polygon:
    def __init__(self, screen, color, vertexes, width=0):
        self.screen = screen
        self.color = color
        self.vertexes = vertexes
        self.width = width
    
    def draw(self): #FIXME add gradient
        pgd.polygon(self.screen, self.color, self.vertexes, self.width)
        
    def rotate(self, angle_deg, point, direction='clockwise'):
        new_vertexes = []
        point_vector = Vector(point)
        for vertex in self.vertexes:
            vertex_vector = Vector(vertex)
            vertex_vector = vertex_vector.rotate(angle_deg, point_vector, direction)
            vertex = vertex_vector.coords
            new_vertexes.append(vertex)
        self.vertexes = new_vertexes
        
    def move(self, velocity): #FIXME to do
        new_vertexes = []
        for vertex in self.vertexes:
            new_vertex = [vertex[0]+velocity[0], vertex[1]+velocity[1]]
            new_vertexes.append(new_vertex)
        self.vertexes = new_vertexes
    
    def center(self): #FIXME to do
        pass
    
    def collide_point(self, point): #FIXME to do
        pass
    
    def triangles(self): #FIXME divide polygon into triangles
        triangles = []
        return triangles