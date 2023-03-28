# Traductor de archivos .PO con la API de Google Translate

# Hecho con cariño para: apalomoo
Este script en Python utiliza la API de Google Translate para traducir un archivo .PO de un idioma a otro. El script recorre cada entrada del archivo .PO y utiliza la API de Google Translate para traducir el texto del msgid al idioma deseado y lo pone en el msgstr correspondiente.

## Requisitos

- Python 3.x
- Librería "polib"

## Instalación

- Clona o descarga el repositorio en tu computadora.                                         
- Instala la librería polib utilizando el siguiente comando en la terminal:

```bash
pip install polib
```

## Uso

- Ejecuta el script utilizando el siguiente comando en la terminal:
```bash
python traductor_po.py
```
- El script traducirá el archivo .PO y mostrará en la consola el texto original y su traducción.

## Notas

- Ten en cuenta que la API de Google Translate tiene limitaciones en cuanto al número de solicitudes que se pueden hacer en un período de tiempo determinado. Si se supera este límite, es posible que la API devuelva errores o que se bloquee temporalmente.
- Asegúrate de respetar los términos de servicio de la API de Google Translate y de cualquier otro servicio de traducción que utilices.
- Si deseas utilizar la API de Google Cloud Translate en lugar de la API de Google Translate gratuita, cambia la URL en la función translate_text y utiliza la autenticación de Google Cloud en lugar de la clave de API.
