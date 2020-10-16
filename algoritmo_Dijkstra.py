def matriz():
    a=int(input("numero de quantos vertices \n"))
    arr = []
    for i in range(1,a+1):
        linha = []
        for j in range(1,a+1):
            print("Vertice",i, "Ligando com o vertice",j,"\n")
            b = int(input("Peso da Aresta(caso nao tenha coloque 0)\n"))
            linha.append(b)
        arr.append(linha)
    
    #for i in range(len(arr)):
        #print(arr[i], end="\n")

    return arr    
        








def main():
    vertice = []
    vertice = matriz()
    #print(vertice)
    #for para a matriz sair identada
    for i in range(len(vertice)):
        print(vertice[i], end="\n")

    inicial = int(input("Escolha o vertice inicial"))
    contInicial = inicial
    #print(vertice[inicial-1:inicial])    #pegando os valores do vertice incial dentro da matriz representada        
    inicial = vertice[inicial-1:inicial]
    #print(inicial)

    #for i in range(len(vertice)):
        #print(i)
        #for j in range(len(vertice)):


main()    