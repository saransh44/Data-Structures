def fibs(n):
    total = 0
    b = 1
    a = 0
    counter = 0
    while (counter < n):
        if counter < n:
            a = b
            b = total
            total = a + b
            # lst.append(total)

            yield total
        counter += 1

    # if n < 2:
        #     yield n
        #
        # # yield n
        # total = [a + b for a, b in zip([c for c in fibs(n-2)], [z for z in fibs(n-1)])]
        # yield total

for curr in fibs(8):
     print(curr)
# print(fibs(8))