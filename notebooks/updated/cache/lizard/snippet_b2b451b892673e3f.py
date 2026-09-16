def traverse_inorder(self, leaves=True, internal=True):
    c = self
    s = deque()
    done = False
    while not done:
        if c is None:
            if len(s) == 0:
                done = True
            else:
                c = s.pop()
                if leaves and c.is_leaf() or internal and not c.is_leaf():
                    yield c
                if len(c.children) == 0:
                    c = None
                elif len(c.children) == 2:
                    c = c.children[1]
                else:
                    raise RuntimeError(INORDER_NONBINARY)
        else:
            s.append(c)
            if len(c.children) == 0:
                c = None
            elif len(c.children) == 2:
                c = c.children[0]
            else:
                raise RuntimeError(INORDER_NONBINARY)