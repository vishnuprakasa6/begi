
h=int(input())
k=list(map(int,input().split()))
y=0
for i in range(len(k)-2):
    for a in range(i+1,len(s)-1):
         for j in range(a+1,len(k)):
            if k[i]<k[x]<k[j] and i<a<j:
                y+=1
print(y)    
