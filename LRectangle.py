from Shapes import Shapes
import math
class  LRectangle(Shapes):
    def __init__(self):
	self.self = self
#	self.type
#        self.origin
#        self.point_1
#	self.point_2
#	self.point_3
#	self.angle   = math.radians(90)
        self.generate()
	Shapes.__init__(self,self.origin,self.points.self.angle)
    def generate(self):
        print str(self.type)
       
class LRectangleR(LRectangle):
    def __init__(self):
        self.type    = 0
  	self.origin  = []#= [4,4]
        self.point_1 = []#= [3,4]
        self.point_2 = []#= [5,4]
        self.point_3 = []#= [5,5]
        self.points  = []#  = [self.point_1,self.origin,self.point_2,self.point_3]
        self.angle   = 0#= math.radians(90);
        LRectangle.__init__(self)

class LRectangleL(LRectangle):
    def __init__(self):
        self.type    = 1
#	 self.origin  = [4,4]
#        self.point_1 = [3,4]
#        self.point_2 = [5,4]
#        self.point_3 = [3,5]
#        self.points    = [self.point_1,self.origin,self.point_2,self.point_3]
#        self.angle   = math.radians(90);
        LRectangle.__init__(self,self.type)
