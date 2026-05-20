from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


class Solution:
    def cloneGraph(self, node):

        if not node:
            return None

        # --------------------------------------------------
        # ESTADO INICIAL
        # --------------------------------------------------

        print("\n[1] Criando fila BFS")
        queue = deque([node])

        print(f"queue -> {[n.val for n in queue]}")

        print("\n[2] Criando hashmap de clones")
        clones = {
            node.val: Node(node.val)
        }

        print(f"clones -> {list(clones.keys())}")

        # --------------------------------------------------
        # BFS
        # --------------------------------------------------

        while queue:

            print("\n" + "=" * 50)

            # ----------------------------------------------
            # REMOVENDO DA FILA
            # ----------------------------------------------

            current = queue.popleft()

            print(f"\n[3] Removendo da fila -> {current.val}")

            print(f"queue agora -> {[n.val for n in queue]}")

            current_clone = clones[current.val]

            print(f"\n[4] Clone atual -> {current_clone.val}")

            print(
                f"Vizinhos do nó {current.val} -> "
                f"{[n.val for n in current.neighbors]}"
            )

            # ----------------------------------------------
            # VISITANDO VIZINHOS
            # ----------------------------------------------

            for neighbor in current.neighbors:

                print("\n" + "-" * 30)

                print(
                    f"Visitando vizinho {neighbor.val}"
                )

                # ------------------------------------------
                # AINDA NÃO FOI CLONADO
                # ------------------------------------------

                if neighbor.val not in clones:

                    print(
                        f"Nó {neighbor.val} ainda NÃO clonado"
                    )

                    neighbor_clone = Node(neighbor.val)

                    clones[neighbor.val] = neighbor_clone

                    print(
                        f"Clone criado -> {neighbor_clone.val}"
                    )

                    queue.append(neighbor)

                    print(
                        f"Adicionado na fila -> {neighbor.val}"
                    )

                    print(
                        f"queue -> {[n.val for n in queue]}"
                    )

                else:
                    print(
                        f"Nó {neighbor.val} já existe no hashmap"
                    )

                # ------------------------------------------
                # CONECTANDO CLONES
                # ------------------------------------------

                current_clone.neighbors.append(
                    clones[neighbor.val]
                )

                print(
                    f"Conectando "
                    f"{current_clone.val} -> "
                    f"{clones[neighbor.val].val}"
                )

            # ----------------------------------------------
            # ESTADO FINAL DA ITERAÇÃO
            # ----------------------------------------------

            print("\n[5] Estado atual dos clones:")

            for k, v in clones.items():

                print(
                    f"{k} -> "
                    f"{[n.val for n in v.neighbors]}"
                )

        print("\n" + "=" * 50)
        print("GRAFO CLONADO FINALIZADO")

        return clones[node.val]


# ======================================================
# MONTANDO GRAFO DE TESTE
# ======================================================

# Grafo:
#
# 1 -- 2
# |    |
# 4 -- 3
#

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

# ======================================================
# EXECUTANDO
# ======================================================

sol = Solution()

clone = sol.cloneGraph(n1)