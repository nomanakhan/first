#
x = int(input ("Rows"))
y = int(input ("Col"))

# x=3
# y=5
a = []
for i in range (0,x):
    a.append([])
    print(a)
    for j in range (0,y):
        a[i].append(i*j)
print(a)