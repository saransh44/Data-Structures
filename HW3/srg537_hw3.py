# 3A
def print_triangle (n):
    if (n == 1):
        print("*")
    else:
        print_triangle(n-1)
        for i in range(n):
            print("*", end= " ")
        print()

# 3B
def print_oposite_triangles(n):
    if (n == 0):
        None
    else:
        for i in range(n):
            print("*", end= " ")
        print()
        print_oposite_triangles(n-1)
        for i in range(n):
            print("*", end= " ")
        print()

# 4
def lst_min(lst, low, high):
    # return lst[low:high+1]
    initial=0
    i = 1
    if (low == high or len(lst) == 1):
        print(lst[low])
    else:
        lst = lst[low:high+1]
        print(lst)
        if (lst[initial] > lst[i]):
            initial = i
            lst_min(lst, initial, high)
        else:
            lst.pop(i)
            lst_min(lst, initial, high-1)

# 5A
def count_lowercase(s, low, high):
    if (low == high):
        if (s.islower()):
            return 1
        else:
            return 0
    else:
        temp = s[low:low+1]
        if (temp.islower()):
            return 1 + count_lowercase(s, low + 1, high)
        else:
            return count_lowercase(s, low + 1, high)


# print(count_lowercase("strIng", 0, 3))

# 5B
def count_number_of_lowercase_even(s, low, high):
    slist = list(s)
    i = 0
    total = 0
    if (ord(slist[high]) < 50):
        while i < len(slist):
            print(slist[i])
            if (ord(slist[i]) == 49):
                total += 1
            i += 1
        if (total > 0 and total % 2 == 0):
            return True
        else:
            return False
    else:
        # print(slist[low], ord((slist[low])))
        if (ord(slist[low]) > 64 and ord(slist[low]) < 91):
            slist[low] = '0'
            return count_number_of_lowercase_even(slist, low+1, high)
        elif (ord(slist[low]) > 96 and ord(slist[low]) < 123):
            slist[low] = '1'
            return count_number_of_lowercase_even(slist, low+1, high)
        else:
            slist[low] = '51'


print(count_number_of_lowercase_even("A", 0, 0))

# 6
def appearances(s, low, high):
    a = dict()
    if (low == high):
        if a.get(s[low]) == None:
            d1 = {s[high]: 1}
            return d1
        else:
            d1 = {s[high]: a.get(s[low])+1}
            return d1

    else:
        a = appearances(s,low+1,high)
        if s[low] in a:
            a[s[low]] += 1
            return a
        else:
            d1 = {s[low]:1}
            a.update(d1)
            return a

print(appearances("dssaa5f",0,4))

# 7
def flat_list(nested_lst, low, high):
    if low > high:
        return []
    if isinstance(nested_lst[low], list):
        return flat_list(nested_lst[low], 0, len(nested_lst[low])-1) + flat_list(nested_lst, low+1, high)
    else:
        a = [nested_lst[low]]
        if (len(a) > 1):
            return a[0] + flat_list(a[1:len(a)], 0, len(a))
        else:
            return a + flat_list(nested_lst, low+1, high)


n = [0, [1,[2]], 3, [4, [5, 6, 7, 8]]]
print(flat_list(n, 0, 3))
