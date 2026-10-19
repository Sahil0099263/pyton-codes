n=input("Enter a variable in camelCase format:")
for i in n:
    if i.isupper():
        print("_"+i.lower(),end="")
    else:
        print(i,end="")
