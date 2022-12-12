class Figure:
    def __init__(self, name) -> None:
        self.name = name

    def print(self):
        print(f'Figure: {self.name}')

class Square(Figure):
    def __init__(self, a) -> None:
        super().__init__('Square')
        self.a = a

class Rectangle(Figure):
    def __init__(self, a, b) -> None:
        super().__init__('Rectangle')
        self.a = a
        self.b = b

class Circle(Figure):
    def __init__(self, r) -> None:
        super().__init__('Cicle')
        self.r = r

class Ellipse(Figure):
    def __init__(self, R, r) -> None:
        super().__init__('Ellipse')
        self.R = R
        self.r = r

sq = Square(10)
sq.print()

req = Rectangle(10, 20)
req.print()

cir = Circle(15)
cir.print()

ell = Ellipse(30, 15)
ell.print()