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

## Códigos de idioma del traductor de Google ISO-639-1

| ISO             | Idioma                                                                |
| ----------------- | ------------------------------------------------------------------ |
|af	| Afrikáans
sq	|Albanés
am	|Amárico
ar	||Árabe
hy	|Armenio
az	|Azerí
eu	|Vasco
be	|Bielorruso
bn	|Bengalí
bs	|Bosnio
bg	|Búlgaro
ca	|Catalán
ceb	|Cebuano
zh	|Chino
zh-CN	|Chino (simplificado)
zh-TW	|Chino (tradicional)
co	|Corso
hr	|Croata
cs	|Checo
da	|Danés
nl	|Holandés
en	|Inglés
eo	|Esperanto
et	|Estonio
fi	|Finlandés
fr	||Francés
fy	|Frisón
gl	|Gallego
ka	|Georgiano
de	|Alemán
el	|Griego
gu	|Guyaratí
ht	|Criollo haitiano
ha	|Hausa
haw	|Hawaiano
he	|Hebreo
iw	|Hebreo
hi	|Hindi
hmn	|Hmong
hu	|Húngaro
is	|Islandés
ig	|Igbo
id	|Indonesio
ga	|Irlandés
it	|Italiano
ja	|Japonés
jv	|Javanés
kn	|Canarés
kk	|Kazajo
km	|Jemer
rw	|Kiñaruanda
ko	|Coreano
ku	|Kurdo
ky	|Kirguís
lo	|Laosiano
la	|Latín
lv	|Letón
lt	|Lituano
lb	|Luxemburgués
mk	|Macedonio
mg	|Malgache
ms	|Malayo
ml	|Malabar
mt	|Maltés
mi	|Maorí
mr	|Maratí
mn	|Mongol
my	|Birmano
ne	|Nepalí
no	|Noruego
ny	|Nyanja (chichewa)
or	|Odia (oriya)
ps	|Pastún
fa	|Persa
pl	|Polaco
pt	|Portugués (Portugal y Brasil)
pa	|Panyabí
ro	|Rumano
ru	|Ruso
sm	|Samoano
gd	|Gaélico escocés
sr	|Serbio
st	|Sesoto
sn	|Shona
sd	|Sindhi
si	|Cingalés
sk	|Eslovaco
sl	|Esloveno
so	|Somalí
es	|Español
su	|Sundanés
sw	|Suajili
sv	|Sueco
tl	|Tagalo (filipino)
tg	|Tayiko
ta	|Tamil
tt	|Tártaro
te	|Telugú
th	|Tailandés
tr	|Turco
tk	|Turcomano
uk	|Ucraniano
ur	|Urdu
ug	|Uigur
uz	|Uzbeko
vi	|Vietnamita
cy	|Galés
xh	|Xhosa
yi	|Yiddish
yo	|Yoruba
zu	|Zulú

## Notas

- Ten en cuenta que la API de Google Translate tiene limitaciones en cuanto al número de solicitudes que se pueden hacer en un período de tiempo determinado. Si se supera este límite, es posible que la API devuelva errores o que se bloquee temporalmente.
- Asegúrate de respetar los términos de servicio de la API de Google Translate y de cualquier otro servicio de traducción que utilices.
- Si deseas utilizar la API de Google Cloud Translate en lugar de la API de Google Translate gratuita, cambia la URL en la función translate_text y utiliza la autenticación de Google Cloud en lugar de la clave de API.
