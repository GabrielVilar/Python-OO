from package.maths.shapes2d import Rectangle, Point
from package.maths.coordsystems import CartesianBoard

def workspace():
    rect1 = Rectangle(1, 2, 2, 5, 10)
    rect2 = Rectangle(2, 1, 1, 8, 15)
    pt1 = Point(1,5,2)
    pt2 = Point(2,6,12)

    dashboard= CartesianBoard()
    dashboard.insertShape(rect1)
    dashboard.insertShape(rect2)
    dashboard.insertShape(pt1)
    dashboard.insertShape(pt2)
    dashboard.showShapes()

    print('\nOs detalhes de cada forma podem ser observados abaixo:')
    dashboard.printDetails()

    print(f'\nRemoção da(s) forma(s) {rect2.getType()}{rect2.getNumber()}')
    rect2.printCoord()
    dashboard.removeShape(rect2)
    dashboard.showShapes()

    print(f'\nVamos pegar uma das formas (retângulo {rect1.getNumber()}) e atualizar:')
    my_copy_of_rect1= dashboard.getShape('Rectangle_1')
    my_copy_of_rect1.updateCoord(1, 1, 6, 4)
    my_copy_of_rect1.printCoord()

    print('\nCalculando a área e o perímetro do(s) retângulo(s):')
    rect1.area()
    rect1.perimeter()

    print('\nVerificando se um ponto está dentro do retângulo:')
    print(f'O ponto {pt1.getNumber()} está dentro do retângulo {rect1.getNumber()}? {rect1.pointIn(pt1)}')
    print(f'O ponto {pt2.getNumber()} está dentro do retângulo {rect1.getNumber()}? {rect1.pointIn(pt2)}')

    print("\nSuccessful exit")
if __name__ == "__main__":
    print('invocou o testbench01.py como programa')
    print(f'__name == {__name__}')
    workspace()
else:
    print('invocou o testbench01.py como módulo')
    print(f'__name__ == {__name__}')