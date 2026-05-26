
def adicionar_aresta(grafo, origem, destino):
    if origem not in grafo:
        grafo[origem] = []

    if destino not in grafo:
        grafo[destino] = []

    grafo[origem].append(destino)
    grafo[destino].append(origem)

# Grafo simples usando dicionário
# Cada chave é um nó, e o valor é uma lista de vizinhos

grafo_exemplo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B", "E"],
    "E": ["C", "E"]
}

print(grafo_exemplo)

grafo = {}

adicionar_aresta(grafo, "A", "B")
adicionar_aresta(grafo, "A", "C")
adicionar_aresta(grafo, "A", "D")
adicionar_aresta(grafo, "B", "E")
adicionar_aresta(grafo, "D", "E")
adicionar_aresta(grafo, "C", "F")
adicionar_aresta(grafo, "F", "G")
adicionar_aresta(grafo, "C", "G")

print(grafo)

