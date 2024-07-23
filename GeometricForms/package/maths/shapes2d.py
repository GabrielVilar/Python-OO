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

    def distanceTo(self, other_point):
        distance = math.sqrt((self._x - other_point._x) ** 2 + (self._y - other_point._y) ** 2)
        print(f'A distância do ponto {self._n} até o ponto {other_point._n} é de {distance:.2f} cm')
        return distance
    
    def midpoint(self, other_point):
        mid_x = (self._x + other_point._x) / 2
        mid_y = (self._y + other_point._y) / 2
        print(f'O ponto médio entre o ponto {self._n} e o ponto {other_point._n} é ({mid_x}, {mid_y})')
        return Point(0, mid_x, mid_y)

class Line():
    def __init__(self, n, x1, y1, x2, y2):
        self._n = n
        self._p1 = Point(n, x1, y1)
        self._p2 = Point(n, x2, y2)

    def updateCoord(self, x1, y1, x2, y2):
        self._p1.updateCoord(x1, y1)
        self._p2.updateCoord(x2, y2)

    def getType(self):
        return 'Line_'

    def getNumber(self):
        return self._n

    def printCoord(self):
        print(f'\nA linha {self._n} possui as coord: ({self._p1._x}, {self._p1._y}) e ({self._p2._x}, {self._p2._y}).')

    def length(self):
        """ Calcula o comprimento da linha """
        length = math.sqrt((self._p2._x - self._p1._x) ** 2 + (self._p2._y - self._p1._y) ** 2)
        print(f'O comprimento da linha {self._n} é {length:.2f} cm')
        return length

    def pointOnLine(self, pt):
        """ Verifica se um ponto está sobre a linha """
        tolerance = 1e-9
        if (self._p2._x - self._p1._x) == 0:  # Linha vertical
            return abs(pt._x - self._p1._x) < tolerance
        else:
            slope = (self._p2._y - self._p1._y) / (self._p2._x - self._p1._x)
            intercept = self._p1._y - slope * self._p1._x
            return abs(pt._y - (slope * pt._x + intercept)) < tolerance
        
    def verifyVertical(self):
        if self._p2._x == self._p1._x:
            print(f'\nA linha {self._n} é uma linha vertical portanto não tem uma inclinação definida')
            return True
        return False
    
    def slope(self):
        if self.verifyVertical() == False:
            slope = (self._p2._y - self._p1._y) / (self._p2._x - self._p1._x)
            print(f'A inclinação da linha {self._n} é {slope:.2f}')
            if slope == 0:
                print(f'A linha {self._n} é uma linha horizontal')
            return slope 
    
    def isParallel(self, other_line):
        if self.slope() == other_line.slope():
            print(f'A linha {self._n} e a linha {other_line._n} são paralelas')
            return True
        else:
            print(f'A linha {self._n} e a linha {other_line._n} não são paralelas')
            return False
        
class Circle(Point):
    
    def __init__(self,n,x,y,radius):
        super().__init__(n, x, y)
        self._radius= radius
        
    def getType(self):
        return 'Circle_'
        
    def updateCoord(self,x,y,radius):        
        super().updateCoord(x, y)
        self._radius= radius

    def printCoord(self):
        print(f'\nO círculo {self._n} possui origem em: ({self._x}, {self._y})')
        print(f'E o seu raio é {self._radius}')
        
    def pointIn(self,pt):
        """ Verifica se o ponto está dentro deste círculo"""
        squared_distance = math.sqrt(((self._x - pt._x)**2 + (self._y - pt._y)**2))
        return squared_distance <= self._radius
    
    def area(self):
        """ calcula a área deste circulo e mostra no terminal"""
        area = math.pi * (self._radius ** 2)
        print(f'A área do círculo {self._n} é {area:.2f} cm')
        return area
    
    def perimeter(self):
        """ calcula o perímetro deste círculo e mostra no terminal"""
        perimeter = 2 * math.pi * self._radius
        print(f'O perímetro do círculo {self._n} é {perimeter:.2f} cm')
        return perimeter
    
    def diameter(self):
        """ calcula o diâmetro deste círculo e mostra no terminal"""
        diameter = 2 * self._radius
        print(f'O diâmetro do círculo {self._n} é: {diameter:.2f} cm')
        return diameter
    
    def circumference(self):
        circumference = 2 * math.pi * self._radius
        print(f'A circunferência do círculo {self._n} é {circumference:.2f}')
        return circumference
    
    def center(self):
        """ Retorna o centro do círculo """
        return (self._x, self._y)
    
    def isTangent(self, other_circle):
        """ Verifica se este círculo é tangente ao outro círculo """
        distance_between_centers = math.sqrt((self._x - other_circle._x)** 2 + (self._y - other_circle._y)**2)
        radius_sum = self._radius + other_circle._radius
        radius_diff = abs(self._radius - other_circle._radius)
        if distance_between_centers == radius_sum or distance_between_centers == radius_diff:
            print(f'O círculo {self._n} é tangente ao círculo {other_circle._n}')
            return True
        else:
            print(f'O círculo {self._n} não é tangente ao círculo {other_circle._n}')
            return False
    
    def isConcentric(self, other_circle):
        """ Verifica se este círculo é concêntrico com o outro círculo """
        if self._x == other_circle._x and self._y == other_circle._y:
            print(f'O círculo {self._n} é concêntrico com o círculo {other_circle._n}')
            return True
        else:
            print(f'O círculo {self._n} não é concêntrico com o círculo {other_circle._n}')
            return False
    
    def translate(self, dx, dy):
        """ Translada o círculo por (dx, dy) """
        self._x += dx
        self._y += dy
        print(f'O círculo {self._n} foi transladado para ({self._x}, {self._y})')

    def scale(self, factor):
        """ Escala o raio do círculo pelo fator dado """
        self._radius *= factor
        print(f'O círculo {self._n} foi escalado para raio {self._radius:.2f}')

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
        is_inside = (min(self._p1._x, self._p2._x) <= pt._x <= max(self._p1._x, self._p2._x) and
                     min(self._p1._y, self._p2._y) <= pt._y <= max(self._p1._y, self._p2._y))
        if is_inside:
            print(f'O ponto {pt._n} está dentro do retângulo {self._n}.')
        else:
            print(f'O ponto {pt._n} não está dentro do retângulo {self._n}.')
        return is_inside
    
    def diagonal(self):
        width = abs(self._p2._x - self._p1._x)
        height = abs(self._p2._y - self._p1._y)
        diagonal = math.sqrt(width**2 + height**2)
        print(f'A diagonal do retângulo {self._n} é {diagonal:.2f}')
        return diagonal
    
    def rotate(self, angle):
        """ Rotaciona o retângulo em torno do seu centro por um dado ângulo """
        center_x = (self._p1._x + self._p2._x) / 2
        center_y = (self._p1._y + self._p2._y) / 2
        angle_rad = math.radians(angle)

        def rotate_point(px, py):
            translated_x = px - center_x
            translated_y = py - center_y
            rotated_x = translated_x * math.cos(angle_rad) - translated_y * math.sin(angle_rad)
            rotated_y = translated_x * math.sin(angle_rad) + translated_y * math.cos(angle_rad)
            return rotated_x + center_x, rotated_y + center_y

        new_p1_x, new_p1_y = rotate_point(self._p1._x, self._p1._y)
        new_p2_x, new_p2_y = rotate_point(self._p2._x, self._p2._y)
        
        self.updateCoord(new_p1_x, new_p1_y, new_p2_x, new_p2_y)
        print(f'O retângulo {self._n} foi rotacionado em {angle} graus.')

    def isSquare(self):
        """ Verifica se o retângulo é um quadrado """
        width = abs(self._p2._x - self._p1._x)
        height = abs(self._p2._y - self._p1._y)
        if width == height:
            print(f'O retângulo {self._n} é um quadrado.')
            return True
        else:
            print(f'O retângulo {self._n} não é um quadrado.')
            return False
        
    def translate(self, dx, dy):
        """ Translada o retângulo por (dx, dy) """
        self._p1._x += dx
        self._p1._y += dy
        self._p2._x += dx
        self._p2._y += dy
        print(f'O retângulo {self._n} foi transladado para ({self._p1._x}, {self._p1._y}) e ({self._p2._x}, {self._p2._y}).')

    def scale(self, factor):
        """ Escala o retângulo por um dado fator """
        center_x = (self._p1._x + self._p2._x) / 2
        center_y = (self._p1._y + self._p2._y) / 2
        new_width = abs(self._p2._x - self._p1._x) * factor
        new_height = abs(self._p2._y - self._p1._y) * factor
        self._p1._x = center_x - new_width / 2
        self._p2._x = center_x + new_width / 2
        self._p1._y = center_y - new_height / 2
        self._p2._y = center_y + new_height / 2
        print(f'O retângulo {self._n} foi escalado para um novo tamanho com fator {factor}.')

    def intersects(self, other_rectangle):
        """ Verifica se este retângulo intersecta com outro retângulo """
        if (self._p1._x < other_rectangle._p2._x and self._p2._x > other_rectangle._p1._x and
            self._p1._y < other_rectangle._p2._y and self._p2._y > other_rectangle._p1._y):
            print(f'O retângulo {self._n} intersecta com o retângulo {other_rectangle._n}.')
            return True
        else:
            print(f'O retângulo {self._n} não intersecta com o retângulo {other_rectangle._n}.')
            return False

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
    
    def classifyTriangle(self):
        side1 = math.sqrt((self._p2._x - self._p1._x) ** 2 + (self._p2._y - self._p1._y) ** 2)
        side2 = math.sqrt((self._p3._x - self._p2._x) ** 2 + (self._p3._y - self._p2._y) ** 2)
        side3 = math.sqrt((self._p1._x - self._p3._x) ** 2 + (self._p1._y - self._p3._y) ** 2)
    
        # Round the side lengths
        side1 = round(side1)
        side2 = round(side2)
        side3 = round(side3)

        if side1 == side2 == side3:
            triangle_type = 'Equilateral'
        elif side1 == side2 or side2 == side3 or side1 == side3:
            triangle_type = 'Isosceles'
        else:
            triangle_type = 'Scalene'
        
        print(f'O triângulo {self._n} é {triangle_type}.')
        return triangle_type
    
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
    
    def circumcircle(self):
        """Calculando o centro do círculo que passa por todos os pontos do triângulo"""
        A = self._p1._x * (self._p2._y - self._p3._y) + self._p2._x * (self._p3._y - self._p1._y) + self._p3._x * (self._p1._y - self._p2._y)
        D = (self._p1._x**2 + self._p1._y**2) * (self._p2._y - self._p3._y) + (self._p2._x**2 + self._p2._y**2) * (self._p3._y - self._p1._y) + (self._p3._x**2 + self._p3._y**2) * (self._p1._y - self._p2._y)
        E = (self._p1._x**2 + self._p1._y**2) * (self._p3._x - self._p2._x) + (self._p2._x**2 + self._p2._y**2) * (self._p1._x - self._p3._x) + (self._p3._x**2 + self._p3._y**2) * (self._p2._x - self._p1._x)
        F = (self._p1._x**2 + self._p1._y**2) * (self._p2._x * self._p3._y - self._p3._x * self._p2._y) + (self._p2._x**2 + self._p2._y**2) * (self._p3._x * self._p1._y - self._p1._x * self._p3._y) + (self._p3._x**2 + self._p3._y**2) * (self._p1._x * self._p2._y - self._p2._x * self._p1._y)
        # Assegurando que A é positivo
        if A < 0:
            A = -A
            D = -D
            E = -E
            F = -F

        circumcenter_x = D / (2 * A)
        circumcenter_y = E / (2 * A)
        circumradius = math.sqrt((D**2 + E**2 - 4*A*F) / (4 * A**2))
        
        print(f'\nO circuncírculo do triângulo {self._n} tem centro em ({circumcenter_x:.2f}, {circumcenter_y:.2f}) e raio {circumradius:.2f}')
        return (circumcenter_x, circumcenter_y, circumradius)
    
    def incircle(self):
        """Calculando o centro do círculo que é tangente de todos os lados do triângulo e cabe dentro"""
        side1 = math.sqrt((self._p2._x - self._p1._x) ** 2 + (self._p2._y - self._p1._y) ** 2)
        side2 = math.sqrt((self._p3._x - self._p2._x) ** 2 + (self._p3._y - self._p2._y) ** 2)
        side3 = math.sqrt((self._p1._x - self._p3._x) ** 2 + (self._p1._y - self._p3._y) ** 2)
        perimeter = side1 + side2 + side3
        incenter_x = (side1 * self._p3._x + side2 * self._p1._x + side3 * self._p2._x) / perimeter
        incenter_y = (side1 * self._p3._y + side2 * self._p1._y + side3 * self._p2._y) / perimeter
        s = perimeter / 2
        area = self.area()
        inradius = area / s
        print(f'O incentro do triângulo {self._n} está em ({incenter_x:.2f}, {incenter_y:.2f}) com raio {inradius:.2f}')
        return (incenter_x, incenter_y, inradius)
    
    def translate(self, dx, dy):
        self._p1._x += dx
        self._p1._y += dy
        self._p2._x += dx
        self._p2._y += dy
        self._p3._x += dx
        self._p3._y += dy
        print(f'O triângulo {self._n} foi transladado para ({self._p1._x}, {self._p1._y}), ({self._p2._x}, {self._p2._y}) e ({self._p3._x}, {self._p3._y}).')

    def scale(self, factor):
        center_x = (self._p1._x + self._p2._x + self._p3._x) / 3
        center_y = (self._p1._y + self._p2._y + self._p3._y) / 3
        
        def scale_point(px, py):
            return center_x + factor * (px - center_x), center_y + factor * (py - center_y)
        
        self._p1._x, self._p1._y = scale_point(self._p1._x, self._p1._y)
        self._p2._x, self._p2._y = scale_point(self._p2._x, self._p2._y)
        self._p3._x, self._p3._y = scale_point(self._p3._x, self._p3._y)
        
        print(f'O triângulo {self._n} foi escalado com um fator de {factor}.')

    def pointIn(self, pt):
        def sign(p1, p2, p3):
            return (p1._x - p3._x) * (p2._y - p3._y) - (p2._x - p3._x) * (p1._y - p3._y)

        b1 = sign(pt, self._p1, self._p2) < 0.0
        b2 = sign(pt, self._p2, self._p3) < 0.0
        b3 = sign(pt, self._p3, self._p1) < 0.0

        is_inside = (b1 == b2) and (b2 == b3)
        if is_inside:
            print(f'O ponto {pt._n} está dentro do triângulo {self._n}.')
        else:
            print(f'O ponto {pt._n} não está dentro do triângulo {self._n}.')
        return is_inside
    
    def angleA(self):
        side1 = math.sqrt((self._p2._x - self._p1._x) ** 2 + (self._p2._y - self._p1._y) ** 2)
        side2 = math.sqrt((self._p3._x - self._p2._x) ** 2 + (self._p3._y - self._p2._y) ** 2)
        side3 = math.sqrt((self._p1._x - self._p3._x) ** 2 + (self._p1._y - self._p3._y) ** 2)
        angle = math.acos((side2**2 + side3**2 - side1**2) / (2 * side2 * side3))
        angle_deg = math.degrees(angle)
        print(f'O ângulo A do triângulo {self._n} é {angle_deg:.2f} graus.')
        return angle_deg

    def angleB(self):
        side1 = math.sqrt((self._p2._x - self._p1._x) ** 2 + (self._p2._y - self._p1._y) ** 2)
        side2 = math.sqrt((self._p3._x - self._p2._x) ** 2 + (self._p3._y - self._p2._y) ** 2)
        side3 = math.sqrt((self._p1._x - self._p3._x) ** 2 + (self._p1._y - self._p3._y) ** 2)
        angle = math.acos((side1**2 + side3**2 - side2**2) / (2 * side1 * side3))
        angle_deg = math.degrees(angle)
        print(f'O ângulo B do triângulo {self._n} é {angle_deg:.2f} graus.')
        return angle_deg

    def angleC(self):
        side1 = math.sqrt((self._p2._x - self._p1._x) ** 2 + (self._p2._y - self._p1._y) ** 2)
        side2 = math.sqrt((self._p3._x - self._p2._x) ** 2 + (self._p3._y - self._p2._y) ** 2)
        side3 = math.sqrt((self._p1._x - self._p3._x) ** 2 + (self._p1._y - self._p3._y) ** 2)
        angle = math.acos((side1**2 + side2**2 - side3**2) / (2 * side1 * side2))
        angle_deg = math.degrees(angle)
        print(f'O ângulo C do triângulo {self._n} é {angle_deg:.2f} graus.')
        return angle_deg

    def centroid(self):
        centroid_x = (self._p1._x + self._p2._x + self._p3._x) / 3
        centroid_y = (self._p1._y + self._p2._y + self._p3._y) / 3
        print(f'O centróide do triângulo {self._n} está em ({centroid_x:.2f}, {centroid_y:.2f}).')
        return (centroid_x, centroid_y)