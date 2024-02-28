#Guess Number Game
#code test
nam = input("Name: ")
ln = len(nam)
print(nam[ln-2])



a = 1
b = 2
print(a, b)

big =max("michael")
print(big)
small = min("michael")
print(small)

smallest = None
for num in [651, -5, 46, -46, 48, 94, -4] :
    if smallest is None:
        smallest = num

    elif num < smallest:
        smallest = num
print("The smallest number is ", smallest)
