from Rotate import Rotate
import unicornhat as unicorn
from random import randint
import time

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
width,height=unicorn.get_shape()
unicorn.brightness(.5)

class Shapes(object):
      def __init__(self, origin, points, angle):
          self.origin  = origin
          self.points  = points
          self.angle   = angle
          self.rotater = Rotate()
          self.color   = self.genColor()

      def genColor(self):
          red   = randint(0,255)
          blue  = randint(0,255)
          green = randint(0,255)
          color = [red,blue,green]
          return color
      
      def getShape(self):
          return self.points

      def rotate(self):
          ox     = self.origin[0]
          oy     = self.origin[1]
          i      = 0;
          _shape = []
          for j in self.points:
              xy = self.rotater.getRotatedPoint(ox,oy,self.points[i][0],self.points[i][1],self.angle);
              _shape.insert(i,[xy[0],xy[1]])
              i+=1
          self.points =_shape;
          return _shape;

      def shift(self):
          i     = 0
          _orig = [self.origin[0],self.origin[1]-1] #shift origin down
          self.points.remove(self.origin)
          _temp = []
          for j in self.points:
              _temp.insert(i,[self.points[i][0],self.points[i][1]-1])
              i+=1
          _temp.insert(i,[_orig[0],_orig[1]])
          self.origin = _orig
          self.points = _temp

      def draw(self):
	  i  = 0
          for j in self.points:
              _x = self.points[i][0]
              _y = self.points[i][1]
	      if _x <= height-1 and _y <=height-1 and _x >= 0 and _y >= 0:
                 unicorn.set_pixel(_x,_y,self.color[0],self.color[1],self.color[2]);
              i+=1
              
