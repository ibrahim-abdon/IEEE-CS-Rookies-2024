def sequance(n,i=1):
    if n >1: 
        if n%2==0:
            i+=1
            return sequance(n/2,i)
        if n%2 !=0:
            i+=1
            return sequance((3*n)+1,i)
        return i
    return i
   
n =int(input())
print(sequance(n))

