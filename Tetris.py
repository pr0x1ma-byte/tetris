
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
unicorn.brightness(.5)
k=-1
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
width,height=unicorn.get_shape()
print '---height and width---'
print str(width) +" "+str(height)
obj = LRectangleR()
unicorn.set_pixel(0,0,255,0,255);
unicorn.show()
time.sleep(2)
while True:
      _shape  = obj.getShape()
      print _shape
      unicorn.clear()
      obj.draw()
      unicorn.show()
      time.sleep(1)
      #unicorn.clear()
      obj.rotate();
      obj.shift();

#from math import radians,cos,sin


'''
from Line import Line
from LRectangle import LRectangleR
from LRectangle import LRectangleL
from Triangle import Triangle
from ZShape import ZShape
obj = ZShapeR()
while True:
      old = obj.getLine()
      count=0
      for i in old:
          unicorn.set_pixel(old[count][0],old[count][1],255,0,255);
          count+=1
      unicorn.show()
      time.sleep(1)
      unicorn.clear()
      obj.rotate();


from Line import Line
from Triangle import Triangle
from LRectangle import LRectangleR
from LRectangle import LRectangleL
from ZShape import ZShapeR
from ZShape import ZShapeL
print "ZShapeR"
print "------Original--------------------------"
obj = ZShapeR();
old = obj.getShape();
print old
print "------Shifted---------------------------"
obj.shift()
xy = obj.getShape()
print xy
print "ZShapeL"
print "------Original--------------------------"
obj = ZShapeL();
old = obj.getShape();
print old
print "------Rotated---------------------------"
xy = obj.rotate()
print xy

print "------Original Now Rotated--------------"
old = obj.getLine();
print old

print "------Original Now Rotated Again--------"
xy = obj.rotate()
print xy
count = 0
for j in xy:
    print str(int(xy[count][0])) +" "+ str(int(xy[count][1]))
    count+=1'''
