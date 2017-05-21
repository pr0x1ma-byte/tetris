from Shapes import Shapes
from Line import Line
from random import randint
import math
class Triangle(Shapes):
      def __init__(self):
  	  self.autoDownShift = False	
          self.origin        = []
          self.point_1       = []
          self.point_2       = []
          self.point_3       = []
          self.direction     = randint(0,1)
          self.angle         = math.radians(90)
	  self.generate()
          self.points        = [self.origin, self.point_1, self.point_2, self.point_3]
          Shapes.__init__(self,self.origin,self.points,self.angle,self.autoDownShift)

      def generate(self):
	  line = Line()
          self.origin  = line.origin
          self.point_1 = line.point_1
	  self.point_2 = line.point_2
          _v = 1
	  if line.direction > 0:
             #vertical alignment
             if self.direction > 0:
                #Right side
                _v = _v * -1
             self.point_3 = [self.origin[0]+_v,self.origin[1]]
          else:
            if self.direction > 0:
                #Bottom side
                _v = _v * -1
            self.point_3 = [self.origin[0],self.origin[1]+_v]          


