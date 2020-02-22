# merge sort works on divide and conquer 
# we will divide the data into two parts and work our way up
items = [3, 2, 1, 4, 5, 2, 1, 10, 9 , 7]

def mergesort(dataset):
    if len(dataset) > 1: 
        mid = len(dataset) // 2
        leftarr = dataset[: mid];
        rightarr = dataset[mid :]

        # breaking down the arrays recursively 
        mergesort(leftarr)
        mergesort(rightarr)

        # merging them in sorted format
        i = 0
        j = 0 
        k = 0 

        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i+=1
            else: 
                dataset[k] = rightarr[j]
                j+=1 
            k+=1

        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i+=1
            k+=1
        
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j+=1
            k+=1
        
#printing the items
print(items)
mergesort(items)
print(items)