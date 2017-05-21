#from Line import Line
#from LRectangle import LRectangleR
#from LRectangle import LRectangleL
#from Square import Square
#from Triangle import Triangle
#from ZShape import ZShapeR
#from ZShape import ZShapeL

from Rotate import Rotate
import unicornhat as unicorn
from random import randint
import time

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
width,height=unicorn.get_shape()
unicorn.brightness(.6)

class Shapes(object):
      def __init__(self, origin, points, angle, auto):
	  self.autoDownShift = auto
          self.origin  = origin
          self.points  = points
          self.angle   = angle
          self.rotater = Rotate()
          self.color   = self.genColor()

      def genColor(self):
          red   = randint(0,255)
          blue  = randint(0,255)
          green = randint(0,255)
          color = [red,blue,green]
          return color
      
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
          self.drawShiftRotate()
#          return _shape;

      def shiftDecisionDown(self, _data, shapeWrapper, board):
    	  _points = _data[0]
          _origin = _data[1]
          _failed = _data[2]
          if not _failed:
             self.origin = _origin
             self.points = _points
             shapeWrapper.shiftIndex+=1
          else:
             board.freeze(self)
             board.draw()
             shapeWrapper.shiftIndex=9 #? trigger new object on next pass
          self.drawShiftRotate()

      def shiftDecision(self, _data, shapeWrapper, board): 
          _points = _data[0]
          _origin = _data[1]
          _failed = _data[2]
          if not _failed:
             self.origin = _origin
             self.points = _points
          else:
             board.draw()
          self.drawShiftRotate()

      def shiftDown(self, shapeWrapper, board):
	  self.shiftDecisionDown(self.detectDownCollision(),shapeWrapper, board)

      def detectDownCollision(self):
	  i       = 0
	  _points = self.points
          _orig   = [self.origin[0],self.origin[1]-1] 
          _temp   = []
          _failed = False
	  for j in _points: #contains origin
	      _x = _points[i][0]
              _y = _points[i][1] -1
              if _y < 0:
	         _failed = True 
              _temp.insert(i,[_x,_y])
              i+=1
          self.autoDownShift = True  #enable down shift increment check
	  return [_temp,_orig,_failed]
      def detectLeftCollision(self):
	  i       = 0
          _points = self.points
          _orig   = [self.origin[0]+1,self.origin[1]]
          _temp   = []
          _failed = False
          for j in _points: #contains origin
              _x = _points[i][0] + 1
              _y = _points[i][1]
              if _x > width-1:
                 _failed = True
              _temp.insert(i,[_x,_y])
              i+=1
          return [_temp,_orig,_failed]

      def shiftLeft(self, shapeWrapper, board):
	  self.shiftDecision(self.detectLeftCollision(), shapeWrapper, board)

      def detectRightCollision(self):
          i       = 0
          _points = self.points
          _orig   = [self.origin[0]-1,self.origin[1]]
          _temp   = []
          _failed = False
          for j in _points: #contains origin
              _x = _points[i][0] - 1
              _y = _points[i][1]
              if _x < 0:
                 _failed = True
              _temp.insert(i,[_x,_y])
              i+=1
          return [_temp,_orig,_failed]

      def shiftRight(self, shapeWrapper, board):
          self.shiftDecision(self.detectRightCollision(), shapeWrapper, board)

      def drawShiftRotate(self):
	  unicorn.clear()
          i  = 0
          for j in self.points:
              _x = self.points[i][0]
              _y = self.points[i][1]
              if _x <= height-1 and _y <=height-1 and _x >= 0 and _y >= 0:
                 unicorn.set_pixel(_x,_y,self.color[0],self.color[1],self.color[2]);
              i+=1
          unicorn.show()

      def draw(self):
          unicorn.clear()
	  i  = 0
          for j in self.points:
              _x = self.points[i][0]
              _y = self.points[i][1]
	      if _x <= height-1 and _y <=height-1 and _x >= 0 and _y >= 0:
                 unicorn.set_pixel(_x,_y,self.color[0],self.color[1],self.color[2]);
              i+=1
	  unicorn.show()
              

