#searching an item through an unsorted array 
items = [1, 3, 4, 5, 8, 9, 0, 6, 7, 22]

def find_item(item, itemlist):
    for i in range(0, len(itemlist)):
        if item == itemlist[i]:
            return i
    return -1

temp = find_item(8, items)
if temp != -1:
    print(temp)
