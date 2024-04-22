import numpy as np
import math

def velocidad(Díametro, Longitud, Rugosidad, Viscosidad, respuestaHF):
    a = ((respuestaHF*2*9.81*Díametro)/Longitud)**0.5
    b = (-2 * a)
    c = (Rugosidad/Díametro)
    d = (2.51*Viscosidad)
    e = (Díametro*a)
    f = ((c/3.7)+(d/e))
    g = round(b * (math.log(f,10)),3)
    return g
