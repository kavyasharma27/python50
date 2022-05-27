def perfect(num):
    s=0
    for i in range(1,num):
        if num%i==0:
            s+=i
    if s==num:
        print(f'{num} is a perfect no')   
    else:
        print(f'{num} is a not a perfect no.')
a=int(input("enter:"))
perfect(a)


