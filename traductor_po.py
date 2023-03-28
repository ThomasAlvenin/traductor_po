import requests
import polib
import time
import os

# Función para traducir un texto con la API de Google Translate
def translate_text(text, target_language, source_language):
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}".format(source_language, target_language, text)
    response = requests.get(url)
    if response.status_code == 200:
        translation = response.json()[0][0][0]
        print("Traducción de '{}': '{}'".format(text, translation))
        return translation
    else:
        print("Error al traducir '{}': {}".format(text, response.status_code))
        return None

# Limpia la pantalla
os.system('cls' if os.name == 'nt' else 'clear')

# Mensaje de bienvenida
print("\n\n\n\n===============================================")
print("=                                             =")
print("=     Traductor de archivos .PO by            =")
print("=                                             =")
print("=             Thomas Alvenin                  =")
print("=                                             =")
print("===============================================\n\n\n")

# Menú de opciones
print("Seleccione una opción:")
print("1. Traducir archivo .PO")
print("2. Salir")

# Pide al usuario que seleccione una opción
opcion = input("Opción: ")

# Si el usuario selecciona la opción 1, traduce el archivo .PO
if opcion == "1":
    # Pide al usuario que ingrese el nombre del archivo .PO
    archivo = input("Ingrese el nombre del archivo .PO: ")

    # Pide al usuario que ingrese el idioma de reconocimiento
    idioma_reconocimiento = input("Ingrese el idioma de reconocimiento (ejemplo: es): ")

    # Pide al usuario que ingrese el idioma de salida
    idioma_salida = input("Ingrese el idioma de salida (ejemplo: en): ")

    # Espera 10 segundos antes de empezar
    for i in range(10, 0, -1):
        print("\rEl proceso de traducción comenzará en {} segundos...".format(i), end="")
        time.sleep(1)

    # Limpia la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

    # Carga el archivo .PO
    po_file = polib.pofile(archivo)

    # Inicializa el contador de palabras traducidas
    palabras_traducidas = 0

    # Recorre cada entrada del archivo .PO
    for entry in po_file:
        # Si hay un msgid y un msgstr vacío, traduce el msgid y lo pone en msgstr
        if entry.msgid and not entry.msgstr:
            translation = translate_text(entry.msgid, idioma_salida, idioma_reconocimiento)
            if translation:
                entry.msgstr = translation
                palabras_traducidas += 1
                # Muestra la traducción
                os.system('cls' if os.name == 'nt' else 'clear')
                print("╔══════════════════════════════════════════════════════╗")
                print("║ Palabras traducidas: {:<5}                               ║".format(palabras_traducidas))
                print("╚══════════════════════════════════════════════════════╝")
                print("Traducción de '{}': '{}'".format(entry.msgid, entry.msgstr))
                

    # Guarda los cambios en el archivo .PO
    po_file.save('{}_traducido.po'.format(archivo.split('.')[0]))

    # Limpia la pantalla y muestra un mensaje de finalización
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n\n\n===============================================")
    print("=                                             =")
    print("=     La traducción ha finalizado             =")
    print("=                                             =")
    print("=     correctamente.                          =")
    print("=                                             =")
    print("===============================================\n\n\n")

# Si el usuario selecciona la opción 2, sale del programa
elif opcion == "2":
    print("Saliendo del programa...")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

# Si el usuario selecciona una opción inválida, muestra un mensaje de error
else:
    print("Opción inválida. Por favor, seleccione una opción válida.")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')