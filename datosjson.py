# Script datosjson.py
# Evaluación N°1 Redes Virtualizadas – VirtualNetwork S.A.

import json
from datetime import datetime

print("=============================================")
print("   Análisis de Token JSON")
print("   VirtualNetwork S.A.")
print("=============================================")
print()

# Ruta del archivo JSON (ajustada a tu entorno)
ruta_json = '/home/devasc/labs/devnet-src/parsing/myfile.json'

try:
    # Abrir y cargar JSON
    with open(ruta_json, 'r') as json_file:
        datos = json.load(json_file)

    print("✔ Archivo JSON cargado correctamente")
    print()

    # Mostrar claves disponibles
    print("Claves disponibles en el archivo:")
    for clave in datos.keys():
        print(f" - {clave}")
    print()

    # Mostrar token
    print("Token de autenticación:")
    print(f"  {datos['access_token']}")
    print()

    # Tiempo de expiración
    segundos = datos['expires_in']
    minutos = segundos // 60
    horas = minutos // 60
    dias = horas // 24

    print("Tiempo antes de expiración del token:")
    print(f"  {segundos} segundos")
    print(f"  {minutos} minutos")
    print(f"  {horas} horas")
    print(f"  {dias} días")
    print()

    # Mostrar refresh token si existe
    if 'refresh_token' in datos:
        print("Refresh Token:")
        print(f"  {datos['refresh_token']}")
        print()

    # Fecha actual del sistema
    ahora = datetime.now()
    print("Fecha actual del sistema:")
    print(f"  {ahora}")
    print()

    print("=============================================")
    print(" Análisis completado correctamente")
    print("=============================================")

except FileNotFoundError:
    print("❌ Error: No se encontró el archivo JSON.")
    print("Verifique la ruta:", ruta_json)

except KeyError as e:
    print(f"❌ Error: Falta la clave {e} en el JSON.")

except json.JSONDecodeError:
    print("❌ Error: El archivo JSON tiene un formato inválido.")

except Exception as e:
    print(f"❌ Error inesperado: {e}")
