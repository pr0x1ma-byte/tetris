
from ShapesWrapper import ShapesWrapper
from User import User
import os
import sys
import Queue
import threading

class Game(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.key = Queue.Queue()
        self.shapes_wrapper = ShapesWrapper(self.key)
        self.user = User(self.key)
        pass
    def load(self):
        self.shapes_wrapper.start()
        self.user.start()
    
    def run(self):
        self.load()



try:
   game = Game()
   game.start()
except KeyboardInterrupt:
   pass

