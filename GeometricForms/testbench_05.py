from package.maths.shapes2d import Triangle, Point
from package.maths.coordsystems import CartesianBoard

def workspace():

    tri1 = Triangle(1, 1, 1, 3, 1, 2, 3)
    tri2 = Triangle(2, 1, 1, 6, 1, 2, 3)
    tri3 = Triangle(3, 1, 1, 3, 1, 2, 5)
    pt1 = Point(1, 3, 2)  
    pt2 = Point(2, 5, 5)

    dashboard= CartesianBoard()
    dashboard.insertShape(tri1)
    dashboard.insertShape(tri2)
    dashboard.insertShape(tri3)
    dashboard.insertShape(pt1)
    dashboard.insertShape(pt2)
    dashboard.showShapes()

    tri1.classifyTriangle()
    tri2.classifyTriangle()
    tri3.classifyTriangle()

    print('\nOs detalhes de cada forma podem ser observados abaixo:')
    dashboard.printDetails()

    tri1.circumcircle()
    tri1.incircle()
    tri1.scale(2)
    tri1.angleA()
    tri1.angleB()
    tri1.angleC()
    tri1.centroid()
    tri1.translate(2,2)

    print(f'\nRemoção da(s) forma(s) {tri2.getType()}{tri2.getNumber()}')
    tri2.printCoord()
    dashboard.removeShape(tri2)
    dashboard.showShapes()

    print(f'\nVamos pegar uma das formas (triângulo {tri1.getNumber()}) e atualizar:')
    my_copy_of_tri1= dashboard.getShape('Triangle_1')
    my_copy_of_tri1.updateCoord(2, 1, 6, 1, 4, 4)
    my_copy_of_tri1.printCoord()

    print('\nCalculando a área e o perímetro do(s) triângulo(s):')
    tri1.area()
    tri1.perimeter()

    print("\nVerificando se o ponto está dentro do triângulo:")
    tri1.pointIn(pt1)
    tri1.pointIn(pt2)

    print("\nSuccessful exit")
    
if __name__ == "__main__":
    print('invocou o testbench01.py como programa')
    print(f'__name == {__name__}')
    workspace()
else:
    print('invocou o testbench01.py como módulo')
    print(f'__name__ == {__name__}')