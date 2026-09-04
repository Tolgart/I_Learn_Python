class Vector:
    def __init__(self, *args):
        self.digits = sorted([x for x in args if type(x) == int])

    def __str__(self):
        return f"Вектор({', '.join(map(str, self.digits))})" if self.digits else 'Пустой вектор'