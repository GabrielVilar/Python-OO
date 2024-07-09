from package.maths.shapes2d import Point
from package.maths.coordsystems import CartesianBoard

def workspace():
    
    point1= Point(1,12,54)
    point2= Point(2,15,22)

    dashboard= CartesianBoard()
    dashboard.insertShape(point1)
    dashboard.insertShape(point2)
    dashboard.showShapes()

    print('\nOs detalhes de cada forma podem ser observados abaixo:')
    dashboard.printDetails()

    print(f'\nRemovendo o ponto {point2.getNumber()}')
    point2.printCoord()
    dashboard.removeShape(point2)
    dashboard.showShapes()
    
    print(f'\nVamos pegar o ponto {point1.getNumber()} e atualizar:')
    my_copy_of_point1= dashboard.getShape('Point_1')
    my_copy_of_point1.updateCoord(2,5)
    my_copy_of_point1.printCoord()

    print("\nSuccessful exit")

if __name__ == "__main__":
    print('invocou o testbench01.py como programa')
    print(f'__name == {__name__}')
    workspace()

else:
    print('invocou o testbench01.py como módulo')
    print(f'__name__ == {__name__}')