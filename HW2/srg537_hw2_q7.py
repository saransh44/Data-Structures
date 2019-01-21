def findChange (lst01):
    first = 0
    last = len(lst01)-1

    while first<=last:
        midpoint = (first+last)//2
        if (lst01[midpoint-1] == 0 and lst01[midpoint]== 1):
            return midpoint

        else:
            if (lst01[midpoint] > 0):
                last=midpoint-1
            else:
                first = midpoint+1

        # print(midpoint)



print(findChange([0,0,1,1,1,1,1]))



