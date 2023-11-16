class TriangleChecker:

    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def is_triangle(self):
        if isinstance(self.num1, int) and isinstance(self.num2, int) and isinstance(self.num3, int):
            if self.num1 > 0 and self.num2 > 0 and self.num3 > 0:

                if self.num1 + self.num2 > self.num3 or self.num2 + self.num3 > self.num1 or self.num1 + self.num3 > self.num2:
                    return 'Ура, можно построить треугольник!'
                else:
                    return 'Жаль, но из этого треугольник не сделать.'
            else:
                return ' С отрицательными числами ничего не выйдет!'
        else:
            return 'Нужно вводить только числа!'


print(TriangleChecker('hy', 32, 41).is_triangle())
