import math


def gcd(a, b):
    """
    calculate greatest common divisor of a and b using Euclid's Algorithm
    :param a: an integer
    :param b: another integer
    :return: common divisor of a and b
    """
    if a < 0: a = -a
    if b < 0: b = -b
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def lcm(a, b):
    """
    calculate the least common multiple of a and b
    :param a:
    :param b:
    :return:
    """
    if a < 0: a = -a
    if b < 0: b = -b
    d = gcd(a, b)
    return a * b // d


class Fraction:
    """
    A class represent the fractional number, used for keeping accuracy of the calculation
    """
    def __init__(self, denominator: int, numerator: int):
        """
        construct a fractional number use the given denominator and numerator
        :param denominator:
        :param numerator:
        """
        # check for sign
        self.__sign = 1
        if denominator < 0:
            self.__sign = -self.__sign
            denominator = -denominator
        if numerator < 0:
            self.__sign = -self.__sign
            numerator = -numerator

        # if the value of the fractional number is greater than 10000, leave out the fractional part
        if numerator // denominator > 10**4:
            numerator = numerator // denominator
            denominator = 1

        # if the denominator is too large, use approximate value instead (cut down the number below 10000)
        while denominator > 10**4:
            denominator /= 10
            numerator /= 10
        self.__denom = math.floor(denominator)
        self.__num = math.floor(numerator)
        self.__simp()

    @classmethod
    def copy(cls, f: "Fraction"):
        """
        make a copy of the given fraction
        :param f:
        :return:
        """
        return Fraction(f.__denom, f.__num * f.__sign)

    @classmethod
    def from_int(cls, a: int):
        """
        make a fraction from the given int
        :param a:
        :return:
        """
        return Fraction(1, a)

    @classmethod
    def from_float(cls, a: float):
        """
        make a fraction from the given float
        :param a:
        :return:
        """
        fp = str(a).split(".")[-1]
        # check the length of fractional part of the float
        # if equal or more than 8 digit, it will be seen as a repeating sequence of the first 4 digit
        # if more than 4 digit but less than 8 digit, only the first 4 digit will be kept
        if len(fp) > 7:
            return Fraction(9999, math.floor(a * 10000) - math.floor(a))
        else:
            return Fraction(10000, math.floor(a * 10000))

    @classmethod
    def convert(cls, a):
        """
        convert integer, float or another fraction to a fraction
        :param a:
        :return:
        """
        if type(a) == Fraction: return cls.copy(a)
        if type(a) == int: return Fraction.from_int(a)
        if type(a) == float: return Fraction.from_float(a)
        else:
            raise Exception("invalid type")

    def __simp(self):
        """
        simplify the fraction represent by this object
        :return:
        """
        d = gcd(self.__denom, self.__num)
        self.__denom = self.__denom // d
        self.__num = self.__num // d

    def inverse(self):
        """
        calculate the inverse of this fraction
        :return:
        """
        return Fraction(self.__num * self.__sign, self.__denom)

    def __float__(self):
        """
        convert the this fraction to a float
        :return:
        """
        return self.__sign * self.__num / self.__denom

    def __str__(self):
        """
        parse  this fraction to a string
        :return:
        """
        res = str(self.__num) + "/" + str(self.__denom)
        if self.__sign < 0: res = "-" + res
        return res

    def __eq__(self, other):
        if type(other) == int: other = Fraction.from_int(other)
        if type(other) == float: other = Fraction.from_float(other)
        return (self.__num == 0 and other.__num == 0) or \
               (self.__sign == other.__sign and self.__num == other.__num and self.__denom == other.__denom)

    def __add__(self, other):
        """
        fraction addition, overload the + operator
        :param other:
        :return:
        """
        if type(other) == int:
            return self + Fraction.from_int(other)
        if type(other) == float:
            return self + Fraction.from_float(other)
        new_denom = lcm(self.__denom, other.__denom)
        new_num = self.__sign * self.__num * new_denom // self.__denom + other.__sign * other.__num * new_denom // other.__denom
        return Fraction(new_denom, new_num)

    def __sub__(self, other):
        """
        fraction subtraction, overload the - operator
        :param other:
        :return:
        """
        if type(other) == int:
            return self - Fraction.from_int(other)
        if type(other) == float:
            return self - Fraction.from_float(other)
        new_denom = lcm(self.__denom, other.__denom)
        new_num = self.__sign * self.__num * new_denom // self.__denom - other.__sign * other.__num * new_denom // other.__denom
        return Fraction(new_denom, new_num)

    def __mul__(self, other):
        """
        fraction multiplication, overload the * operator
        :param other:
        :return:
        """
        if type(other) == int:
            return self * Fraction.from_int(other)
        if type(other) == float:
            return self * Fraction.from_float(other)
        new_denom = self.__denom * other.__denom
        new_num = self.__sign * self.__num * other.__sign * other.__num
        return Fraction(new_denom, new_num)

    def __floordiv__(self, other):
        """
        fraction division, return a fraction representation of the result, overload the // operator
        :param other:
        :return:
        """
        if type(other) == int:
            return self // Fraction.from_int(other)
        if type(other) == float:
            return self // Fraction.from_float(other)
        other = Fraction(other.__num, other.__denom) * other.__sign
        return self * other

    def __truediv__(self, other):
        """
        fraction division, return the float value of the result, overload the / operator
        :param other:
        :return:
        """
        if type(other) == int:
            return self / Fraction.from_int(other)
        if type(other) == float:
            return self / Fraction.from_float(other)
        other = Fraction(other.__num, other.__denom) * other.__sign
        return float(self * other)


class FractionMatrix:
    def __init__(self, matrix):
        if len(matrix) == 0:
            self.m = 0
            self.n = 0
            self.matrix = []
        elif len(matrix[0]) == 0:
            self.m = 0
            self.n = 0
            self.matrix = []
        else:
            self.m = len(matrix)
            self.n = len(matrix[0])
            self.matrix = []
            for i in range(self.m):
                self.matrix.append([])
                for j in range(self.n):
                    self.matrix[i].append(Fraction.convert(matrix[i][j]))


    @classmethod
    def zeroes(cls, row_num: int, col_num: int):
        m = []
        for ri in range(row_num):
            m.append([])
            for cj in range(col_num):
                m[ri].append(Fraction(1, 0))
        return FractionMatrix(m)

    @classmethod
    def identity(cls, dim: int):
        m = cls.zeroes(dim, dim)
        for idx in range(dim):
            li = m.matrix[idx]
            li[idx] = Fraction(1, 1)
        return m

    @classmethod
    def copy(cls, matrix: "FractionMatrix"):
        return FractionMatrix(matrix.matrix)

    @classmethod
    def from_matrix(cls, matrix: list):
        if len(matrix) == 0: return FractionMatrix(matrix)
        col_num = len(matrix[0])
        for li in matrix:
            if len(li) != col_num: raise Exception("inconsistent dimensions")
        return FractionMatrix(matrix)

    @classmethod
    def from_rows(cls, *lists: list):
        matrix = []
        for li in lists:
            matrix.append(li)
        return FractionMatrix.from_matrix(matrix)

    def __str__(self):
        res = "["
        temp = map(
            lambda li: ", ".join(
                map(lambda f: str(f), li)
            ),
            self.matrix
        )
        res += ("]\n[".join(temp) + "]")
        return res

    def __getitem__(self, idx: int):
        return self.matrix[idx]

    def remove_row(self, idx: int):
        del self.matrix[idx]
        self.m -= 1

    def remove_col(self, idx: int):
        for i in range(self.m):
            del self.matrix[i][idx]
        self.n -= 1

    def merge(self, other):
        if self.m == 0:
            self.m = other.m
            self.n = other.n
            self.matrix = other.matrix
            return self
        elif other.m == 0:
            return self
        if other.m != self.m: raise Exception("inconsistent dimensions")
        for i in range(self.m): self.matrix[i].extend(other.matrix[i])
        self.n = self.n + other.n
        return self

    def rbind(self, other):
        if self.n == 0:
            self.m = other.m
            self.n = other.n
            self.matrix = other.matrix
            return self
        elif other.n == 0:
            return self
        if other.n != self.n: raise Exception("inconsistent dimensions")
        for i in range(other.m): self.matrix.append(other.matrix[i])
        self.m = self.m + other.m
        return self

    def row_addition(self, to_idx: int, from_idx: int, scalar):
        from_row = self.matrix[from_idx]
        to_row = self.matrix[to_idx]
        for idx, val in enumerate(from_row):
            to_row[idx] = to_row[idx] + val * scalar
        return self

    def row_multiplication(self, idx: int, scalar):
        row = self.matrix[idx]
        for idx, val in enumerate(row):
            row[idx] = val * scalar
        return self

    def row_switching(self, to_idx: int, from_idx: int):
        temp_row = self.matrix[from_idx]
        self.matrix[from_idx] = self.matrix[to_idx]
        self.matrix[to_idx] = temp_row
        return self

    def transpose(self):
        new_matrix = []
        for j in range(self.n):
            new_matrix.append([])
            for i in range(self.m):
                new_matrix[j].append(self.matrix[i][j])
        self.matrix = new_matrix
        temp = self.m
        self.m = self.n
        self.n = temp
        return self

    def is_collinear(self, i: int, j: int):
        row_i = self.matrix[i]
        row_j = self.matrix[j]
        if len(row_i) == 0 and len(row_j) == 0: return True
        r = None
        for k in range(self.n):
            if float(row_j[k]) != 0:
                r = row_i[k] // row_j[k]
                break
        if r is not None:
            for k in range(self.n):
                if float(row_j[k]) == 0:
                    if float(row_i[k]) != 0: return False
                elif row_i[k] // row_j[k] != r: return False
            return True
        else:
            return True
