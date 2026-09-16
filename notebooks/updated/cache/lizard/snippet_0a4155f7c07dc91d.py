def find_recursive_dependency(self):
    nodes_on_path = []

    def helper(nodes):
        for node in nodes:
            cycle = node in nodes_on_path
            nodes_on_path.append(node)
            if cycle or helper(self.deps.get(node, [])):
                return True
            nodes_on_path.pop()
        return False
    helper(self.unordered)
    return nodes_on_path