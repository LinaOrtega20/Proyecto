import numpy as np
import math

def caudal(Díametro, respuestaV):
    a = (respuestaV) * (math.pi * (Díametro ** 2) * 0.25)
    return a
