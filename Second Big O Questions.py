# what is the runtime of the code below
def foo(array):
    sum = 0     # O(1)
    product = 1    # o(1)

    for i in array:  # O(n)
        sum += i  # O(1)
    for i in array: # 0(n)
        product *= i # (1)
    print("Sum = " +str(sum)+", Product = "+str(product)) # O(1) final is O(n)


#Question 2 print pairs
def printPairs(array):
    for i in array:#O(N^2)
        for j in array:#O(N)
            print(str(i)+","+str(j))#O(1) final is O(n^2)

# Question 3 print unordered pairs
def printUnorderedPairs(array):
    for i in range(0,len(array)):
        for j in range(i+1, len(array)):
            print(array[i] + "," + array[j]) # O(n^2)

# Question 4 print undored pairs2 arrays
def printUnorderedPairs(arrayA, arrayB):
    for i in range(0,len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i]  < arrayB[j]:
                print(str(arrayA[i]) + "," +str(arrayB[j]))