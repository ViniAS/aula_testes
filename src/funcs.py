import math

def lei_cossenos(lado1: int|float,lado2: int|float,angulo: int|float)-> int:    
    if angulo>=math.pi or angulo<=0:
        raise ValueError('angulo invalido')
    if lado1 <= 0 or lado2 <=0:
        raise ValueError('lados negativos')
    return math.sqrt(lado1**2+lado2**2-2*lado1*lado2*math.cos(angulo))

