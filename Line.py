from Shapes import Shapes
import math
class Line(Shapes):
      def __init__(self):
          self.origin  = [4,4]
          self.point_1 = [3,4]
          self.point_2 = [5,4]
          self.points    = [self.point_1,self.origin,self.point_2]
          self.angle   = math.radians(90);
          Shapes.__init__(self,self.origin,self.points,self.angle)


