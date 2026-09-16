def find_children(self, predicate, breadth_first=True):

    def _search(node, klass):
        results = []
        childrenToExamine = []
        for child in node.children:
            if predicate(child):
                results.append(child)
            elif not breadth_first:
                results.extend(_search(child, klass))
            elif breadth_first:
                childrenToExamine.append(child)
        if breadth_first:
            for child in childrenToExamine:
                results.extend(_search(child, klass))
        return results
    return _search(self, predicate)