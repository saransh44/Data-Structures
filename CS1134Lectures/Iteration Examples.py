def f():
    x=1
    yield x

    x +=1
    yield x

    x +=1
    yield x

def my_range(start, stop, step):
    curr = start
    while (curr < stop):
        yield curr
        curr += step

G = f()
type(G)

# /*allows to produce an implcit sequence*/
# //no data structure that stores the entire sequence all at once
# //It isnt evaluted all up front but breaks the execution
# to stops that are triggered on demand

def prime (num):
    com_dividers=0
    for curr in range (1, num+1):
        if (num % curr == 0)
        com_dividers += 1
        if(com_dividers == 2):
            return True
        else
            return False

    def is.prime2(num)

    def is_prime2(num):
        count_divisors = 0;
        for curr in range(1, num//2+1):
            if(num%curr == 0)
                count_divisors += 1
        if(count_divisors == 1)
            return True
        else
            return False