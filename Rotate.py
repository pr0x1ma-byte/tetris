from Matrix import Matrix
from Vector import Vector

class Rotate():
    def __init__(self):
        self.Matrix = Matrix()
        self.Vector = Vector()

    def getRotatedPoint(self, _ox,_oy, _x, _y, _angle):
        _x1             = _x - _ox;
        _y1             = _y - _oy;                                                      # find difference between x/y and origin
        matrix          = self.Matrix.translate(_x1, _y1);                               # put points into 3x3 matrix
        angle           = self.Matrix.rotate(_angle);                                    # generate angle matrix
        prime           = self.Matrix.multiply(matrix, angle)                            # rotate point matrix to get xy prime-> multiply  angle matrix and point matrix
        xy              = self.Matrix.toVectorAddOrigin(self.Vector, prime, _ox, _oy)    # add rotated point coordintes to origin
        return xy;
