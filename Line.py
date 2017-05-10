from Shapes import Shapes
from random import randint
import math
class Line(Shapes):
      def __init__(self):
          self.origin  =[]# [randint(0,8),8]
          self.point_1 =[]# [self.origin[0]+1,self.origin[1]+1]
          self.point_2 =[]# [self.origin[0]-1,self.origin[1]-1]
          self.generate();

	  self.points    = [self.point_1,self.origin,self.point_2]
          self.angle   = math.radians(90);
          Shapes.__init__(self,self.origin,self.points,self.angle)
      
      def generate(self):
          self.direction = randint(0,1)
          if self.direction > 0:
             #vertical alignment
             print 'vertical alignment'
	     self.origin  = [randint(0,8),8]
             self.point_1 = [self.origin[0],self.origin[1]+1]
 	     self.point_2 = [self.origin[1],self.origin[1]-1]         
          if self.direction < 1:
             #horizontal alignment
	     print 'horizontal alignment'
             self.origin  = [randint(1,7),8]
             self.point_1 = [self.origin[0]+1,self.origin[1]]
	     self.point_2 = [self.origin[0]-1,self.origin[1]]
