def unsafe_peek(init):

    def peek(store, container, _stack=None):
        return init(*[store.peek(attr, container, _stack=_stack) for attr in
            container])
    return peek