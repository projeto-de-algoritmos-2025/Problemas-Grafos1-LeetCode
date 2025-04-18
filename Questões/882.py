from collections import defaultdict
import heapq

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        graph = defaultdict(list)
        for u, v, cnt in edges:
            graph[u].append((v, cnt))
            graph[v].append((u, cnt))

        fila = [(-maxMoves, 0)]
        visitados = dict()
        subnodes = dict()
        result = 0

        while fila:
            moves_restantes, node = heapq.heappop(fila)
            moves_restantes = -moves_restantes

            if node in visitados:
                continue
            visitados[node] = moves_restantes
            result += 1

            for vizinho, cnt in graph[node]:
                aresta = (min(node, vizinho), max(node, vizinho))
                if aresta not in subnodes:
                    subnodes[aresta] = 0
                reach = min(cnt, moves_restantes)
                subnodes[aresta] += reach

                if vizinho not in visitados and moves_restantes > cnt:
                    heapq.heappush(fila, (-(moves_restantes - cnt - 1), vizinho))

        for u, v, cnt in edges:
            aresta = (min(u, v), max(u, v))
            subnodes_count = subnodes.get(aresta, 0)
            result += min(cnt, subnodes_count)

        return result
