'''



'''

def soma(a, b):

    return a + b


def subtrair(a, b):

    return a - b


def multiplicar(a,b):

    return a * b


def dividir(a,b):

    if b == 0:
        return "Erro: Divisão po zero não permitida"
    return a / b

def divisao_inteira(a, b):
    """ 
    Retorna apenas a parte inteira da divisão a 'a' por 'b'.
    Parametros: a (int/floart), b (int/float)
    Retorno: o quociente inteiro ou uma mensagem de erro se b == 0.
    """
    if b == 0:
        return "erro: Divisão por zero não e permitida."
    return a // b

def resto_divisao(a, b):
    if b == 0:
        Return "erro: divisao por zzero nao e permitida."
    return a % b


def potencia(base, expoente):
    return base ** expoente


def calcular_media(lista_numeros):
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)


def calcular_media(lista_numeros):

    if not lista_numeros:
        return 0
    return sum(lista_numeros) /len(lista_numeros)


def e_par(numero):
    return numero % 2 == 0




















def caucular_medida(lista_numeros):

    if not lista_numeros:
        reuturn 0
    return sum(lista_numeros) / len(lista_numeros)

def e_par(numeros):
    return numero % 2 == 0