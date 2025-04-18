from collections import defaultdict, deque
from typing import List

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topologicalSort(graph, in_degree):
            queue = deque([node for node in range(len(in_degree)) if in_degree[node] == 0])
            result = []
            while queue:
                node = queue.popleft()
                result.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            return result if len(result) == len(in_degree) else []

        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        itemGraph = defaultdict(list)
        itemInDegree = [0] * n
        for i in range(n):
            for pre in beforeItems[i]:
                itemGraph[pre].append(i)
                itemInDegree[i] += 1
        sortedItems = topologicalSort(itemGraph, itemInDegree)
        if not sortedItems:
            return []

        groupGraph = defaultdict(list)
        groupInDegree = [0] * group_id
        for i in range(n):
            for pre in beforeItems[i]:
                if group[i] != group[pre]:
                    groupGraph[group[pre]].append(group[i])
                    groupInDegree[group[i]] += 1
        sortedGroups = topologicalSort(groupGraph, groupInDegree)
        if not sortedGroups:
            return []

        groupToItems = defaultdict(list)
        for item in sortedItems:
            groupToItems[group[item]].append(item)

        result = []
        for grp in sortedGroups:
            result.extend(groupToItems[grp])
        return result
