t = int(input())
list_n=[]
if t > 0:
    for i in range(t):
        n = int(input()) 
        list_n.append(n)
 

def digits(list_n):
    for index in list_n:
        print (*map(int, str(index)))
 
digits(list_n)