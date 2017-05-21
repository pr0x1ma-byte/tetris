from Shapes import Shapes
from Line import Line
import math
class  LRectangle(Shapes):
    def __init__(self):
	self.autoDownShift = False
        self.origin        = []
        self.point_1       = []
        self.point_2       = []
        self.point_3       = []
        self.points        = []
        self.angle         = math.radians(90);
        self.direction     = 0
        self.generate()
	Shapes.__init__(self,self.origin,self.points,self.angle,self.autoDownShift)
		
    def generate(self):
        line = Line();
        self.origin  = line.origin
	self.point_1 = line.point_1
        self.point_2 = line.point_2
        self.direction = line.direction
        _v = 1;
        if self.type > 0:
           _v = _v * -1;
        
        if self.direction > 0:
           #vertical alignment
           if self.type > 0:
              #R type
	      _v = _v * -1	
           self.point_3 = [self.point_2[0]+_v,self.point_2[1]]
        else:
	   #horizontal alignment
           if self.type > 1:
              #L type
	      _v = _v * -1
           self.point_3 = [self.point_2[0],self.point_2[1]+_v]
        self.points = [self.point_1,self.origin,self.point_2,self.point_3]

class LRectangleR(LRectangle):
    def __init__(self):
        self.type    = 0
        LRectangle.__init__(self)

class LRectangleL(LRectangle):
    def __init__(self):
        self.type    = 1
        LRectangle.__init__(self)
