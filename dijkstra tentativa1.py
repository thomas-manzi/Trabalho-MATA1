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

    # imprimindo o grafo só pra conferir
    for v in g.vertices:
        print(v, "(vizinho, peso): ", g.vertices[v].vizinhos)

main()

