from Shapes import Shapes
import math
class ZShapeR(Shapes):
    def __init__(self):
        self.origin  = [4,4]
        self.point_1 = [3,4]
        self.point_2 = [4,5]
        self.point_3 = [5,5]
        self.points    = [self.point_1,self.origin,self.point_2,self.point_3]
        self.angle   = math.radians(90);
        Shapes.__init__(self,self.origin,self.points,self.angle)

    def rotate(self):
        _points = super(ZShapeR,self).rotate();
        self.angle = self.angle * -1;
        return _points

class ZShapeL(Shapes):
    def __init__(self):
        self.origin  = [4,4]
        self.point_1 = [3,4]
        self.point_2 = [4,3]
        self.point_3 = [5,3]
        self.points    = [self.point_1,self.origin,self.point_2,self.point_3]
        self.angle   = math.radians(90);
        Shapes.__init__(self,self.origin,self.points,self.angle)

    def rotate(self):
        _points = super(ZShapeL,self).rotate();
        self.angle = self.angle * -1;
        return _points