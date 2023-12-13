# def getQTh(a,b,q):
#     if(q==1):
#         return a
#     elif(q==2):
#         return b
#     else:
#         return getQTh(a,b,q-1)^getQTh(a,b,q-2)
   

# a,b,q=map(int, input().split())
# # result = getQTh(a,b,q)
# if q >=1 :
#     print(getQTh(a,b,q))
# else:
#     print('q must be equal one ore bigger')

A, B, Q = map(int, input().split())

for _ in range(Q-1):
    A, B = B, A ^ B

print(A)