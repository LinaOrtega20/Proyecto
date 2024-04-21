import numpy as np
import math

def coeficientef(respuestaHF, Díametro, Longitud, respuestaV):
    a = (respuestaHF*2*9.81*Díametro/(Longitud*respuestaV**2))
    return a

