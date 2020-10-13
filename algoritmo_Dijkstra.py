def matriz():
    a= 3
    arr = []
    for i in range(1,a+1):
        linha = []
        for j in range(1,a+1):
            b = int(input("numero aresta"))
            linha.append(b)
        arr.append(linha)
    
    for i in range(len(arr)):
        print(arr[i], end="\n")
        
        


matriz()





#def main():
#    vertice= int(input("quantos vertices?\n"))
#    vet = []
 #   for i in range(vertice):
#        vet.append(i+1)
#    #arestas= int(input("quantas arestas?\n"))
#    matriz_grafo = []
#    for i in range(1,vertice+1):
 #       #print(i)
 #       for j in range(1,vertice+1):
 #           peso da aresta i e j
                




#main()    