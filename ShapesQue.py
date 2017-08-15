from Line import Line
from LRectangle import LRectangleR
from LRectangle import LRectangleL
from Square import Square
from Triangle import Triangle
from ZShape import ZShapeR
from ZShape import ZShapeL
from random import randint
#
class ShapesQue():
      def __init__(self):
	  self.que = []
	  self.que.insert(0,self.genShape())

      def getNext(self):          
	  shape = self.que[0]
	  del self.que[:]
	  self.que.insert(0,self.genShape())
	  return shape
	  
      def getShape(self):
	  return self.que[0]

      def genShape(self):
	  index  = randint(0,6)
          shapes = [Line(),LRectangleL(),LRectangleR(),Triangle(),Square(),ZShapeL(),ZShapeR()]
          shape  = shapes[index]	  
	  return shape	     
	  		
#      def drawQue(self):

