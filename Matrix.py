from math import sin, cos, radians
'''
#adjacent over hypotenuse is cos(theta)
#opposite over hypotenuse is sin(theta)
#xp = xcos(theta) - ysin(theta)
#yp = xsin(theta) + ycos(theta)

#x=1
#y=0

#xp = _x*cosang - _y*sinang
#yp = _x*sinang + _y*cosang
'''

class Matrix():
    def __init__(self):
        self.dummy=0

    def identity(self):
        return [ [1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 1] ]

    def multiply(self, p, m): #
        return [
            [  (p[0][0] * m[0][0])
             + (p[0][1] * m[1][0])
             + (p[0][2] * m[2][0]),

               (p[0][0] * m[0][1])
             + (p[0][1] * m[1][1])
             + (p[0][2] * m[2][1]),

               (p[0][0] * m[0][2])
             + (p[0][1] * m[1][2])
             + (p[0][2] * m[2][2])],
            # ---
            [  (p[1][0] * m[0][0])
             + (p[1][1] * m[1][0])
             + (p[1][2] * m[2][0]),

               (p[1][0] * m[0][1])
             + (p[1][1] * m[1][1])
             + (p[1][2] * m[2][1]),

               (p[1][0] * m[0][2])
             + (p[1][1] * m[1][2])
             + (p[1][2] * m[2][2])],
            # ---
            [  (p[2][0] * m[0][0])
             + (p[2][1] * m[1][0])
             + (p[2][2] * m[2][0]),

               (p[2][0] * m[0][1])
             + (p[2][1] * m[1][1])
             + (p[2][2] * m[2][1]),

               (p[2][0] * m[0][2])
             + (p[2][1] * m[1][2])
             + (p[2][2] * m[2][2])]]

    def translate(self,_x,_y):
        return [ [1 ,0 ,0],
                 [0 ,1 ,0],
                 [_x,_y,1] ]

    def rotate(self,rad):
        return [ [float(cos(rad)) , float(sin(rad)), float(0)],
               [  float(-sin(rad)), float(cos(rad)), float(0)],
               [  float(0)        , float(0 )      , float(1)] ]

    def toVectorAddOrigin(self, vec, p, _ox, _oy):
                return [int(round( vec.x *p[0][0]
                                   +vec.y *p[1][0]
                                   +vec.w *p[2][0]))+_ox,
                        int(round( vec.x *p[0][1]
                                   +vec.y *p[1][1]
                                   +vec.w *p[2][1]))+_oy,
                        int(round( vec.x *p[0][2]
                                   +vec.y *p[1][2]
                                   +vec.w *p[2][2]))]
    def toVector(self, vec, p):
        return [int(round( vec.x *p[0][0]
                           +vec.y *p[1][0]
                           +vec.w *p[2][0])),
                int(round( vec.x *p[0][1]
                           +vec.y *p[1][1]
                           +vec.w *p[2][1])),
                int(round( vec.x *p[0][2]
                           +vec.y *p[1][2]
                           +vec.w *p[2][2]))]

