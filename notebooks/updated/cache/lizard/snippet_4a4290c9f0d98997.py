def portCnt(port):
    if port.children:
        return sum(map(lambda p: portCnt(p), port.children))
    else:
        return 1