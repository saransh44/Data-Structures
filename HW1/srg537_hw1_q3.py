# Question3A
# def sum_squares (n):
#     list = [a**2 for a in range(n)]
#     print(list)
#     total = sum(list)
#     print(total)
#
# sum_squares (5)



# Question3B
print(sum([a ** 2 for a in range(6)]))


def sum_squares (n):
    return (sum([a**2 for a in range(n)]))
# print(sum_squares (6))





# Question3C & Question3D
print(sum([a ** 2 for a in range(7) if a % 2 == 1]))


def sum_odd_squares (n):
    return (sum([a**2 for a in range(n) if a % 2 == 1] ))


# print(sum_odd_squares (7))