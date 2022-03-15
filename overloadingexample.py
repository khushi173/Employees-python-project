#overloading ==>

class A:
    def myCalculate(self,x = None, y = None):
        if x != None and y !=None:
            return x+y