# Script 3 – Clasificador ACL IPv4
# Evaluación N°1 Redes Virtualizadas

print('=== Clasificador de ACL IPv4 ===')
print('VirtualNetwork S.A.')
print()

try:
    acl_num = int(input('Ingrese el número de ACL IPv4: '))

    # ACL Estándar: 1-99 y 1300-1999
    if (1 <= acl_num <= 99) or (1300 <= acl_num <= 1999):
        print(f'El número {acl_num} corresponde a una ACL ESTÁNDAR.')
        print('Rango: 1-99 o 1300-1999')
        print('Filtra tráfico basándose solo en IP origen.')

    # ACL Extendida: 100-199 y 2000-2699
    elif (100 <= acl_num <= 199) or (2000 <= acl_num <= 2699):
        print(f'El número {acl_num} corresponde a una ACL EXTENDIDA.')
        print('Rango: 100-199 o 2000-2699')
        print('Filtra por IP origen, IP destino, protocolo y puerto.')

    else:
        print(f'El número {acl_num} NO corresponde a ninguna lista de acceso IPv4.')
        print('Verifique el número ingresado.')

except ValueError:
    print('Error: Debe ingresar un número entero válido.')
