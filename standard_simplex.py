from fraction import *


class StandardSimplexSolver:
    def __init__(self, A, b, c):
        self.__m = len(b)
        self.__n = len(c)
        self.__a = FractionMatrix.from_matrix(A)
        self.__a.merge(FractionMatrix.identity(self.__m))
        self.__a.merge(FractionMatrix.from_rows(b).transpose())
        self.__a.rbind(FractionMatrix.from_rows(c).merge(FractionMatrix.zeroes(1, self.__m + 1)))

    def __bland(self):
        for q in range(self.__m + self.__n):
            if float(self.__a[-1][q]) > 0: return q
        return -1

    def __min_ratio_rule(self, q: int):
        p = -1
        for i in range(self.__m):
            if float(self.__a[i][q]) <= 0:
                continue
            elif p == -1:
                p = i
            elif self.__a[i][self.__m + self.__n] / self.__a[i][q] < self.__a[p][self.__m + self.__n] / self.__a[p][q]:
                p = i
        return p

    def __pivot(self, p: int, q: int):
        for i in range(self.__m + 1):
            if i != p: self.__a.row_addition(i, p, self.__a[i][q] // self.__a[p][q] * -1)
        self.__a.row_multiplication(p, self.__a[p][q].inverse())

    def solve(self):
        while True:
            q = self.__bland()
            if q == -1: break

            p = self.__min_ratio_rule(q)
            if p == -1: raise Exception("unbounded problem")

            self.__pivot(p, q)

    def __str__(self):
        return str(self.__a)
