# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц


class Matrix:
    """
    Класс Matrix представляет собой матрицу с базовыми операциями сложения, умножения и сравнения.
    """

    def __init__(self, rows, columns):
        """
        Инициализирует объект матрицы с заданным количеством строк и столбцов.

        :param rows: Количество строк в матрице.
        :type rows: int
        :param columns: Количество столбцов в матрице.
        :type columns: int
        """
        self.rows = rows
        self.columns = columns
        self.data = [[0 for _ in range(columns)] for _ in range(rows)]

    def __str__(self):
        """
        Возвращает строковое представление матрицы.

        :return: Строковое представление матрицы.
        :rtype: str
        """
        result = ""
        for row in self.data:
            result += " ".join(str(element) for element in row) + "\n"
        return result

    def __eq__(self, other):
        """
        Проверяет, равны ли две матрицы.

        :param other: Другая матрица, с которой происходит сравнение.
        :type other: Matrix
        :return: True, если матрицы равны, иначе False.
        :rtype: bool
        """

    def __eq__(self, other):
        """
        Проверяет, равны ли две матрицы.

        :param other: Другая матрица, с которой происходит сравнение.
        :type other: Matrix
        :return: True, если матрицы равны, иначе False.
        :rtype: bool
        :raises ValueError: Если матрицы имеют разные размеры.
        """
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError(
                "Матрицы должны иметь одинаковый размер для сравнения")
        return True

    def __add__(self, other):
        """
        Выполняет сложение двух матриц.

        :param other: Матрица, которая складывается с текущей матрицей.
        :type other: Matrix
        :return: Результат сложения матриц.
        :rtype: Matrix
        :raises ValueError: Если матрицы имеют разные размеры.
        """
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError(
                "Матрицы должны иметь одинаковый размер для сложения")

        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        """
        Выполняет умножение двух матриц.

        :param other: Матрица, на которую умножается текущая матрица.
        :type other: Matrix
        :return: Результат умножения матриц.
        :rtype: Matrix
        :raises ValueError: Если количество столбцов в первой матрице не равно количеству строк во второй матрице.
        """
        if self.columns != other.rows:
            raise ValueError(
                "Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице")

        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result


matrix1 = Matrix(2, 2)
matrix1.data = [[1, 2], [3, 4]]

matrix2 = Matrix(2, 2)
matrix2.data = [[5, 6], [7, 8]]

print("Матрица 1:")
print(matrix1)

print("Матрица 2:")
print(matrix2)

try:
    print("Сравнение матриц:")
    print(matrix1 == matrix2)

    sum_matrix = matrix1 + matrix2
    print("Сумма матриц:")
    print(sum_matrix)

    product_matrix = matrix1 * matrix2
    print("Произведение матриц:")
    print(product_matrix)
except ValueError as e:
    print("Ошибка:", e)


# help(Matrix)
# help(Matrix.__str__)
# help(Matrix.__eq__)
# help(Matrix.__add__)
# help(Matrix.__mul__)