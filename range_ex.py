c = 0
for i in range(2000,3201):
    if (i%5)!= 0 and (i%7)==0:
        print(str(i)+",", end='')
        c = c+1
print(c)
