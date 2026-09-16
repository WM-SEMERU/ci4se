def Split(g, *, maxbuffer=10, tuple_len=None):
    if tuple_len is None:
        try:
            tuple_len = g.tuple_len
        except AttributeError:
            raise ValueError(
                "Argument 'tuple_len' must be given since generator is not of type TupleGenerator."
                )
    g_buffered = BufferedTuple(g, maxbuffer=maxbuffer, tuple_len=tuple_len)
    return tuple(NthElementBuffered(g_buffered, i) for i in range(tuple_len))