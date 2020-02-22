# this is simple implementation of quick sort
items = [11, 3, 2, 5, 10, 8 , 7 , 9]

def quickSort(dataset, first, last):
    if first < last: 
        # calculate the split point
        pivotIdx = partition(dataset, first, last)

        # sorting the two partitions 
        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)

def partition(datavalues, first, last):
    # choosing first value for pivot
    pivotvalue = datavalues[first]

    # establish the upper and lower indexes 
    lower = first +  1
    upper = last 

    # start searching for the crossing point
    done = False
    while not done: 
        # advance the lower index
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower+=1

        # advance the upper index
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper-=1
        
        # if indexes cross, we have found the split point
        if upper < lower:
            done = True
        else: 
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp
        
    # split point is found, so, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    return upper
    
quickSort(items, 0, len(items) - 1)
print(items)