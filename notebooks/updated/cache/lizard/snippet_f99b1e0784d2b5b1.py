def sort_nodes(dom, cmp_func):
    dom.normalize()
    for node in list(walk_dom(dom, elements_only=True)):
        prev_sib = node.previousSibling
        while prev_sib and cmp_func(prev_sib, node) == 1:
            node.parentNode.insertBefore(node, prev_sib)
            prev_sib = node.previousSibling