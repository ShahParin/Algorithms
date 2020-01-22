# Name: Parin Shah
# Roll No: E029
# Experiment No.4 - Merge Sort

def mergeSort(arr,p,q):
    if len(arr) >1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        print("\nThe Sub-Arrays are: ", L, "\t", R)
        mergeSort(L,0,q)
        mergeSort(R,p,0)
        i = j = k  = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
            q+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
            p=p+1
        print("\nThe Merged array is:", arr[:j+3])
        print("Number of comparisons:", q+p)

def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

p=q=3
arr = [12, 11, 13, 5, 6, 7]
print("\nGiven array is: ")
printList(arr)
mergeSort(arr,0,0)
print("\nSorted array is: ")
printList(arr)
print("\nTotal number of comparisons are: ",p+q)