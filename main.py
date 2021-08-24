def cria_matriz():

    matriz = []
    M = int(input("Quantas linhas(M) terá a matriz: "))
    N = int(input("Qual será o número de colunas(N) dessa matriz: "))

    for i in range(M):
        linha = []
        for j in range(N):
            valor = int(input("Digite valor do elemento [" + str(i+1) + "][" + str(j+1) + "]" + " da matriz: "))
            linha.append(valor)
        matriz.append(linha)

    print("\n" + "Matriz Escrita: ",M, "X",N,"\n")
    for i in range(len(matriz)):
        print(matriz[i])


    return matriz

def zera_linha(matriz):

    listai = []
    listaj = []
    resultado = matriz

    for i in range(len(resultado)):
        for j in range(len(resultado[0])):
            if (resultado[i][j] == 0):
                listai.append(i)
                listaj.append(j)

    for i in range(len(listai)):
        for j in range(len(resultado[0])):
            resultado[listai[i]][j] = 0

    for j in range(len(listaj)):
        for i in range(len(resultado)):
            resultado[i][listaj[j]] = 0


    print("\n" + "Matriz Transformada pelo algoritmo: " + "\n")
    for i in range(len(resultado)):
        print(resultado[i])
    return resultado

def interacao_com_usuario():
     print("Vamos começar! Primeiro, crie a sua matriz: ")
     print(100*"-" + "\n")
     A = cria_matriz()
     zera_linha(A)


interacao_com_usuario()





































