
class maths:
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    
    def __init__(self,n1,n2,n3,n4,n5):
        print('Enter the values here')
        self.a = n1
        self.b = n2
        self.c = n3
        self.d = n4
        self.e = n5


    def Addvalue(self):
        print(f'Addition = {self.a + self.b + self.c + self.d + self.e}') 

    def Subvalue(self):
        print(f'Subtraction = {self.a - self.b - self.c - self.d -self.e}')  

    def Mulvalue(self):
        print(f'Multiplication = {self.a * self.b * self.c * self.d *self.e}') 

    def Divvalue(self):
        print(f'Division = {self.a / self.b /self.c / self.d / self.e}') 

    def Meanvalue(self):
        print(f'Mean = {self.a + self.b + self.c + self.d + self.e/(5)}')   

    def Modevalue(self):
        print(f'Mode = {self.a // self.b // self.c //self.d // self.e}') 

    def Minvalue(self):
        print(f'Minimum = {min(self.a,self.b, self.c , self.d,self.e)}') 

    def Maxvalue(self):
        print(f'Maximum = {max(self.a, self.b, self.c, self.d, self.e)}')  

    def Per_75(self):
        print(f'75_percent = {((self.a + self.b + self.c + self.d + self.e))/100 * 75}')   
        
    def Per_50(self):
        print(f'50_percent = {((self.a + self.b + self.c + self.d + self.e))/100 * 50}')  

    def Per_25(self):
        print(f'25_percent = {((self.a + self.b + self.c + self.d + self.e))/100 * 25}') 


d1=maths(2,4,6,4,10)
d1.Addvalue()
d1.Subvalue()
d1.Mulvalue()
d1.Divvalue()
d1.Meanvalue()
d1.Modevalue()
d1.Minvalue()
d1.Maxvalue()
d1.Per_75()
d1.Per_50()
d1.Per_25()


             
            
                             