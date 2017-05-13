from Shapes import Shapes
from Line import Line
import math
#change
class ZShape(Shapes):
    def __init__(self):
        self.origin    = []
        self.point_1   = []
        self.point_2   = []
        self.point_3   = []
        self.angle     = math.radians(90)
        self.generate()
        self.points    = [self.point_1,self.origin,self.point_2,self.point_3]
        Shapes.__init__(self,self.origin,self.points,self.angle)
    def rotate(self):
        _points = super(ZShape,self).rotate();
        self.angle = self.angle * -1;
        return _points

    def generate(self):
        line = Line();
        self.origin  = line.origin
        self.point_1 = line.point_2
        if line.direction > 0:
           #vertical alignment
           if self.type > 0:
              #R
              self.point_2 = [self.origin[0]-1, self.origin[1]]
	      self.point_3 = [self.point_2[0] , self.point_2[1]-1]
           else:
              #L
              self.point_2 = [self.origin[0]+1, self.origin[1]]
	      self.point_3 = [self.point_2[0] , self.origin[1]-1]
        else:
              #horizontal alignment
           if self.type > 0:
              #R
              self.point_2 = [self.origin[0]   , self.origin[1]+1]
              self.point_3 = [self.point_2[0]-1, self.point_2[1]] 
           else:
              #L
              self.point_2 = [self.origin[0]   , self.origin[1]-1]
              self.point_3 = [self.point_2[0]-1, self.point_2[1]]
 
   
class ZShapeR(ZShape):
    def __init__(self):
        self.type = 0
#        self.origin  = [4,4]
#        self.point_1 = [3,4]
#        self.point_2 = [4,5]
#        self.point_3 = [5,5]
#        self.points    = [self.point_1,self.origin,self.point_2,self.point_3]
#        self.angle   = math.radians(90);
        ZShape.__init__(self)


class ZShapeL(ZShape):
    def __init__(self):
        self.type = 1
#        self.origin  = [4,4]
#        self.point_1 = [3,4]
#        self.point_2 = [4,3]
#        self.point_3 = [5,3]
#        self.points    = [self.point_1,self.origin,self.point_2,self.point_3]
#        self.angle   = math.radians(90);
        ZShape.__init__(self)
