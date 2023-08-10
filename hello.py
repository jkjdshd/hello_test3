def reverse(start, end, arr):
 
    # No of iterations needed for reversing the list
    no_of_reverse = end-start+1
 
    # By incrementing count value swapping
    # of first and last elements is done.
    count = 0
    while((no_of_reverse)//2 != count):
        arr[start+count], arr[end-count] = arr[end-count], arr[start+count]
        count += 1
    return arr
