import requests
import polib

# Función para traducir un texto con la API de Google Translate
def translate_text(text, target_language):
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}".format('es', target_language, text)
    response = requests.get(url)
    if response.status_code == 200:
        translation = response.json()[0][0][0]
        print("Traducción de '{}': '{}'".format(text, translation))
        return translation
    else:
        print("Error al traducir '{}': {}".format(text, response.status_code))
        return None

# Carga el archivo .PO
po_file = polib.pofile('archivo.po')

# Recorre cada entrada del archivo .PO
for entry in po_file:
    # Si hay un msgid y un msgstr vacío, traduce el msgid y lo pone en msgstr
    if entry.msgid and not entry.msgstr:
        translation = translate_text(entry.msgid, 'en') # Cambiar 'es' por el idioma deseado
        if translation:
            entry.msgstr = translation

# Guarda los cambios en el archivo .PO
po_file.save('archivo_traducido.po')