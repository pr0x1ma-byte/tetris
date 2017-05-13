from Rotate import Rotate
class Shapes(object):
      def __init__(self, origin, points, angle):
          self.origin  = origin
          self.points  = points
          self.angle   = angle
          self.rotater = Rotate()

      def getShape(self):
          return self.points

      def rotate(self):
          ox     = self.origin[0]
          oy     = self.origin[1]
          i      = 0;
          _shape = []
          for j in self.points:
              xy = self.rotater.getRotatedPoint(ox,oy,self.points[i][0],self.points[i][1],self.angle);
              _shape.insert(i,[xy[0],xy[1]])
              i+=1
          self.points =_shape;
          return _shape;

      def shift(self):
          i     = 0
          _orig = [self.origin[0],self.origin[1]-1] #shift origin down
          print self.points
          self.points.remove(self.origin)
          print self.points
          _temp = []
          for j in self.points:
              _temp.insert(i,[self.points[i][0],self.points[i][1]-1])
              i+=1
          _temp.insert(i,[_orig[0],_orig[1]])
          self.points = _temp


              
