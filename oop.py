#sample prgm
class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram        
        
    def config(self):
        print("Config",self.cpu,self.ram)

comp1 = Computer('i5','1TB')  
comp2 = Computer('Ryzen 3','8TB')  

comp1.config()
comp2.config()