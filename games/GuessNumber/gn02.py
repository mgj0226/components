#def


#start
n = input("First Name: ")
sm = input("Sur Name: ")
while True:
    try:
        rn = int(input("A Random Number: "))
    except:
        print("Number only")
        print("Please try again")
        continue
    break

ans = len(n) + len(sm) + rn

# narrow down
if ans <= 0:
    ans = ans * -1 + 1
while True:
    if ans <= 100:
        ans = int(ans)
        break
    elif ans > 100:
        ans = ans / 10
        continue

#test
print(ans)

#Guess
cn = 5
while True:
        try:
            gn = float(input("Guess a number(1-100): "))
        except:
            print("Number only")
            print("Please try again")
            continue
        break

while gn > ans:
    print("smaller, Chance: ", cn)
    cn = cn -1
    while True:
        if cn == 0:
            print("Game Over")
            break
        try:
            gn = float(input("Guess a number(1-100): "))
        except:
            print("Number only")
            print("Please try again")
            continue
        break

while gn < ans:
    print("bigger, Chance: ", cn)
    cn = cn - 1
    while True:
        if cn == 0:
            print("Game Over")
        try:
            gn = float(input("Guess a number(1-100): "))
        except:
            print("Number only")
            print("Please try again")
            continue
        break

if gn == ans:
    print("Jackpot!")
#print("Finish")
