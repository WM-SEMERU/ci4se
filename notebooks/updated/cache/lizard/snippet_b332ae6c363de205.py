def pipe(inpipe, outpipe):
    if hasattr(outpipe, '__pipe__'):
        return outpipe.__pipe__(inpipe)
    elif hasattr(outpipe, '__call__'):
        return outpipe(inpipe)
    else:
        raise BrokenPipe('No connection mechanism defined')