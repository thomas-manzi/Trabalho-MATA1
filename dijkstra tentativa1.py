class Vertice:
    # Classe para definir um vértice
    # construtor
    def __init__(self, i):
        self.id = i # nome do vértice
        self.visitado = False # define se ele já foi checado, começa negativo
        self.vizinhos = [] # lista dos vértices adjacentes, começa vazia
        self.anterior = None # vértice de origem do atual, no primeiro é nulo
        self.distancia = float('inf') # distância somada desde a origem, por padrão é infinito

    def juntarVizinho(self, v, p):
        # adicionar os vizinhos do vértice, v é nome do vértice e p é o peso da aresta
        if v not in self.vizinhos:
            self.vizinhos.append([v, p])

class Grafo:
    # Classe para definir o grafo em si
    def __init__(self):
        self.vertices = {} # os vértices serão guardados em dicionário

    def adicionarVertice(self, v):
        # Se o vértice já não estiver no grafo, ele é adicionado; v é o nome do vértice
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)

    def adicionarAresta(self, a, b, p):
        # a e b são os vértices da aresta, p é o peso
        # se os dois vértices estiverem no grafo,
        # a é adicionado à lista de vizinhos de b usando a função juntarVizinho
        # e b é adicionado à lista de vizinhos de a usando a mesma função

        if a in self.vertices and b in self.vertices:
            self.vertices[a].juntarVizinho(b, p)
            self.vertices[b].juntarVizinho(a, p)

    def minimo(self, lista):
        # define qual o vértice com a menor distância
        if len(lista) > 0: # se a lista tivee algum valor
            m = self.vertices[lista[0]].distancia # essa variável pega a distância do primeiro vértice da lista
            v = lista[0] # essa variável pega o primeiro vértice da lista
            for e in lista: # pra cada elemento da lista
                if m > self.vertices[e].distancia: # se o vértice tiver distância menor que a menor distância atual
                    m = self.vertices[e].distancia # a distância dele passa a ser a menor distância
                    v = e # e esse passa a ser o vértice de menor distância
        return v


    def dijkstra(self, a):
        # função do algoritmo em si, a é o vértice inicial
        # checar se o vértice passado faz parte do grafo
        if a in self.vertices:
            self.vertices[a].distancia = 0 # atribuir ao vértice inicial distância 0
            atual = a # definir que o vértice a é o atual
            nao_visitados = [] # criar lista de vértices não visitados

            for v in self.vertices:
                if v != a:
                    self.vertices[v].distancia = float('inf')
                    # todos os vértices, exceto o atual, têm distância infinita
                self.vertices[v].anterior = None
                # todos os vértices começam sem vértice anterior
                nao_visitados.append(v)
                # adicionar todos os vértices à lista de não visitados

            while len(nao_visitados) > 0: # enquanto tiver vértice na lista de vértices
                for vizinho in self.vertices[atual].vizinhos: # para cada vizinho do vértice atual
                    if self.vertices[vizinho[0]].visitado == False: # se o vizinho não tiver sido visitado
                        if self.vertices[vizinho[atual]].distancia + vizinho[1] < self.vertices[vizinho[0]].distancia:
                            self.vertices[vizinho[0]].distancia = self.vertices[vizinho[atual].distancia + vizinho[1]
                            # se a distancia atual mais o peso da aresta que está sendo checada for MENOR que a distância do vértice vizinho,
                            # a distância do vértice vizinho passa a ser a distância atual
                            self.vertices[vizinho[0]].anterior = atual # o vértice atual passa a ser anterior ao vizinho
                self.vertices[atual].visitado = True # vértice atual passa a estar visitado
                nao_visitados.remove(atual) # ele é removido da lista de não visitados
                atual = self.minimo(nao_visitados) # o vértice de menor distância passa a ser o atual, usando a função "minimo"



            #          atribuir vértice anterior nulo


        else:
            return False

def imprimirGrafo(self):
    for v in self.vertices:
        print(f"A distância do vértice {v} é {self.vertices[v].distancia}, chegando desde o vértice {self.vertices[v].anterior}")

def caminho(self, a, b):
    caminho = []
    atual = b
    while atual != None:
        caminho.insert(0, atual)
        atual = self.vertices[atual].anterior
    return [caminho, self.vertice[b].distancia]

def main():
    # adicionar o vértices e as arestas do grafo mostrado em sala, o terceiro parâmetro é o peso da aresta
    g = Grafo()

    g.adicionarVertice(1)
    g.adicionarVertice(2)
    g.adicionarVertice(3)
    g.adicionarVertice(4)
    g.adicionarVertice(5)
    g.adicionarVertice(6)
    g.adicionarVertice(7)
    g.adicionarAresta(1, 2, 1)
    g.adicionarAresta(1, 3, 2)
    g.adicionarAresta(1, 4, 3)
    g.adicionarAresta(2, 3, 3)
    g.adicionarAresta(2, 5, 2)
    g.adicionarAresta(3, 4, 4)
    g.adicionarAresta(3, 5, 1)
    g.adicionarAresta(3, 6, 3)
    g.adicionarAresta(4, 6, 2)
    g.adicionarAresta(5, 6, 1)
    g.adicionarAresta(5, 7, 1)
    g.adicionarAresta(6, 7, 4)
    g.adicionarAresta(7, 5, 1)

    g.dijkstra(1)
    print("O caminho mais curto por Dijkstra é: ")
    print(g.caminho(1, 7))
    print("----")
    print("O grafo final é: ")
    g.imprimirGrafo()

main()

