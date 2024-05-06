import numpy as np
import math

def FO(PérdidaCarga, respuestaHF, Ʃk, respuestaV):
    a = round(PérdidaCarga - respuestaHF - Ʃk / (2 *  9.81) * respuestaV**2 ,3)
    return a