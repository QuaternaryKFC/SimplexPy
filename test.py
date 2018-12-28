from fraction import *
from standard_simplex import StandardSimplexSolver
from general_simplex import GeneralSimplexSolver
from revised_general_simplex import RevisedGeneralSimplexSolver
#
# A = [[5,15],[4,4],[35,20]]
# b = [480, 160, 1190]
# c = [13, 23]
#
# p = GeneralSimplexSolver([], A, [], [], b, [], c, [])
# p.solve()
# print(p)
# print("\n\n")
#
# equals_A = []
# lesses_A = [[0,3]]
# greaters_A = [[1,1],[2,-1]]
# equals_b = []
# lesses_b = [2]
# greaters_b = [1,1]
# c = [6,3]
# unrestricts = []
# maximize = False
#
# p = GeneralSimplexSolver(equals_A, lesses_A, greaters_A, equals_b, lesses_b, greaters_b, c, unrestricts, maximize)
# p.solve()
# print(p)
# print("\n\n")
#
# equals_A = []
# lesses_A = [[2, 4, 1]]
# greaters_A = [[2, 2, 3]]
# equals_b = []
# lesses_b = [6]
# greaters_b = [2]
# c = [5, -2, 1]
# unrestricts = [3]
# maximize = True
#
# p = GeneralSimplexSolver(equals_A, lesses_A, greaters_A, equals_b, lesses_b, greaters_b, c, unrestricts, maximize)
# p.solve()
# print(p)
# print("\n\n")
#
# equals_A = []
# lesses_A = [[2, 4, 1]]
# greaters_A = [[2, 2, 3], [4, 4, 6]]
# equals_b = []
# lesses_b = [6]
# greaters_b = [2, 8]
# c = [5, -2, 1]
# unrestricts = [3]
# maximize = True
#
# p = GeneralSimplexSolver(equals_A, lesses_A, greaters_A, equals_b, lesses_b, greaters_b, c, unrestricts, maximize)
# p.solve()
# print(p)
# print("\n\n")
#
# equals_A = []
# lesses_A = [[1 / 2, -11 / 2, -5 / 2, 9], [1 / 2, -3 / 2, -1 / 2, 1], [1, 1, 1, 1]]
# greaters_A = []
# equals_b = []
# lesses_b = [0, 0, 1]
# greaters_b = []
# c = [10, -57, -9, -24]
# unrestricts = []
# maximize = True
#
# p = GeneralSimplexSolver(equals_A, lesses_A, greaters_A, equals_b, lesses_b, greaters_b, c, unrestricts, maximize)
# p.solve()
# print(p)
# print("\n\n")
#
# equals_A = []
# lesses_A = [[1 / 2, -11 / 2, -5 / 2, 9], [1 / 2, -3 / 2, -1 / 2, 1], [1, 1, 1, 1], [2, 2, 2, 2]]
# greaters_A = []
# equals_b = []
# lesses_b = [0, 0, 1, 1/2]
# greaters_b = []
# c = [10, -57, -9, -24]
# unrestricts = []
# maximize = True
#
# p = GeneralSimplexSolver(equals_A, lesses_A, greaters_A, equals_b, lesses_b, greaters_b, c, unrestricts, maximize)
# p.solve()
# print(p)
# print("\n\n")

# equals_A = []
# lesses_A = []
# greaters_A = [[1, 1, 1], [0, 1, 2], [-1, 2, 2]]
# equals_b = []
# lesses_b = []
# greaters_b = [6, 8, 4]
# c = [2, 10, 8]
# unrestricts = []
# maximize = False
#
# p = GeneralSimplexSolver(equals_A, lesses_A, greaters_A, equals_b, lesses_b, greaters_b, c, unrestricts, maximize)
# p.solve()
# print(p)
# print("\n\n")


lesses_A = []
greaters_A = []
equals_A = [[0.6,0.25,0.45,0.2,0.5],[0.1,0.15,0.45,0.5,0.4],[0.3,0.6,0.1,0.3,0.1]]
lesses_b = []
greaters_b = []
equals_b = [0.4,0.35,0.25]
c = [19,17,23,21,25]
unrestricts = []
maximize = False

p = RevisedGeneralSimplexSolver(lesses_A, greaters_A, equals_A, lesses_b, greaters_b, equals_b, c, unrestricts, maximize)
p.solve()
print(p)
print("\n\n")

lesses_A = []
greaters_A = []
equals_A = [[0.6,0.25,0.45,0.2,0.5],[0.1,0.15,0.45,0.5,0.4],[0.3,0.6,0.1,0.3,0.1],[1,1,1,1,1]]
lesses_b = []
greaters_b = []
equals_b = [0.4,0.35,0.25,1]
c = [19,17,23,21,25]
unrestricts = []
maximize = False

p = RevisedGeneralSimplexSolver(lesses_A, greaters_A, equals_A, lesses_b, greaters_b, equals_b, c, unrestricts, maximize)
p.solve()
print(p)
print("\n\n")

# equals_A = [[1,0,0,Fraction(23, -17),Fraction(23, 5)],[0,1,0,Fraction(23, 16),Fraction(23, -2)],[0,0,1,Fraction(23, 24),Fraction(23, 20)]]
# lesses_A = []
# greaters_A = []
# equals_b = [Fraction(23, 1),Fraction(46, 13),Fraction(46, 31)]
# lesses_b = []
# greaters_b = []
# c = [0,0,0,Fraction(23, -18),Fraction(23, 54)]
# unrestricts = []
# maximize = False
#
# p = GeneralSimplexSolver(equals_A, lesses_A, greaters_A, equals_b, lesses_b, greaters_b, c, unrestricts, maximize)
# p.solve()
# print(p)
# print("\n\n")

# lesses_A = [[1 / 2, -11 / 2, -5 / 2, 9], [1 / 2, -3 / 2, -1 / 2, 1], [1, 1, 1, 1], [2, 2, 2, 2]]
# greaters_A = []
# equals_A = []
# lesses_b = [0, 0, 1, 5]
# greaters_b = []
# equals_b = []
# c = [10, -57, -9, -24]
# unrestricts = []
# maximize = True
#
# p = RevisedGeneralSimplexSolver(lesses_A, greaters_A, equals_A, lesses_b, greaters_b, equals_b, c, unrestricts, maximize)
# p.solve()
# print(p)
# print("\n\n")
