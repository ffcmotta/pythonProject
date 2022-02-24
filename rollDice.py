from pynput.keyboard import Key, Listener
import random

def rollDice(key):
    if key == Key.enter:
        number = random.randint(1,6)
        print(number)
    else:
        exit()

resposta = ""

while resposta != "S" or resposta != "N":
    resposta = input("Você deseja jogar o dado? (S/N)")

    if resposta == "S":
        print("Aperte <ENTER> para jogar o dado (<ESC> para finalizar)")

        with Listener(on_press = rollDice) as listener:
            listener.join()

    elif resposta == "N":
        print("Até logo!")
        exit()

    else:
        print("Sua resposta deve ser S/N.")