# bubble sort algorithm 
# it is the simplest form of sorting methods
def bubble_sort(data):
    for i in range(len(data) - 1, 0, -1):
        for j in range(0, i):
            if(data[j] > data[j+1]):
                # swap
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
            else: 
                pass
                #nothing to do here
    return data
print(bubble_sort([1, 3, 4, 2]))
