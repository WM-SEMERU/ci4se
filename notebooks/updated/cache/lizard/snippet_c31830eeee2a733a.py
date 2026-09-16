def _close_generator(g):
    if isinstance(g, generatorwrapper):
        g.close()
    elif _get_frame(g) is not None:
        try:
            g.throw(GeneratorExit_)
        except (StopIteration, GeneratorExit_):
            return
        else:
            raise RuntimeError('coroutine ignored GeneratorExit')