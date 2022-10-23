from math import factorial

def mensagemBonita(sessao):
    print("\n",sessao, "\n", ("---------------------------------------------"))

def conceito():
    mensagemBonita("CONCEITO")
    print("\tA distribuição binomial é um cálculo estatístico utilizado para\n\tidentificar a probabilidade de ocorrência de determinado evento\n\tdentro de um sistema fechado e utilizando de uma sequência\n\tlimitada de tentativas.")

def formula():
    mensagemBonita("FÓRMULA")
    print('\tP(x) = Cn,x . (p)^x. (q)^n-x')
    print("\t----------------------------------")
    print("\tn = número de observações\n\tp = probabilidade de sucesso\n\tx = número especificado de sucesso")
    print("\t----------------------------------")

def combinacao(n, p):
    x = factorial(n) #fatoral de N
    y = factorial(p) #fatoral de P
    fatorial = (x/((factorial(n-p))*y)) #combinação de N e P
    return fatorial

def Binomial(p, x, q, n):
    c = combinacao(n, x)
    distriBi = (c * (p**x) * (q**(n-x)))
    return distriBi

def Acumulada(p, x, q, n):
    soma = 0
    for i in range(x+1):
        acum = Binomial(p, i, q, n)
        soma+=acum
        
    return soma

def menu():
    mensagemBonita("| OPÇÕES ")
    print('\t1- | CONCEITUAÇÃO ')
    print('\t2- | FÓRMULA ')
    print('\t3- | CALCULAR A DISTRUIBUIÇÃO BINOMIAL INDIVIDUAL ')
    print('\t4- | CALCULAR A DISTRUIBUIÇÃO DINOMIAL ACUMULADA  ')
    print('\t5- | DEVS ')
    print('\t0- | SAIR ')
    opção = int(input("\t"))
    return opção

def saida():
    while True:
        opção = menu()
        if opção == 0:
            break
        if opção == 1:
            conceito()
        if opção == 2:
            formula()
        if opção == 3:
            mensagemBonita("DISTRUIBUIÇÃO BINOMIAL INDIVIDUAL")
            N = int(input("\tINSIRA UM VALOR INTEIRO PARA 'n' (Número de observações): "))
            P = float(input("\tINSIRA UM VALOR DECIMAL PARA 'p' (Probabilidade de sucesso): "))
            X = int(input("\tINSIRA UM VALOR INTEIRO PARA 'x' (número especificado de sucesso): "))
            Q = (1 - P)
            Px = Binomial(P, X, Q, N)
            Px = Px * 100
            print(f"\nP({X}) = {Px:.4}%\n")
        if opção == 4:
            N = int(input("\tINSIRA UM VALOR INTEIRO PARA 'n' (Número de observações): "))
            P = float(input("\tINSIRA UM VALOR DECIMAL PARA 'p' (Probabilidade de sucesso): "))
            X = int(input("\tINSIRA UM VALOR INTEIRO PARA 'x' (número especificado de sucesso): "))
            Q = (1 - P)
            Px = Acumulada(P, X, Q, N)
            Px = Px * 100
            print(f"\nP(<={X}) = {Px:.4}%\n")
        if opção == 5:
            print(" DEVS : GABRIEL HENRIQUE MENONCIN\n\tJOSÉ VITOR TESSARO")

saida()