class rectangle:
    def __init__(self,l,w):
        self.lenght = l
        self.width = w
    

    def  rectangle_area(self):
        return self.lenght*self.width
rectangle2 = rectangle(7,8)
print ("lenght: %d width: %d"%(rectangle2.lenght,rectangle2.width))
print ("area:",rectangle2.rectangle_area())