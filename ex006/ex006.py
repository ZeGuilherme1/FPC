class Grafo:
    def __init__(self, qtd_nos):
        # inicializa o grafo com 'num_nos' nós
        self.qtd_nos = qtd_nos
        # matriz de adjacência para indicar se há conexão entre os nós
        self.adj_matrix = [[0] * qtd_nos for _ in range(qtd_nos)]
        # coordenadas (x, y) para cada nó
        self.coordenadas = [(0, 0)] * qtd_nos
    
    def set_coord(self, no, x, y):
        # define as coordenadas (x, y) de um nó 
        if 0 <= no < self.qtd_nos:
            self.coordenadas[no] = (x, y)
    
    def add_aresta(self, no1, no2):
        # adiciona uma aresta entre no1 e no2
        if 0 <= no1 < self.qtd_nos and 0 <= no2 < self.qtd_nos:
            self.adj_matrix[no1][no2] = 1
            self.adj_matrix[no2][no1] = 1 
    
    def del_no(self, no):
        # deleta um nó e todas as arestas conectadas a ele
        if 0 <= no < self.qtd_nos:
            # remove todas as conexões desse nó
            for i in range(self.qtd_nos):
                self.adj_matrix[no][i] = 0
                self.adj_matrix[i][no] = 0
            self.coordenadas[no] = None  # remove as coordenadas do nó
    
    def del_aresta(self, no1, no2):
        # deleta a aresta entre no1 e no2
        if 0 <= no1 < self.qtd_nos and 0 <= no2 < self.qtd_nos:
            self.adj_matrix[no1][no2] = 0
            self.adj_matrix[no2][no1] = 0  # Supondo grafo não direcionado
    
    def print_grafo(self):
        # imprime a matriz de adjacência e as coordenadas
        print("Matriz de Adjacência:")
        for linha in self.adj_matrix:
            print(linha)
        
        print("\nCoordenadas dos Nós:")
        for i, coord in enumerate(self.coordenadas):
            if coord:
                print(f"Nó {i}: {coord}")
            else:
                print(f"Nó {i}: Deletado")

grafo = Grafo(5)

# define as coordenadas
grafo.set_coord(0, 1, 2)
grafo.set_coord(1, 2, 3)
grafo.set_coord(2, 3, 4)
grafo.set_coord(3, 4, 5)
grafo.set_coord(4, 5, 6)

# adicionado as arestas
grafo.add_aresta(0, 1)
grafo.add_aresta(1, 2)
grafo.add_aresta(2, 3)
grafo.add_aresta(3, 4)

grafo.del_aresta(0, 1)

grafo.del_no(1)

grafo.print_grafo()
