
base = None
altura = None

while True:
    try:
        base = float(input('Digite La Base Del Triangulos:'))
        break
    except:
        print('Debe Digitar El Numero.')

while True:
    try:
        altura = float(input('Digite La Altura Del Triangulos:'))
        break
    except:
        print('Debe Digitar El Numero.')

area = base * altura / 2

print('El Area Del Triangulo Es: {}'.format(area))