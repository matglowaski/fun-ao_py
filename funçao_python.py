# def imprimir_name(nome):
#     print(f"Salve, {nome}!")
# nome_user = input("Digite seu nome: ")
# imprimir_name(nome_user)

def imprimir_nome():
    print("Matheus")
imprimir_nome()

def maior(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    else:
        return c
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
maior_n = maior(num1, num2, num3)
print(maior_n)

def criar_vetor():
    vetor = [0] * 5
    print(vetor)
    return(vetor)
criar_vetor()

def inverter(texto):
    invertido = texto[::-1]
    print(invertido)
texto = (input("Digite algo: "))
inverter(texto)
