import math
def calcularArea(raio):
    area = math.pi * raio ** 2
    return area

raio = 5
areaDoCirculo = calcularArea(raio)
print(f'A área do círculo com raio {raio} é {areaDoCirculo:.2f}')