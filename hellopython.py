def fact(n):
    if n<=0:
        print('ValeError')
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n = 5
mult=fact(n)
print('% 的阶乘是%',n,mult)
    
