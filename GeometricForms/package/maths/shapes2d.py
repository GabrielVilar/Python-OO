import math
class Point():

    def __init__(self,n,x,y):
        self._n= n
        self._x= x
        self._y= y

    def updateCoord(self,x,y):
        self._x= x
        self._y= y
    
    def getType(self):
        return 'Point_'
        
    def getNumber(self):
        return self._n

    def printCoord(self):
        print(f'\nO ponto {self._n} possui as coordenadas: ({self._x}, {self._y}).') 

class Line():
    
    def __init__(self, n, x1, y1, x2, y2):
        self._n = n
        self._p1 = Point(n, x1, y1)
        self._p2 = Point(n, x2, y2)
    
    def updateCoord(self, x1, y1, x2, y2):
        self._p1.updateCoord(x1,y1)
        self._p2.updateCoord(x2,y2)
    
    def getType(self):
        return 'Line_'
        
    def getNumber(self):
        return self._n

    def printCoord(self):
        print(f'\nA linha {self._n} possui as coord: ({self._x1}, {self._y1}) e ({self._x2}, {self._y2}).')
        
    def length(self):
        """ Calcula o comprimento da linha """
        length = math.sqrt((self._x2 - self._x1) ** 2 + (self._y2 - self._y1) ** 2)
        print(f'O comprimento da linha {self._n} é {length:.2f} cm')
        return length
    
    def pointOnLine(self, pt):
        """ Verifica se um ponto está sobre a linha """
        tolerance=1e-9
        if (self._x2 - self._x1) == 0:  # Linha vertical
            return abs(pt._x - self._x1) < tolerance
        else:
            slope = (self._y2 - self._y1) / (self._x2 - self._x1)
            intercept = self._y1 - slope * self._x1
            return abs(pt._y - (slope * pt._x + intercept)) < tolerance       

class Circle(Point):
    
    def __init__(self,n,x,y,radius):
        super().__init__(n, x, y)
        self.radius= radius
        
    def getType(self):
        return 'Circle_'
        
    def updateCoord(self,x,y,radius):        
        super().updateCoord(x, y)
        self.radius= radius

    def printCoord(self):
        print(f'\nO círculo {self._n} possui origem em: ({self._x}, {self._y})')
        print(f'E o seu raio é {self.radius}')
        
    def pointIn(self,pt):
        """ Verifica se o ponto está dentro deste círculo"""
        squared_distance = math.sqrt(((self._x - pt._x)**2 + (self._y - pt._y)**2))
        return squared_distance <= self.radius
    
    def area(self):
        """ calcula a área deste circulo e mostra no terminal"""
        area = math.pi * (self.radius ** 2)
        print(f'A área do círculo {self._n} é {area:.2f} cm')
        return area
    
    def perimeter(self):
        """ calcula o perímetro deste círculo e mostra no terminal"""
        perimeter = 2 * math.pi * self.radius
        print(f'O perímetro do círculo {self._n} é {perimeter:.2f} cm')
        return perimeter
    
    def diameter(self):
        """ calcula o diâmetro deste círculo e mostra no terminal"""
        diameter = 2 * self.radius
        print(f'O diâmetro do círculo {self._n} é: {diameter:.2f} cm')
        return diameter

class Rectangle():
    
    def __init__(self, n, x1, y1, x2, y2):
        self._n = n
        self._p1 = Point(n, x1, y1)
        self._p2 = Point(n, x2, y2)
    
    def updateCoord(self, x1, y1, x2, y2):
        self._p1.updateCoord(x1,y1)
        self._p2.updateCoord(x2,y2)
    
    def getType(self):
        return 'Rectangle_'
    
    def getNumber(self):
        return self._n
    
    def printCoord(self):
        print(f'\nO retângulo {self._n} possui as coord: ({self._p1._x}, {self._p1._y}) e ({self._p2._x}, {self._p2._y}).')
        
    def area(self):
        width = abs(self._p2._x - self._p1._x)
        height = abs(self._p2._y - self._p1._y)
        area = width * height
        print(f'A área do retângulo {self._n} é {area:.2f}')
        return area
    
    def perimeter(self):
        width = abs(self._p2._x - self._p1._x)
        height = abs(self._p2._y - self._p1._y)
        perimeter = 2 * (width + height)
        print(f'O perímetro do retângulo {self._n} é {perimeter:.2f}')
        return perimeter
    
    def pointIn(self, pt):
         return (min(self._p1._x, self._p2._x) <= pt._x <= max(self._p1._x, self._p2._x) and
                min(self._p1._y, self._p2._y) <= pt._y <= max(self._p1._y, self._p2._y))

class Triangle():
    def __init__(self, n, x1, y1, x2, y2, x3, y3):
        self._n = n
        self._p1 = Point(n, x1, y1)
        self._p2 = Point(n, x2, y2)
        self._p3 = Point(n, x3, y3)

    def updateCoord(self, x1, y1, x2, y2, x3, y3):
        self._p1.updateCoord(x1, y1)
        self._p2.updateCoord(x2, y2)
        self._p3.updateCoord(x3, y3)
    
    def getType(self):
        return 'Triangle_'
        
    def getNumber(self):
        return self._n

    def printCoord(self):
        print(f'\nO triângulo {self._n} possui as coord: ({self._p1._x}, {self._p1._y}), ({self._p2._x}, {self._p2._y}) e ({self._p3._x}, {self._p3._y}).')
        
    def area(self):
        area = abs((self._p1._x * (self._p2._y - self._p3._y) + self._p2._x * (self._p3._y - self._p1._y) + self._p3._x * (self._p1._y - self._p2._y)) / 2)
        print(f'A área do triângulo {self._n} é {area:.2f}')
        return area
    
    def perimeter(self):
        side1 = math.sqrt((self._p2._x - self._p1._x) ** 2 + (self._p2._y - self._p1._y) ** 2)
        side2 = math.sqrt((self._p3._x - self._p2._x) ** 2 + (self._p3._y - self._p2._y) ** 2)
        side3 = math.sqrt((self._p1._x - self._p3._x) ** 2 + (self._p1._y - self._p3._y) ** 2)
        perimeter = side1 + side2 + side3
        print(f'O perímetro do triângulo {self._n} é {perimeter:.2f}')
        return perimeter
    
    def pointIn(self, pt):
        def sign(p1, p2, p3):
            return (p1._x - p3._x) * (p2._y - p3._y) - (p2._x - p3._x) * (p1._y - p3._y)

        b1 = sign(pt, self._p1, self._p2) < 0.0
        b2 = sign(pt, self._p2, self._p3) < 0.0
        b3 = sign(pt, self._p3, self._p1) < 0.0

        return (b1 == b2) and (b2 == b3)