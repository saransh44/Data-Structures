def factors(n):
    k=1
    lst = []
    while k * k <= n:
        if n % k == 0:
            lst.append(k)
            # if (lst[k - 1] > lst[k]):
            #     lst[k-1], lst[k] = lst[k], lst[k-1]
        k += 1
    # if k * k == n:
    #     lst.append(k)

    for i in range(len(lst)-1,-1,-1):
        lst.append(n//lst[i])


    return lst

for curr_factor in factors(100):
    print(curr_factor, end=" ")
