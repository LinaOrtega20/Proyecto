import numpy as np



def coeficientef(respuestaHF, Díametro, Longitud, respuestaV):
    a = round(respuestaHF*2*9.81*Díametro/(Longitud*respuestaV**2),3)
    return a

