def head(line, n: int):
    global counter
    counter += 1
    if counter > n:
        raise cbox.Stop()
    return line