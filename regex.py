import re


def main():
    run = True
    while run:
        print('''---Bienvenido---\n
        \rOpciones disponibles:
        \r\r1- Validar email
        \r\r2- Validar URL
        \r\r0- Salir
        ''')
        try:
            opt = int(input('Ingrese opcion:'))
        except:
            print('Ingres un valor numerico')
            input("Presione una tecla para continuar...")
            continue
        if opt == 1:
            mail = input('Ingrese mail: ')
            print(valid(ismail(mail)))
            input("Presione una tecla para continuar...")
        elif opt == 2:
            url = input('Ingrese URL: ')
            print(valid(isurl(url)))
            input("Presione una tecla para continuar...")
        elif opt == 0:
            run = False
        else:
            print('Error, opcion invalida!')
            input("Presione una tecla para continuar...")


def isurl(url):
    urlcheck = re.compile(r'^[htt(p|ps):\/\/?]+[\w.-]+\.([\w]{2,6})*[(\/)]$', re.X)
    result = urlcheck.search(url)
    return result

def ismail(mail):
    mailcheck = re.compile(r'\b[\w.-]+@[\w.-]+\.[a-zA-Z]{2,6}\b', re.X)
    result = mailcheck.search(mail)
    return result


def valid(bool):
    if bool:
        return 'Es valido'
    else:
        return 'No valido'


if __name__ == '__main__':
    main()

