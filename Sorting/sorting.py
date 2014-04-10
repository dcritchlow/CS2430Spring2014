def quickSort(myList):
    # print myList
    lowerList = []
    pivotList = []
    higherList = []

    if len(myList) <= 1:
        return myList
    else:
        pivotNumber = myList[0]
        for i in myList:
            if i < pivotNumber:
                lowerList.append(i)
            elif i > pivotNumber:
                higherList.append(i)
            else:
                pivotList.append(i)
        # print lowerList + pivotList + higherList
        lowerList = quickSort(lowerList)
        higherList = quickSort(higherList)
    return lowerList + pivotList + higherList

def bubbleSort(myList):
    # print myList
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(myList)-1):
            if myList[i] > myList[i+1]:
                myList[i], myList[i+1] = myList[i+1], myList[i]
                swapped = True
    return myList

def mySort(myList):
    b = list()
    while myList != sorted and len(myList) > 0:
        for i in myList:
            minimum = min(myList)
            index = myList.index(minimum)
            b.append(minimum)
            myList.pop(index)
    return b

if __name__ == '__main__':
    import timeit
    import random

    unsortedList = random.sample(range(1,10001), 1000)
    print 'Unsorted List: \n', unsortedList

    t1 = timeit.Timer('a = unsortedList[:]; quickSort(a)','from __main__ import quickSort, unsortedList')
    t2 = timeit.Timer('a = unsortedList[:]; bubbleSort(a)','from __main__ import bubbleSort, unsortedList')
    t3 = timeit.Timer('a = unsortedList[:]; mySort(a)','from __main__ import mySort, unsortedList')

    print '\nQuick Sort time: ', min(t1.repeat(7,10))
    print '\nBubble Sort time: ', min(t2.repeat(7,10))
    print '\nMy Sort time: ', min(t3.repeat(7,10))

    print "\nI'm sorted now: \n", quickSort(unsortedList)
