# Bubblesort
from random import randint
length = 100

# create list of random ints
unsorted = []
for i in range(length):
    unsorted.append(randint(0,1000))
sortedlst = []
print (unsorted)
print (len(unsorted))

def bubblesort(lst):  
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            tmp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = tmp
#for i in range(100):
bubblesort(unsorted)
print (unsorted)
