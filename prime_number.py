# Print all prime number between 1 to 100
for i in range(2,101):
    a=True
    for a in range(2,int(i**0.50)+1):
        if i%a==0:
            a=False
            break
    if a:
        print(i,end=" ")