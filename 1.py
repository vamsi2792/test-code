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
