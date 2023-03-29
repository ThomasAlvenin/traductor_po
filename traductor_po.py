import requests
import polib
import time
import os

def translate_text(text, target_language, source_language):
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}".format(source_language, target_language, text)
    response = requests.get(url)
    if response.status_code == 200:
        translation = response.json()[0][0][0]
        return translation
    else:
        return None

os.system('cls' if os.name == 'nt' else 'clear')

print("\n\n\n\n===============================================")
print("=                                             =")
print("=     Traductor de archivos .PO by            =")
print("=                                             =")
print("=             Thomas Alvenin                  =")
print("=                                             =")
print("===============================================\n\n\n")

print("Seleccione una opción:")
print("1. Traducir archivo .PO")
print("2. Salir")

opcion = input("Opción: ")

if opcion == "1":
    archivo = input("Ingrese el nombre del archivo .PO: ")
    idioma_reconocimiento = input("Ingrese el idioma de reconocimiento (ejemplo: es): ")
    idioma_salida = input("Ingrese el idioma de salida (ejemplo: en): ")

    for i in range(10, 0, -1):
        print("\rEl proceso de traducción comenzará en {} segundos...".format(i), end="")
        time.sleep(1)

    os.system('cls' if os.name == 'nt' else 'clear')

    po_file = polib.pofile(archivo)

    palabras_traducidas = 0

    for entry in po_file:
        if entry.msgid and not entry.msgstr:
            translation = translate_text(entry.msgid, idioma_salida, idioma_reconocimiento)
            if translation:
                entry.msgstr = translation
                palabras_traducidas += 1
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Progreso de la traducción:")
                print("╔══════════════════════════════════════════════════════╗")
                print("║ Palabras traducidas: {:<5}                           ║".format(palabras_traducidas))
                print("╚══════════════════════════════════════════════════════╝")
                print("Traducción de '{}': '{}'".format(entry.msgid, entry.msgstr))

    po_file.save('{}_traducido.po'.format(archivo.split('.')[0]))

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n\n\n===============================================")
    print("=                                             =")
    print("=     La traducción ha finalizado             =")
    print("=                                             =")
    print("=     correctamente.                          =")
    print("=                                             =")
    print("===============================================\n\n\n")

elif opcion == "2":
    print("Saliendo del programa...")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

else:
    print("Opción inválida. Por favor, seleccione una opción válida.")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')