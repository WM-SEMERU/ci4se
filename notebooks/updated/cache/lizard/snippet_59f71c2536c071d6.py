def backlink(node):
    seen = set()
    to_see = [node]
    while to_see:
        node = to_see.pop()
        seen.add(node)
        for succ in node.next:
            succ.prev.add(node)
            if succ not in seen:
                to_see.append(succ)