N1 = float(input("donner le nombre:"))
N2 = float(input("donner une autre nombre:"))
oper = input("donner l'operation:")
if oper=="+":
    print("la somme est:",N1+N2)
elif oper=="-":
    print("la moin est",N1-N2)
elif oper=="*":
    print("multiplication est:",N1*N2)
elif oper=="/":
    if N2==0:
        print("go home")
    else:
        print("le div est:",N1/N2)


