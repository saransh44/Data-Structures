# import copy
# Question4A
# print([10**a for a in range(6)])
# # print([c for c in range(10) if c > 1])
#
# # Question4B
# print([a*b for a,b in zip([c for c in range(11) if c > 0],[d for d in range(10)])])
# # list = [range(11) * c for c in [1, 2, 3, 4, 5, 6, 7, 8, 9]]
# list = [[1,2,4] * [3, 4],6]
# print (list)
#
# # Question4C
# print([chr(a) for a in range(123) if a > 96])

print([10**i for i in range(6)])

print([a * b for a,b in zip([c for c in range(1,11)], [d for d in range(10)])])

# print([chr(c) for c in range(97,123)])

lst1 = [1,2,3]
lst2 = [lst1 for i in range(3)]
lst3 = lst1.copy()
print(lst2[0][0])
# lst2[0][0] = 10
print(lst2)
lst3[0] = 10
print(lst1)
