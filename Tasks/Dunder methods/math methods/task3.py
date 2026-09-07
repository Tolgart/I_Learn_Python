class Vector:
    def __init__(self, *args):
        self.values = sorted([num for num in args if type(num) == int])

    def __str__(self):
        if len(self.values) == 0:
            return 'Пустой вектор'
        return f'Вектор({", ".join(map(str, self.values))})'

    def __add__(self, other):
        if type(other) == int:
            return Vector(*[x + other for x in self.values])

        if isinstance(other, Vector):
            if not (len(self.values) == len(other.values)):
                print('Сложение векторов разной длины недопустимо')
                return None
            return Vector(*[x + y for x, y in zip(self.values, other.values)])

        print(f'Вектор нельзя сложить с {other}')
        return None

    def __mul__(self, other):
        if type(other) == int:
            return Vector(*[x * other for x in self.values])

        if isinstance(other, Vector):
            if not (len(self.values) == len(other.values)):
                print('Умножение векторов разной длины недопустимо')
                return None
            return Vector(*[x * y for x, y in zip(self.values, other.values)])

        print(f'Вектор нельзя умножать с {other}')
        return None

v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"