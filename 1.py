# n=int(input())
# b=3
# ans=""

# def str(s):
#     l=len(s)
#     for i in range(int(l/2)):
#         temp=s[i]
#         s[i]=s[l-i-1]
#         s[l-i-1]=temp

# def base(n):
#     if n>=0 and n<=9:
#         return chr(n+ord('0'))
#     else:
#         return chr(n-10+ord('A'))

# def dtb(ans,b,n):
#     j=0
#     while(n>0):
#         ans+=base(n%b)
#         n=int(n/b)
#     ans=ans[::-1]
#     return ans

# print(dtb(ans,b,n))
def dtb(num):
    if num==0:
        return
    x=num%3
    num//=3
    if (x<0):
        num+=1 
    dtb(num)
    
    if x<0:
        print(x+(3*-1),end="")
    else:
        print(x,end="")

def con(num):
    print(con(num))
    if num!=0:
        dtb(num)
    else:
        print("0",end="")
num=int(input())
