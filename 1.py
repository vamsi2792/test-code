n=int(input())
b=3
ans=""

def str(s):
    l=len(s)
    for i in range(int(l/2)):
        temp=s[i]
        s[i]=s[l-i-1]
        s[l-i-1]=temp

def base(n):
    if n>=0 and n<=9:
        return chr(n+ord('0'))
    else:
        return chr(n-10+ord('A'))

def dtb(ans,b,n):
    j=0
    while(n>0):
        ans+=base(n%b)
        n=int(n/b)
    ans=ans[::-1]
    return ans

print(dtb(ans,b,n))
