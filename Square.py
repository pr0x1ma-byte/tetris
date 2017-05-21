from Shapes import Shapes
from Line import Line
import math
class Square(Shapes):
    def __init__(self):
	self.autoDownShift = False
        self.origin        = []
        self.point_1       = []
        self.point_2       = []
        self.point_3       = []
        self.angle         = math.radians(90)
        self.generate()
        self.points        = [self.origin, self.point_1, self.point_2, self.point_3]
        Shapes.__init__(self,self.origin,self.points,self.angle,self.autoDownShift)

    def rotate(self):
        super(Square, self).drawShiftRotate()
        return self.points

    def generate(self):
        line         = Line()
        self.origin  = line.origin
        self.point_1 = line.point_2
        if line.direction > 0:
           #vertical alignment
           self.point_2 = [self.origin[0]+1 ,self.origin[1]]
           self.point_3 = [self.point_1[0]+1,self.point_1[1]]
        else:
           self.point_2 = [self.origin[0] ,self.origin[1]+1]
           self.point_3 = [self.point_1[0],self.point_1[1]+1]




