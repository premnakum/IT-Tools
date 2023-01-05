bubble_sort(array)
for j in range (0,len(array),-1):
    for i in range (len(array),-1):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
            return(array):
            array=(2,11,0,-1,-9)
            print("The unsorted list is ",array)
            print("The sorted list is ",buuble_sort(array))
            