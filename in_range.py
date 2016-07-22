x = int(input("Enter starting value for range? \n "))
y = int(input("Enter ending  value for range? \n "))
c = 0
for i in range(x,y):
    if (i%5)!= 0 and (i%7)==0:
        print(str(i)+",", end='')
        c = c+1
print("\n"+ str(c))