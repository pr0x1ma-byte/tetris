from Shapes import Shapes
from random import randint
import math
class Line(Shapes):
      def __init__(self):
	  self.autoDownShift = False
          self.origin        =[]
          self.point_1 	     =[]
          self.point_2 	     =[]
	  self.direction     = randint(0,1)
          self.generate();

	  self.points        = [self.point_1,self.origin,self.point_2]
          self.angle         = math.radians(90);
          Shapes.__init__(self,self.origin,self.points,self.angle,self.autoDownShift)
      
      def generate(self):
          if self.direction > 0:
             #vertical alignment
	     self.origin  = [randint(2,30),32]
             self.point_1 = [self.origin[0],self.origin[1]-1]
 	     self.point_2 = [self.origin[0],self.origin[1]+1]         
          if self.direction < 1:
             #horizontal alignment
             self.origin  = [randint(2,30),32]
             self.point_1 = [self.origin[0]-1,self.origin[1]]
	     self.point_2 = [self.origin[0]+1,self.origin[1]]
