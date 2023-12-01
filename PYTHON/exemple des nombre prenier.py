n = int(input("donner un nombre: "))
a=1
for i in range(2,n-1):
        if n % i == 0:
            a=0
            break
if a==0:
    print(f"{n} est non premier")
else:
    print(f"{n} est premier")
    choix=input("voulez vous voir les nombre premiers avant?")
choix=input
c=0
while choix== 'oui':
    x=0
    for j in range(2+c,n+1):
        a=1
        c+=1
        for i in range(2 ,j):
            if j%i == 0:
                a = 0
                break
        if a == 1:
            print(j, end=" ")
            x += 1
        if x == 10:
            break
    if c <= n-10 :
        choix = input("afficher la suite ?")
