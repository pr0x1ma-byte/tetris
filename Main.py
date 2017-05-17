
from random import randint
import unicornhat as unicorn
import time
import os
import sys
import tty
import threading
import math
from pyfiglet import figlet_format
from Line import Line
from LRectangle import LRectangleR
from LRectangle import LRectangleL
from Square import Square
from Triangle import Triangle
from ZShape import ZShapeR
from ZShape import ZShapeL
unicorn.brightness(.5)
k=-1
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
width,height=unicorn.get_shape()
obj = Triangle()

class Generator():
  def __init__(self):
      self.shiftIndex = 0
      self.shape = []
      self.getNewObject()
      self.exit = False
  def getNewObject(self):
      val = randint(0,6);
      o   = [Line(),LRectangleL(),LRectangleR(),Triangle(),Square(),ZShapeL(),ZShapeR()]
      self.shape = o[val]

  def shift(self):
      if not self.exit:
         if self.shiftIndex > 7:
            self.shiftIndex = 0
            self.getNewObject()
         self.shape.shiftDown()
         self.shiftIndex+=1
         threading.Timer(1, self.shift).start()
  def start(self):
      self.shift()
      while not self.exit:            
#            self.shape.rotate();
            self.shape.draw()
            time.sleep(.2)

#while True:
#    _shape  = obj.getShape()
#    print _shape
#    if i > 8:
#       i=0
#       obj = getNewObject()
#    unicorn.clear()
#    obj.draw()
#    unicorn.show()
#    time.sleep(.5)
    #unicorn.clear()
#    obj.rotate();
