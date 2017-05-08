from Shapes import Shapes
import math
class Square(Shapes):
    def __init__(self):
        self.origin  = [4,4]
        self.point_1 = [3,4]
        self.point_2 = [3,5]
        self.point_3 = [4,5]
        self.angle   = math.radians(90)
        self.points  = [self.origin, self.point_1, self.point_2, self.point_3]
        Shapes.__init__(self,self.origin, self.points,self.angle)
    def rotate(self):
        return self.points




