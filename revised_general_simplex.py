from fraction import *


class RevisedGeneralSimplexSolver:
    def __init__(self, lesses_A: list, greaters_A: list, equals_A: list,
                 lesses_b: list, greaters_b: list, equals_b: list,
                 c: list, unrestricts: list, maximize=True):
        self.remove_redundant(lesses_A, lesses_b, True)
        self.remove_redundant(greaters_A, greaters_b, False)
        self.__has_phase_one = False
        self.__len_artificials = len(greaters_b) + len(equals_b)
        if self.__len_artificials > 0: self.__has_phase_one = True
        self.__m = len(lesses_b) + len(greaters_b) * 2 + len(equals_b)
        self.__n = len(c) + len(unrestricts)
        self.__a = []
        self.combine_As(lesses_A, greaters_A, equals_A)
        self.add_complimentaries_for_unrestricts(c, unrestricts)
        self.__a = FractionMatrix.from_matrix(self.__a)
        self.add_slacks_and_artificials(len(lesses_b), len(greaters_b), len(equals_b))
        self.merge_bs(lesses_b, greaters_b, equals_b)
        self.__a.rbind(
            FractionMatrix.from_rows(c).merge(FractionMatrix.zeroes(1, self.__m + 1))
        )
        if not maximize: self.__a.row_multiplication(-1, -1)
        if self.__has_phase_one: self.construct_phase_one(len(greaters_b), len(equals_b))

    def combine_As(self, *As):
        for A in As:
            self.__a.extend(A)

    def add_complimentaries_for_unrestricts(self, c, unrestricts: list):
        for i in range(len(self.__a)):
            for k in unrestricts:
                self.__a[i].append(self.__a[i][k - 1] * -1)
        for k in unrestricts:
            c.append(-c[k - 1])

    def add_slacks_and_artificials(self, len_lesses: int, len_greaters: int, len_equals: int):
        slacks = FractionMatrix.identity(len_lesses + len_greaters)
        for i in range(len_greaters):
            k = len_lesses + i
            slacks[k][k] = slacks[k][k] * -1
        artificials = FractionMatrix.identity(len_greaters + len_equals)
        artificials = FractionMatrix.zeroes(len_lesses, len_greaters + len_equals).rbind(artificials)
        self.__a.merge(slacks.rbind(FractionMatrix.zeroes(len_equals, len_lesses + len_greaters)).merge(artificials))

    def merge_bs(self, *bs):
        B = []
        for b in bs:
            B.extend(b)
        B = FractionMatrix.from_rows(B)
        self.__a.merge(B.transpose())

    def remove_redundant(self, A: list, b: list, lesses=True):
        a = FractionMatrix.from_matrix(A)
        for i in range(len(b)):
            for j in range(i + 1, len(b)):
                if a.is_collinear(i, j):
                    q = 0
                    for k in range(a.n):
                        if float(a[i][k]) != 0:
                            q = k
                            break
                    if (Fraction.convert(b[i]) / a[i][q] > Fraction.convert(b[j]) / a[j][q]) == lesses:
                        del A[i]
                        del b[i]
                    else:
                        del A[j]
                        del b[j]

    def construct_phase_one(self, len_greaters: int, len_equals: int):
        artificials_sum = [0] * self.__a.n
        for i in range(len_greaters + len_equals):
            artificials_sum[self.__n + self.__m - len_greaters - len_equals + i] = -1
        self.__a.rbind(FractionMatrix.from_rows(artificials_sum))
        for i in range(len_greaters + len_equals):
            self.__a.row_addition(-1, -(len_greaters + len_equals) + i - 2, 1)

    def __bland(self):
        for q in range(self.__m + self.__n):
            if float(self.__a[-1][q]) > 0: return q
        return -1

    def __min_ratio_rule(self, q: int):
        p = -1
        M = self.__a.m
        if self.__has_phase_one: M -= 1
        for i in range(M - 1):
            if float(self.__a[i][q]) <= 0:
                continue
            elif p == -1:
                p = i
            elif self.__a[i][self.__m + self.__n] / self.__a[i][q] < \
                    self.__a[p][self.__m + self.__n] / self.__a[p][q]:
                p = i
        return p

    def __pivot(self, p: int, q: int):
        for i in range(self.__a.m):
            if i != p: self.__a.row_addition(i, p, self.__a[i][q] // self.__a[p][q] * -1)
        self.__a.row_multiplication(p, self.__a[p][q].inverse())

    def __solve(self):
        while True:
            q = self.__bland()
            if q == -1: break

            p = self.__min_ratio_rule(q)
            if p == -1: raise Exception("unbounded problem")

            self.__pivot(p, q)

    def solve(self):
        if self.__has_phase_one:
            self.__solve()
            if math.floor(float(self.__a[-1][-1]) * 10000) != 0: raise Exception("infeasible problem")
            self.__a.remove_row(-1)
            for i in range(self.__len_artificials): self.__a.remove_col(-2)
            self.__m -= self.__len_artificials
            self.__has_phase_one = False
        self.__solve()

    def __str__(self):
        return str(self.__a)
