def min_max (list_numbers,n):
    minIndex=0
    maxIndex=0
    i=0
    while i<len(list_numbers):
        if list_numbers[i]<list_numbers[minIndex]:
            minIndex = i
        if (list_numbers[i]>list_numbers[maxIndex]):
            maxIndex=i
        i += 1
    maxValue = list_numbers[maxIndex]
    minVale = list_numbers[minIndex]
    if maxIndex !=-1 and minIndex != -1 :
        list_numbers[maxIndex]=minVale
        list_numbers[minIndex]=maxValue
    return list_numbers

n= int(input())
list_numbers=list(map(int, input().split()))

resut =min_max(list_numbers,n)
print(*resut)


# I mean to do this without min and max functions