from Rotate import Rotate
class Shapes:
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
          count  = 0;
          _xline = []
          for j in self.points:
              i = count;
              xy = self.rotater.getRotatedPoint(ox,oy,self.points[i][0],self.points[i][1],self.angle);
              _xline.insert(i,[xy[0],xy[1]])
              count+=1
          self.line=_xline;
          return _xline;
