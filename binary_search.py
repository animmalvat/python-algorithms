import quick_sort

# we will be searching using binary search but for that we need a sorted array 
items = [2, 4, 1, 10, 13, 5, 6, 7, 8]

quick_sort.quickSort(items, 0, len(items) - 1)

def binarySearch(item, dataset):
   
    # finding middle point
    middle = (len(dataset) - 1) // 2
    print(middle)

    if item == dataset[middle]:
        return middle
    elif item > dataset[middle]:
        return binarySearch(item, dataset[middle:])
    elif item < dataset[middle]:
        return binarySearch(item, dataset[:middle])
    