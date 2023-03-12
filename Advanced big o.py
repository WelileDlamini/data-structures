# fibbonanci complexity
def allFib(n):
    for i in range(n):
        print(str(i)+","+ str(fib(i)))

def fib(n):
    if n<=0:
        return 0 # branches^depth 0(2^n)
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)
# time complexity = O(2^n)

# Question 10 Powers of 2
def powersOf2(n):
    if n<1:
        return 0
    elif n == 1:
        print(1) # this part is O(1)
        return 1
    else:
        prev = powersOf2(int(n/2))
        curr = prev*2 # this part is O(1)
        print(curr)
        return curr
# if we can halve n until we get 1 the time complexity of this will be LogN


