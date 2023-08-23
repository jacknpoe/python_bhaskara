# Calcula o valor de x usando a fórmula de Bhaskara
# Versões
# 0.1 23/08/2023 Primeira implementação, para testes

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    if b == 0:
        print("x é indefinido")
    else:
        if c == 0:
            print("x = 0")
        else:
            print("x = " + str(c / b * -1))
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("x é indefinido")
    else:
        if delta == 0:
            print("x = " + str((b * -1) / (2 * a)))
        else:
            x1 = (b * -1 - delta ** 0.5) / (2 * a)
            x2 = (b * -1 + delta ** 0.5) / (2 * a)
            print("x = " + str(x1) + " e " + str(x2))
