# -*- coding: cp936 -*-
#第8章的习题
from time import *
def f_t_i(f,t,i):
    'Loop f to t'
   # '循环，用循环方式打印出f到t的数字，步长为i'
    n=f
    while n<t:
        print n,
        n=n+i
    
def isprime(n):
    #判断一个数是否为素数
    i=0
    if n==2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
            break
        if i>n/2:
            return True
def getfactors(n):
    #求一个整数的所有约数
    a=[]
    i=0
    for i in range(1,n+1):
        if n % i == 0:
            a.append(i)
    return a
def getprime(n):
    #求小于某一个数的所有素数集合
    i=2
    a=[]
    if n<2:
       print 'the int number must be great than 2 '
    if n==2:
        a=[2]
    for i in range(2,n):
        if isprime(i):
            a.append(i)
    return a
        
def getprime_factors(n):
    #求素因子分解
    a=getfactors(n)
    b=[]    #素因子序列
    c=[]    #返回值
    i=0
    j=0
    k=1    
    for i in range(len(a)):
        b=[]
        if isprime(a[i]):
            k=a[i]
            b.append(a[i])
            for j in range(i,len(a)):
                if isprime(a[j]):
                    b.append(a[j])
                    k=k*a[j]
                    if k==n:
                        c.append(b)
                        break
                    if k>=n:
                        break
    return c
def isperfect(n):
    #判定一个数是否是全数
    a=[]
    b=0
    i=0
    a=getfactors(n)
    for i in range(len(a)-1):
        b=b+a[i]
    if b==n:
        return True
    else:
        return False
def getfactorial(n):
    #求阶乘
    a=1
    i=1
    for i in range(1,n+1):
        a=a*i
    return a

def getFibonacci(n):
    a=1
    b=0
    c=0
    star_time=time()
    for i in range(n):
        now_time=time()
        if now_time-star_time>=2:
            ss=raw_input( '计算任务量太大，需要时间太长,结束请按0,继续请输入任意键：')
            if ss=='0':
                return 0
                break
            else:
                star_time=time()
        c=a+b
        a=b
        b=c
    return c
def get_numTypeAll(a,b):
    print 'Enter begin value:%i'%a
    print 'Enter end value:%i'%b
    print 'DEC%sBIN%sOCT%sHEX%sASCII%s' %(' '*7,' '*7,' '*7,' '*7,' '*5)
    for i in range(a,b+1):
        print str(i)+'%s' %(' '*(9-len(str(i)))),
        print str(bin(i))+'%s' %(' '*(9-len(str(i)))),
        print str(oct(i))+'%s' %(' '*(9-len(str(i)))),
        print str(hex(i))+'%s' %(' '*(9-len(str(i)))),
        print str(chr(i))+'%s' %(' '*(9-len(str(i))))
        



          
            
        
        

        

                    

                    
                        
                        
