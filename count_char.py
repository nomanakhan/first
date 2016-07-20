x = input("Any stream for counting of letters, digits , space and others? \n ")
letters=0
digit=0
space=0
other=0
for char in x:
        if char.isalpha():
            letters += 1
        elif char.isnumeric():
            digit += 1
        elif char.isspace():
            space += 1
        else:
            other += 1
print("Letters = "+str(letters))
print("Digits = "+str(digit))
print("Space = "+str(space))
print("other = "+str(other))