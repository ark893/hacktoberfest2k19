n=int(input("Enter number"))
s=0; m=n
while n>=0:
    a=n%10
    s+=a**3
    n=n/10
if s==m:
    print("Armstrong number");
else:
    print("Not an armstrong number");