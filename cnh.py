idade=int(input("me diga sua idade: "))
cnh = input("c e o toque da nave: ").capitalize()

if idade>=18 and cnh == "Sim":
        print("e de maior e pode dirigir")
elif idade>=18 and cnh == "Nao" :
        print("de maior mas e frango na pilota")
else:
    print("c e junin")
