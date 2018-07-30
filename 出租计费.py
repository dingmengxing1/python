var=1
while var == 1:
    n=int(raw_input())
    if n<=0:
        print '请输入正确的公里数进行计算'
        exit(0)
    elif n<=2 and n>0:
        s=8
        print s
    elif n>2 and n<=12:
        s=8+(n-2)*1.2
        print s
    elif n>12:
        s=20+(n-12)*1.5
        print s
