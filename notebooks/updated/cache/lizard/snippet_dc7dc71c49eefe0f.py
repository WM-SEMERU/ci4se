def FindByIndex(node, index):
    result = None
    if isinstance(node.children, dict):
        result = node.GetChild(index)
        if result is None:
            children = list(node.children.keys())
            child = 0
            while child < len(children) and result is None:
                key = children[child]
                result = FindByIndex(node.GetChild(key), index)
                if result is not None:
                    break
                child += 1
    else:
        child = 0
        while child < len(node.children) and result is None:
            result = FindByIndex(node.GetChild(child), index)
            if result is not None:
                break
            child += 1
    return result