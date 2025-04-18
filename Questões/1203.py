from collections import defaultdict, deque
from typing import List

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topologicalSort(graph, grau_entrada):
            fila = deque([no for no in range(len(grau_entrada)) if grau_entrada[no] == 0])
            result = []
            while fila:
                no = fila.popleft()
                result.append(no)
                for neighbor in graph[no]:
                    grau_entrada[neighbor] -= 1
                    if grau_entrada[neighbor] == 0:
                        fila.append(neighbor)
            return result if len(result) == len(grau_entrada) else []

        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        grafoItems = defaultdict(list)
        itemInDegree = [0] * n
        for i in range(n):
            for pre in beforeItems[i]:
                grafoItems[pre].append(i)
                itemInDegree[i] += 1
        items_ord = topologicalSort(grafoItems, itemInDegree)
        if not items_ord:
            return []

        grafoGrupos = defaultdict(list)
        groupInDegree = [0] * group_id
        for i in range(n):
            for pre in beforeItems[i]:
                if group[i] != group[pre]:
                    grafoGrupos[group[pre]].append(group[i])
                    groupInDegree[group[i]] += 1
        grupos_ord = topologicalSort(grafoGrupos, groupInDegree)
        if not grupos_ord:
            return []

        groupToItems = defaultdict(list)
        for item in items_ord:
            groupToItems[group[item]].append(item)

        result = []
        for grp in grupos_ord:
            result.extend(groupToItems[grp])
        return result

