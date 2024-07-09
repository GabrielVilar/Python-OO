from package.maths.shapes2d import *

class CartesianBoard():
    
    def __init__(self):
        self.shapes= {}
        
    def insertShape(self, shape):
        self.shapes[shape.getType() + str(shape.getNumber())]= shape
        
    def removeShape(self, shape):
        del self.shapes[shape.getType() + str(shape.getNumber())]
            
    def showShapes(self):
        print('\nEste plano cartesiano possui a(s) seguinte(s) forma(s):')
        for shape in self.shapes.keys():
            print(shape)
    
    def printDetails(self):
        
        for key in self.shapes.keys():
            self.shapes[key].printCoord()
    
    def getShape(self,key):
        return self.shapes[key]