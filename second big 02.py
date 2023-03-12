# Question 4 print undored pairs2 arrays
def printUnorderedPairs(arrayA, arrayB):
    for i in range(0,len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i]  < arrayB[j]: # O(1)
                print(str(arrayA[i]) + "," +str(arrayB[j]))

# b = len(arrayB)
# a = len(arrayA)
# time complexity: O(ab)

# question 5
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)): #O(ab)
        for j in range(len(arrayB)):#O(ab)
            for k in range(0,100000):#O(1)
                print(str(arrayA[i] + ","+ str(arrayB[j])))#0(1)
# a = len(arrayA)
# b = len(arrayB)
# 100 000 units work is still constant O(1)
#time complexity: O(ab)

# question 6 Reverse
def reverse(array):
    for i in range(0, int(len(array)/2)):#O(N/2) = O(N)
        other = len(array)-i-1# O(1)
        temp = array[i]#0(1)
        array[i] = array[other]#O(1)
        array[other] = temp#O(1)
    print(array)# O(1)
#time complexity: O(N)
# question 7  Equivalents
# which of the following are equivalent to O(N)? Why
# 1. O(N+P) where P<N/2 N is dominant so you drop P to get O(N)
# 2.0(2N) drop the constant to to get O(N)
# 3.O(N+logN) O(N) is dominant tha O(logN) so you drop logN to get O(N)
# 4.O(N+NlogN) O(NlogN) is more dominant than O(N) so this not equavalent to O(N)
# 5.O(N+M) the is no established relationship between N and M so we keep both variables which is not equavelnt to O(N)

#question 8 factorial complexity
def factorial(n):#M(N)
    if n<0:
        return -1 # O(1)
    elif n == 0:
        return 1 # O(1)
    else:
        return n * factorial(n-1) # M(n-1)

# # M(n) = O(1)+M(n-1)
# M(0) =O(1)
# M(n-1)= O(1)+M((n-1)-1)
# M(n-2)= O(1)+M((n-2)-1)
#
# M(n)=1+M(n-1)
# =1+(1+M((n-1)-1))
# =2+M(n-2)
# =2+1+M((n-2)-1)
# =3+M(n-3)
# =a+M(n-a)
# =n+M(n-n)
# =n+1
# =n this is the time complexity

