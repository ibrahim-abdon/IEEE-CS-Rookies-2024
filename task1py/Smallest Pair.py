def find_smallest_result(n,list_numbers):
    result =None
    small_result =None
    i=1
    while i< n:
        j =i+1
        while j <=n:
            a1=list_numbers[i-1]
            a2=list_numbers[j-1]
            result = a1+a2+j-i
            if small_result == None or result <small_result :
                small_result = result
            j += 1
        i += 1
    return small_result

    
input_value = int(input())

for i in range(input_value):
    n = int(input())
    list_numbers = list(map(int, input().split()))
    result = find_smallest_result(n, list_numbers)
    print(result)

