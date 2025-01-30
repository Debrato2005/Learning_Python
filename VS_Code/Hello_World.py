y=1
while y>0:
    x=int(input('enter number:'))
    while x>1:
        print(x,end=' ')
        if x%2==0:
            x=x//2
        else:
            x=(x*3)+1
        if x==0:
            y=0
        if x==1:
            print('1')
            continue
    print()