from package.maths.shapes2d import Circle, Point
from package.maths.coordsystems import CartesianBoard

def workspace():

    circ1= Circle(1, 13, 15, 4)
    circ2= Circle(2, 17, 27, 8)
    pt1 = Point(1,2,4)
    pt2 = Point(2,1,1)

    dashboard= CartesianBoard()
    dashboard.insertShape(circ1)
    dashboard.insertShape(circ2)
    dashboard.insertShape(pt1)
    dashboard.insertShape(pt2)
    dashboard.showShapes()

    print('\nOs detalhes de cada forma podem ser observados abaixo:')
    dashboard.printDetails()

    print(f'\nVerificando se o circulo {circ1.getNumber()} é tangente ao circulo {circ2.getNumber()}:')
    circ1.isTangent(circ2)

    print(f'\nVerificando se o círculo {circ1.getNumber()} é concêntrico ao círculo {circ2.getNumber()}:')
    circ1.isConcentric(circ2)

    print(f'\nRemoção da(s) forma(s) {circ2.getType()}{circ2.getNumber()}')
    circ2.printCoord()
    dashboard.removeShape(circ2)
    dashboard.showShapes()

    print(f'\nTransladando o centro do círculo {circ1.getNumber()}:')
    circ1.translate(6,7)

    print(f'\nEscalando o raio do círculo {circ1.getNumber()} por um determinado fator:')   
    circ1.scale(7) 

    print(f'\nVamos pegar uma das formas (círculo {circ1.getNumber()}) e atualizar:')
    my_copy_of_circ1= dashboard.getShape('Circle_1')
    my_copy_of_circ1.updateCoord(3,3,2)
    my_copy_of_circ1.printCoord()

    print(f'\nCalculando a área o perímetro o diâmetro e a circunferência do(s) círculo(s):')
    circ1.area()
    circ1.perimeter()   
    circ1.diameter()
    circ1.circumference()

    print("\nVerificando se o ponto está dentro do círculo:")
    print(f'O ponto {pt1.getNumber()} está dentro do círculo {circ1.getNumber()}? {circ1.pointIn(pt1)}')
    print(f'O ponto {pt2.getNumber()} está dentro do círculo {circ1.getNumber()}? {circ1.pointIn(pt2)}')

    print("\nSuccessful exit")
    
if __name__ == "__main__":
    print('invocou o testbench01.py como programa')
    print(f'__name == {__name__}')
    workspace()
else:
    print('invocou o testbench01.py como módulo')
    print(f'__name__ == {__name__}')