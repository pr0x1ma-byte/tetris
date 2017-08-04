#from Line import Line
#from LRectangle import LRectangleR
#from LRectangle import LRectangleL
#from Square import Square
#from Triangle import Triangle
#from ZShape import ZShapeR
#from ZShape import ZShapeL

from Rotate import Rotate
from random import randint
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions
height = 32
width = 32
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.brightness = 100
#options.show_refresh_rate = 1
options.gpio_slowdown = 2
options.pwm_lsb_nanoseconds = 325
options.pwm_bits = 11
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
#options.rotation = 90
matrix = RGBMatrix(options = options)
canvas = matrix.CreateFrameCanvas()
canvas = matrix.SwapOnVSync(canvas);
#print canvas
class Shapes(object):
      def __init__(self, origin, points, angle, auto):
	  self.autoDownShift = auto
          self.origin  = origin
          self.points  = points
          self.angle   = angle
          self.rotater = Rotate()
	  self.board   = []
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
	  _failed = False
          for j in self.points:
              xy = self.rotater.getRotatedPoint(ox,oy,self.points[i][0],self.points[i][1],self.angle);
              _v = self.board.checkPointsCollision(xy[0],xy[1])
	      if xy[0] > width - 1 or xy[0] < 0 or xy[1] < 0:
	         _failed = True
	      if _v['other']:
	         _failed = True 
	      _shape.insert(i,[xy[0],xy[1]])
              i+=1
	  if not _failed:
             self.points =_shape;
          self.drawShiftRotate()
#          return _shape;

      def shiftDecisionDown(self, _data, shapeWrapper):
    	  _points = _data[0]
          _origin = _data[1]
          _failed = _data[2]
	  if _failed[2]:
	     shapeWrapper.observer.end()
          elif not _failed[0] and not _failed[1]:
             self.origin = _origin
             self.points = _points
             shapeWrapper.shiftIndex+=1
	     if shapeWrapper.shiftIndex > height - 1:
                self.board.freeze(self,canvas,matrix)
             self.drawShiftRotate()
	  else:
             self.board.freeze(self,canvas,matrix)
             shapeWrapper.shiftIndex=33 #? trigger new object on next pass

      def shiftDecision(self, _data, shapeWrapper): 
          _points = _data[0]
          _origin = _data[1]
          _failed = _data[2]
          if not _failed:
             self.origin = _origin
             self.points = _points
          self.drawShiftRotate()

      def shiftDown(self, shapeWrapper):
	  self.shiftDecisionDown(self.detectDownCollision(),shapeWrapper)

      def detectDownCollision(self):
	  i       = 0
	  _points = self.points
          _orig   = [self.origin[0],self.origin[1]-1] 
          _temp   = []
         # _failed = False
          _failed = [False,False,False]#{bottom:False,other:False}
	  _top    = False
          _other  = False
          for j in _points: #contains origin
	      _x = _points[i][0]
              _y = _points[i][1] -1
	      _v = self.board.checkPointsCollision(_x,_y)
              if _v['bottom']:
	         _failed[0] = True
              if _v['other']:
	         _failed[1] = True
	         _other = True
	      if  _v['top']:
	         _top = True
              _temp.insert(i,[_x,_y])
              i+=1
          if _other and _top:
	     _failed[2] = True 
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
	      _v = self.board.checkPointsCollision(_x,_y)
              if _x > width-1:
                 _failed = True
	      if _v['other'] or _v['side']:
	         _failed = True
              _temp.insert(i,[_x,_y])
              i+=1
          return [_temp,_orig,_failed]

      def shiftLeft(self, shapeWrapper):
	  self.shiftDecision(self.detectLeftCollision(), shapeWrapper)

      def detectRightCollision(self):
          i       = 0
          _points = self.points
          _orig   = [self.origin[0]-1,self.origin[1]]
          _temp   = []
          _failed = False
          for j in _points: #contains origin
              _x = _points[i][0] - 1
              _y = _points[i][1]
	      _v = self.board.checkPointsCollision(_x,_y)
              if _x < 0:
                 _failed = True
	      if _v['other'] or _v['side']:
	         _failed = True
              _temp.insert(i,[_x,_y])
              i+=1
          return [_temp,_orig,_failed]

      def shiftRight(self, shapeWrapper):
          self.shiftDecision(self.detectRightCollision(), shapeWrapper)

      def drawShiftRotate(self):
	  global canvas
          matrix.Clear();
          i  = 0
          for j in self.points:
              _x = self.points[i][0]
              _y = self.points[i][1]
              if _x <= height-1 and _y <=height-1 and _x >= 0 and _y >= 0:
                 canvas.SetPixel(_x,_y,self.color[0],self.color[1],self.color[2]);
              i+=1
          self.board.draw(canvas)	
 	  canvas = matrix.SwapOnVSync(canvas);

      def draw(self):
	  global canvas
	  matrix.Clear()
	  i  = 0
          for j in self.points:
              _x = self.points[i][0]
              _y = self.points[i][1]
	      if _x <= height-1 and _y <=height-1 and _x >= 0 and _y >= 0:  
	         canvas.SetPixel(_x,_y,self.color[0],self.color[1],self.color[2]);
              i+=1
	  canvas = matrix.SwapOnVSync(canvas);
              
      def setBoard(self,board):
          self.board = board
