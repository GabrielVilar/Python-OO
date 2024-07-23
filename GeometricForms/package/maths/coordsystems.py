from maths.shapes2d import *

class CartesianBoard():
    
    def __init__(self):
        self.shapes= {}
        
    def insertShape(self, shape):
        key = shape.getType() + str(shape.getNumber())
        self.shapes[key] = shape
        
    def removeShape(self, shape):
        del self.shapes[shape.getType() + str(shape.getNumber())]
            
    def showShapes(self):
        print('\nEste plano cartesiano possui a(s) seguinte(s) forma(s):')
        for key in self.shapes.keys():
            print(f"Key: {key}, Shape: {self.shapes[key]}")
    
    def printDetails(self):        
        for key in self.shapes.keys():
            self.shapes[key].printCoord()
    
    def getShape(self,key):
        if key in self.shapes:
            return self.shapes[key]
        else:
            raise KeyError(f"Shape with key {key} does not exist.")