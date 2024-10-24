class p:
    species = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def sing(self,song):
        return "{} sings {}".format(self.name,song)
    
blu = p("Blu",24)
woo = p("Woo",26)
 
 

print(blu.sing("happily"))
