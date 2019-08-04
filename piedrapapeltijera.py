from time import sleep
import random


def mayor(opcionMIA,opcionCPU):
    print("El Cpu esta eligiendo......> ")
    for i in range(0,5):
        print(5-i),sleep(1)
    print("El cpu ha elegido",opcionCPU)
    if opcionMIA=="piedra" and opcionCPU=="piedra":
        return "queda en empate"
    elif opcionMIA=="papel"and opcionCPU=="piedra":
        elmayor=opcionMIA
        return "has ganado con %s" %elmayor
    elif opcionMIA == "tijera" and opcionCPU == "piedra":
        elmayor = opcionCPU
        return "ha ganado el CPU con %s" %elmayor
    if opcionMIA =="piedra" and opcionCPU=="papel":
        elmayor=opcionCPU
        return "gana el CPU con %s" %elmayor
    elif opcionMIA=="papel"and opcionCPU=="papel":
        return "queda en empate"
    elif opcionMIA == "tijera" and opcionCPU == "papel":
        elmayor = opcionMIA
        return "has ganado con %s" %elmayor
    if opcionMIA=="piedra" and opcionCPU=="tijera":
        elmayor=opcionMIA
        return "has ganado con %s" %elmayor
    elif opcionMIA=="papel"and opcionCPU=="tijera":
        elmayor=opcionCPU
        return "ha ganado la CPU con %s" %elmayor
    elif opcionMIA == "tijera" and opcionCPU == "tijera":
        return "queda en empate"
def principal():
    print("JUEGO PIEDRA PAPEL O TIJERA")
    print("=" * 100)
    while True:
        opcionescpu = ["piedra", "papel", "tijera"]
        opcionCPU = random.choice(opcionescpu)
        print("MENU de OPCIONES")
        print("1...PIEDRA")
        print("2...PAPEL")
        print("3...TIJERA")
        print("4...Salir")
        op=input("Ingrese una opcion ")
        if op=="1":
            print("::::::>>>> has seleccionado PIEDRA ")
            opcionMIA="piedra"
            ganador= mayor(opcionMIA,opcionCPU)
            print("RESULTADO: ", "{{ ",ganador," }} ")
        elif op=="2":
            print("::::::>>>> has seleccionado PAPEL")
            opcionMIA="papel"
            ganador = mayor(opcionMIA, opcionCPU)
            print("RESULTADO ", "{{ ",ganador," }} ")
        elif op=="3":
            print(":::::::>>>> has seleccionado TIJERA")
            opcionMIA="tijera"
            ganador = mayor(opcionMIA, opcionCPU)
            print("RESULTADO ", "{{ ",ganador," }} ")
        elif op=="4":
            print("Gracias por jugar este juego de azar")
            break
        resp = input("desea seguir jugando? ")
        if resp == "n":
            print('gracias por haber jugado')
            break


principal()
