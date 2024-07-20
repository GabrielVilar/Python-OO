from package.maths.shapes2d import Line
from package.maths.shapes2d import Point
from package.maths.coordsystems import CartesianBoard

def workspace():

    line1 = Line(1, 0, 0, 3, 4)
    line2 = Line(2, 0, 1, 5, 7)
    point1 = Point(1, 3, 3)
    
    dashboard= CartesianBoard()
    dashboard.insertShape(line1)
    dashboard.insertShape(line2)
    dashboard.insertShape(point1)
    dashboard.showShapes()

    print('\nOs detalhes de cada forma podem ser observados abaixo:')
    dashboard.printDetails()

    print(f'\nVerificando se a linha {line1.getNumber()} e a linha {line2.getNumber()} são paralelas:')
    line1.isParallel(line2)

    print(f'\nRemoção da(s) forma(s) linha {line2.getNumber()}')
    line2.printCoord()
    dashboard.removeShape(line2)
    dashboard.showShapes()

    print(f'\nVamos pegar a linha {line1.getNumber()} e atualizar:')
    my_copy_of_line1= dashboard.getShape('Line_1')
    my_copy_of_line1.updateCoord(1, 1, 3, 1)
    my_copy_of_line1.printCoord()    

    print(f'\nCalculando o comprimento da linha {line1.getNumber()}')
    line1.length()

    print(f'\nCalculando a inclinação da linha {line1.getNumber()}')
    line1.slope()

    print(f'\nVerificando se o ponto {point1.getNumber()} está na linha {line1.getNumber()}')
    print(f'O ponto {point1.getNumber()} que tem as coordenadas {point1._x, point1._y} está sobre a linha {line1.getNumber()}? {line1.pointOnLine(point1)}')

    print("\nSuccessful exit")

if __name__ == "__main__":
    print('invocou o testbench01.py como programa')
    print(f'__name == {__name__}')
    workspace()
else:
    print('invocou o testbench01.py como módulo')
    print(f'__name__ == {__name__}')