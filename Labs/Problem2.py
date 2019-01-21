def reverse_vovels(input_str):
    lst = list(input_str)
    count = 0
    lstV = []
    lstP = []
    i = 0
    for char in input_str:
        if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
            lstV.append(char)
            lstP.append(count)
        count+=1

    lstV.reverse()
    max = len(lstV)
    while (i < max):
        # del lst[lstP[i], (lstP[i] + 1)]
        pos = lstP[i]
        lst.__setitem__(lstP[i], lstV[i])
        i += 1

    print(lst)


reverse_vovels("ideal")