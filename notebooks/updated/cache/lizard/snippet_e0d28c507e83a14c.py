def mutual_accessibility(graph):
    recursionlimit = getrecursionlimit()
    setrecursionlimit(max(len(graph.nodes()) * 2, recursionlimit))
    mutual_access = {}
    stack = []
    low = {}

    def visit(node):
        if node in low:
            return
        num = len(low)
        low[node] = num
        stack_pos = len(stack)
        stack.append(node)
        for successor in graph.neighbors(node):
            visit(successor)
            low[node] = min(low[node], low[successor])
        if num == low[node]:
            component = stack[stack_pos:]
            del stack[stack_pos:]
            component.sort()
            for each in component:
                mutual_access[each] = component
            for item in component:
                low[item] = len(graph)
    for node in graph:
        visit(node)
    setrecursionlimit(recursionlimit)
    return mutual_access