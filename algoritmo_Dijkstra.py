def matriz():
    a=int(input("Quantos vertices \n"))
    print(end="\n")
    arr = []
    for i in range(1,a+1):
        linha = []
        for j in range(1,a+1):
            print("Vertice",i, "Ligando com o Vertice",j,"\n")
            b = int(input("Peso da Aresta(caso nao tenha coloque 0)\n"))
            print(end="\n")
            linha.append(b)
        arr.append(linha)
    
    #for i in range(len(arr)):
        #print(arr[i], end="\n")

    return arr    
        








def main():
    grafo = []
    grafo = matriz()
    #print(grafo)
    #for para a matriz sair identada
    for i in range(len(grafo)):
        print("Vertice", i+1, end="\n")
        print(grafo[i], end="\n")

    inicial = int(input("Escolha o vertice inicial \n"))
    vertInicial = inicial
    #print(grafo[inicial-1:inicial])    #pegando os valores do vertice incial dentro da matriz representada        
    inicial = grafo[inicial-1:inicial]
    #print(inicial)

    #for i in range(len(grafo)):
        #print(i)
        #for j in range(len(grafo)):


main()    