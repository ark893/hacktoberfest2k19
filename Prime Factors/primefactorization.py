n=int(input("Enter an integer:"))
i=1;
c=0
while i <=n:
    j=1
    f=0
    if n%i == 0:
        while j<=i:
            if i%j == 0:
                f+=1
            j+=1
        if f == 2:
            c+=1
        i+=1
print (c)
