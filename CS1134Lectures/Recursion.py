def count_up_and_down(start, end):
    if (start == end):
        print(start)

    else:
        print(start)
        count_up_and_down(start+1, end)
        print(start)


def factorial(n):
    if (n==1):
        return 1
    else:
        return n * factorial(n-1)

def sum_list (lst):
    if (len(lst) == 1):
        return lst[0]
    else:
        rest = sum_list(lst[1: ])
        return (lst[0] + rest)

# return x^n
def power (x, n):
    if n == 1:
        return x
    else:
        rest = power(x,n-1)
        return x + rest

count_up_and_down(1,5)
print(factorial(4))
print(sum_list([0,1,2,3,4,5]))
print(power(2,4))

