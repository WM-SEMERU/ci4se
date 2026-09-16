def avl_new_top(t1, t2, top, direction=0):
    top.parent = None
    assert top.parent is None, str(top.parent.value)
    top.set_child(direction, t1)
    top.set_child(1 - direction, t2)
    top.balance = max(height(t1), height(t2)) + 1
    return top