def knapsack(items, max_number, n):
    if n == 0 or max_number == 0:
        return 0
    
    if items[n - 1][0] > max_number:
        return knapsack(items, max_number, n - 1)

    return max(
                 items[n - 1][1] + 
                knapsack(items, max_number - items[n - 1][0], n - 1),
               knapsack(items, max_number, n - 1)
               )



n, w = map(int, input().split())
items = [list(map(int, input().split())) for index in range(n)]

result = knapsack(items, w, n)
print(result)
