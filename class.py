class Test:
    def f1(self,b):
        self.a = 10
        self.b = b
        print("abc")

    @staticmethod
    def f2():
        print("static method")
    
    @classmethod
    def f3(palpal):
        palpal.x = 5
        print('class method')

def fun():
    print("non member fn")

t1 = Test()
t1.b = 11
t1.f1(5)