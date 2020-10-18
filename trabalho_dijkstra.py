grafo = {
    'a':{'b':3,'c':4,'d':7},
    'b':{'c':1,'f':5},
    'c':{'f':6, 'd':2},
    'd':{'e':3 , 'g':6},
    'e':{'g':3, 'h':4},
    'f':{'e':1, 'h':8},
    'g':{'h':2},
    'h':{'g':2}
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

            if distancia_min_vertice is None:
                distancia_min_vertice = vertice

            elif caminho_minimo[vertice] < caminho_minimo[distancia_min_vertice]:
                distancia_min_vertice = vertice
        
        opcoes_caminho = grafo[distancia_min_vertice].items()

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

    if caminho_minimo[final] != infinito and caminho_minimo[final]<0:
        print("O caminho minimo é "+ str(caminho_minimo[final]))
        print("Caminho do Grafo é "+ str(caminho))
    else:
        print("caminho não existe pois é infinito(os numeros são negativos) ")

dijkstra(grafo,'a' ,'h')



