grafo = {
    'a':{'b':1,'c':3,'d':2},
    'b':{'a':1,'d':3,'e':2.5},
    'c':{'d':4, 'f':2},
    'd':{'e':1 , 'f':3},
    'e':{'f':1, 'g':1},
    'f':{'e':1, 'g':4},
    'g':{'e':1, 'f':4}
}

def dijkstra(grafo,inicio,final):
    caminho_minimo = {} # guardar os pesos dos vertices e ser atualizado ao longo do grafo
    caminho_vertice = {} # guardar o caminho que levou ate o vertice
    caminho_grafo = grafo # passar o grafo inteiro 
    infinito = 99999 # numero para garantir que o caminho minimo seja validado
    caminho = [] #mostra o caminho que foi feito

    for vertice in caminho_grafo:
        caminho_minimo[vertice] = infinito
    caminho_minimo[inicio] = 0

    while caminho_grafo:

        distancia_min_vertice = None

        for vertice in caminho_grafo:

            if distancia_min_vertice is None: #garantir que a primeira distancia seja do primeiro vertice 'a'
                distancia_min_vertice = vertice

            elif caminho_minimo[vertice] < caminho_minimo[distancia_min_vertice]:
                distancia_min_vertice = vertice
        
        opcoes_caminho = grafo[distancia_min_vertice].items() #salvar todos os caminhos dos vertices que sairam do for

        for novo_vertice, peso in opcoes_caminho:

            if peso + caminho_minimo[distancia_min_vertice] < caminho_minimo[novo_vertice]:
                caminho_minimo[novo_vertice] = peso + caminho_minimo[distancia_min_vertice]
                caminho_vertice[novo_vertice] = distancia_min_vertice
        
        caminho_grafo.pop(distancia_min_vertice)

    valor_atual = final
    
    while valor_atual != inicio:
        try:
            caminho.insert(0, valor_atual)
            valor_atual = caminho_vertice[valor_atual]

        except KeyError:
            print("Nao tem caminho entre o vertice incial e o final")
            break

    caminho.insert(0, inicio)

    if caminho_minimo[final] != infinito :
        print("O caminho minimo é "+ str(caminho_minimo[final]))
        print("Caminho do Grafo é "+ str(caminho))
    

dijkstra(grafo,'b' ,'a')



