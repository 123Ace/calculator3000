a = int(input("vvedite pervoe chislo: "))
b = int(input("vvedite vtoroe chislo: "))
c = input("vvedite znak operacii: ")
if c in ('+', '-', '*', '/'):
    if c == '+':
        print(a+b)
    elif c == '-':
        print(a-b)
    elif c == '*':
        print(a*b)
    elif c == '/':
        if b!=0:
            print("%.2f"%(a/b))
        else:
            print ("delenie na null")
else:
    print ("nepravilniy znak!")