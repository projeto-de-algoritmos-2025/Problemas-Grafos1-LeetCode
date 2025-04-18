class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        def dfs(no, tempo, prob):
            nonlocal probabilidade
            vizinhos = grafo[no]
            nosNaoVisitados = [v for v in vizinhos if v not in nosVisitados]

            if tempo > t:
                return

            if no == target:
                if tempo == t or not nosNaoVisitados:
                    probabilidade = prob
                return

            if nosNaoVisitados:
                p = 1 / len(nosNaoVisitados)

            for v in nosNaoVisitados:
                nosVisitados.add(v)
                dfs(v, tempo + 1, prob * p)
                nosVisitados.remove(v)

        grafo = defaultdict(list)
        for a, b in edges:
            grafo[a].append(b)
            grafo[b].append(a)

        nosVisitados = set()
        nosVisitados.add(1)
        probabilidade = 0

        dfs(1, 0, 1)

        return probabilidade
