class Figure:
    def __init__(self, name) -> None:
        self.name = name

    def area(self):
        pass

    def print(self):
        print(f'Figure: {self.name}. Area: {self.area()}')

class Square(Figure):
    def __init__(self, a) -> None:
        super().__init__('Square')
        self.a = a

    def area(self):
        return self.a **2

class Rectangle(Figure):
    def __init__(self, a, b) -> None:
        super().__init__('Rectangle')
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

class Circle(Figure):
    def __init__(self, r) -> None:
        super().__init__('Cicle')
        self.r = r
    
    def area(self):
        return 3.14 * (self.r **2)

class Ellipse(Figure):
    def __init__(self, R, r) -> None:
        super().__init__('Ellipse')
        self.R = R
        self.r = r

    def area(self):
        return 3.14 * self.R * self.r

sq = Square(10)
sq.print()

req = Rectangle(10, 20)
req.print()

cir = Circle(15)
cir.print()

ell = Ellipse(30, 15)
ell.print()