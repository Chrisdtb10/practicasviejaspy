global vida
vida=100

def alimentar():
    print("alimentando al robot +20")
    global vida
    vida=vida+20
def pegar():
    print("pegandole al robot -10")
    global vida
    vida = vida -10
def golpemortal():
    print("dandole un golpe mortal -90")
    global vida
    vida = vida -90
def matar():
    print("matando al robot kill")
    global vida
    vida = 0
def revivir():
    print("reviviendo")
    global vida
    vida = 100
def principal():
    print("="*100)
    print("ROBOT 2.0 ")
    print("=" * 100)
    while(True):
        print("MENU DE OPCIONES \n")
        print("VIDA",vida)
        print("1.-Alimentar")
        print("2.-Pegar")
        print("3.-Golpe Mortal")
        print("4.-Matar")
        print("5.-Revivir")
        print("6.-Salir")
        op = input("ingrese numero de opcion: ")
        if op=="1":
            alimentar()
        elif op=="2":
            pegar()
        elif op=="3":
            golpemortal()
        elif op=="4":
            matar()
        elif op=="5":
            revivir()
        elif op=="6":
            print("gracias por crear el robot")
            break
principal()



