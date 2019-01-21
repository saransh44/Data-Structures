# test[15] = 0
# test[30] = 54
#
# del test[2]
# test[9] = 50
# test[14] = 99
#
# print()
# for i in test:
#     print(i)
# for i in test:
#     print(i)

# lst = [12, 56, 22, 106, 36, 72, 902, 86, 96, 62, 42]
lst = [59, 39, 135, 91, 46, 132, 169, 277, 157]
result = []
result2 = []
for i in lst:
    # print(i)
    result.append((((125*i+342)%1009)%10))
    result2.append((i%11))
print(result2)

print(5//2)