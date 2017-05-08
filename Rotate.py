from Matrix import Matrix
from Vector import Vector

class Rotate():
    def __init__(self):
        self.Matrix3f = Matrix()
        self.Vector2f = Vector()

    def getRotatedPoint(self, _ox,_oy, _x, _y, _angle):
        _x1             = _x - _ox;
        _y1             = _y - _oy;                                                        # find difference between x/y and origin
        matrix          = self.Matrix3f.translate(_x1, _y1);                               # put points into 3x3 matrix
        angle           = self.Matrix3f.rotate(_angle);                                    # generate angle matrix
        prime           = self.Matrix3f.multiply(matrix, angle)                        # rotate point matrix to get xy prime-> multiply  angle matrix and point matrix
        xy              = self.Matrix3f.toVectorAddOrigin(self.Vector2f, prime, _ox, _oy)  # add rotated point coordintes to origin
        return xy;
