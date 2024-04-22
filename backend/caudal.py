import numpy as np
import math

def caudal(Díametro, respuestaV):
    a = (respuestaV)
    b = (math.pi * (Díametro ** 2) * 0.25)
    c = round(a * b,3)
    return c


