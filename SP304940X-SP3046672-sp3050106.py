# Prof dicionario em python tem uma certa dificuldade para fazer a leitura entao deixei 2 grafos e se quiser testar com outros numeros
# O primeiro grafo eh o da sua aula no slide de dijkstra e o segundo um aleatorio com os numeros de entrada 1 a n 


grafo = {
    'a':{'b':1,'c':3,'d':2},
    'b':{'a':1,'d':3,'e':2.5},
    'c':{'d':4, 'f':2},
    'd':{'e':1 , 'f':3},
    'e':{'f':1, 'g':1},
    'f':{'e':1, 'g':4},
    'g':{'e':1, 'f':4}
}

gr = {
    '1':{'2':1,'3':3.2},
    '2':{'1':1.2,'4':3.5},
    '3':{'4':4.4},
    '4':{'2':1.3}
}



def dijkstra(grafo,inicio,final):
    caminho_minimo = {} # guardar os pesos dos vertices e ser atualizado ao longo do grafo
    caminho_vertice = {} # guardar o caminho que levou ate o vertice
    caminho_grafo = grafo # passar o grafo inteiro 
    infinito = 99999 # numero para garantir que o caminho minimo seja validado
    caminho = [] #mostra o caminho que foi feito

    for vertice in caminho_grafo:   #vai iniciar todos vertices do grafo com 99999 menos o inicial para fazer a validacao
        caminho_minimo[vertice] = infinito
    caminho_minimo[inicio] = 0

    while caminho_grafo:

        distancia_min_vertice = None

        for vertice in caminho_grafo:

            if distancia_min_vertice is None: #garantir que a primeira distancia seja do primeiro vertice 'a' e na segunda seja o 'b' etc
                distancia_min_vertice = vertice

            elif caminho_minimo[vertice] < caminho_minimo[distancia_min_vertice]: #sempre validar o caminho minimo fazendo com que se algum momento algum vertice tiver menos peso que outro realizar a troca 
                distancia_min_vertice = vertice
        
        opcoes_caminho = grafo[distancia_min_vertice].items() #salvar todos os itens da distancia minima do vertice que sair do for ou seja da menor distancia

        for novo_vertice, peso in opcoes_caminho:       #dentre as opcoes que chegaram do opcoes_caminho o for vai escolher qual vertice tem o menor peso e fazer a troca

            if peso + caminho_minimo[distancia_min_vertice] < caminho_minimo[novo_vertice]:
                caminho_minimo[novo_vertice] = peso + caminho_minimo[distancia_min_vertice]
                caminho_vertice[novo_vertice] = distancia_min_vertice
        
        caminho_grafo.pop(distancia_min_vertice) # .pop tira o valor ou seja tira o 'a' na primeira volta e começa a validar denovo com o 'b' dps tira o 'b' e assim por diante e sempre ira tirar a distancia minima do vertice que foi validado

    valor_atual = final
    
    while valor_atual != inicio: #validar se existe um caminho entre o inicio e o fim e colocar o caminho feito
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
    

dijkstra(grafo,'a' ,'g')

#dijkstra(gr, '1', '4')



