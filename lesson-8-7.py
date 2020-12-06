"""7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return ComplexNumber((self.re + other.re), (self.im + other.im))

    def __mul__(self, other):
        return ComplexNumber((self.re * other.re - (self.im * other.im)), (self.re * other.im + (other.re * self.im)))

    def __str__(self):
        if self.re == 0:
            return f'{self.im}i'
        elif self.im == 0:
            return f'{self.re}'
        else:
            return f'{self.re} {"+" if self.im > 0 else "-"} {abs(self.im)}i'


comp_1 = ComplexNumber(5, -2)
comp_2 = ComplexNumber(-5, 3)
comp_3 = ComplexNumber(3, 6)
print(comp_1)
print(comp_2)
print(comp_3)
print('Sum = ', comp_1 + comp_2 + comp_3)
print('Sum = ', comp_1 + comp_2)
print('Mul = ', comp_1 * comp_2 * comp_3)
