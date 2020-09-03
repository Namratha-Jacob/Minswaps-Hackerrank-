def swap(p,i,arr):
    temp1 = arr.index(p)
    temp2 = arr.index(i)
    temp3 = arr[temp1]
    arr[temp1] = arr[temp2]
    arr[temp2] = temp3
    

def minimumSwaps(arr):
    count = 0
    arr = [p-1 for p in arr]
    for p,i in enumerate(arr):
        if p != i:
            swap(p,i,arr)
            print("after swapping ", i, " and ",p,": ",arr)
            count += 1
    return count
    
 if __name__ == '__main__':

    n = int(input())

    arr = list(map(int,input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)
