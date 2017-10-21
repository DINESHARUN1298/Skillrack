#Your code below
n=int(input())
arr=[int(x) for x in input().strip().split(" ")]
t=int(input())
z=int(n//t)
y=n%t
k=0
ans=[]
m=0
print(y)
i=0
if n<=t:
    print(max(arr))
elif n>t and y==0:
    while i<n:
        j=1
        m=0
        while j<=t:
            if arr[i]>m:
                m=arr[i]
            i+=1
            j+=1
        ans.append(m)
    for i in ans:
        print(i,end=" ")
    
else:
    while i<(n-y):
        j=1
        m=0
        while j<=t:
            if arr[i]>m:
                m=arr[i]
            i+=1
            j+=1
        ans.append(m)
    k=0
    print(ans[0])
    print(ans)
    while i<n:
        if arr[i]>ans[k]:
            ans[k]=arr[i]
        i+=1
        k+=1
        if k==len(ans):
          k=0
    for i in ans:
        print(i,end=" ")
        
            
        
    
