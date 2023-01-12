# product and sum
# find the runtime
def foo(array):
    sum = 0                                               # O(1)
    product = 1                                           # O(1)
    for i in array:                                       # O(n)
        sum += i                                          # O(1)
    for i in array:                                       # O(n)
        product *= i                                      # O(1)
    print('Sum = '+str(sum) + ',Product = '+str(product)) # O(1)
# time complexity: O(N)


# print pairs
def printPairs(array):
    for i in array:                  # O(n squared)
        for j in array:              # O(n)
            print(str(i) +","+str(j)) # O(1)
# time complexity O(n squared)
