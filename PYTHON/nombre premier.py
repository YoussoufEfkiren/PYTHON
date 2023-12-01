k = int(input("donner un nombre: "))
if k > 1:
    for i in range(2, int(k / 2) + 1):
        if (k % i) == 0:
            print("pas un nombre premier")
            break
    else:
        print("est un nombre premier")
else:
    print("pas un nombre premier")
