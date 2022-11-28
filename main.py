import os

def add_text (texto):
    data = open(file, 'a')
    data.write(texto)
    data.close()
    
def write_text (texto):
    data = open(file, 'w')
    for li in texto:
        data.writelines(li+'\n')
    data.close()

list_dir = os.listdir('./')
file = input('El nombre del archivo: ')
file += '.txt'
linea = ''
texto = []
while linea != 'salir':
    linea = input('Escriba el texto que desea añadir o escriba "salir": ')
    if linea != 'salir':
        texto.append(linea)

if file in list_dir:
    print('El archivo ya existe, se actualizará.')
    for li in texto:
        add_text('\n' + li)
else: 
    print('El archivo no existe, se creará.')
    write_text(texto)



