from maths.shapes2d import *
from maths.coordsystems import CartesianBoard

class Data:
    def __init__(self):
        self.board = CartesianBoard()
        self._populate_board()
    
    def _populate_board(self):
        # Pre-register shapes with some default data
        
        # Points
        self.board.insertShape(Point(1, 10, 20))
        self.board.insertShape(Point(2, 30, 45))
        
        # Lines
        self.board.insertShape(Line(1, 10, 20, 30, 40))
        self.board.insertShape(Line(2, 50, 60, 70, 80))
        
        # Circles
        self.board.insertShape(Circle(1, 10, 20, 15))
        self.board.insertShape(Circle(2, 30, 40, 25))
        
        # Triangles
        self.board.insertShape(Triangle(1, 10, 20, 30, 40, 50, 60))
        self.board.insertShape(Triangle(2, 15, 25, 35, 45, 55, 65))
        
        # Rectangles
        self.board.insertShape(Rectangle(1, 10, 20, 30, 40))
        self.board.insertShape(Rectangle(2, 50, 60, 70, 80))

    def get_board(self):
        return self.board