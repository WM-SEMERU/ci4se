def assignLeafRegisters(inodes, registerMaker):
    leafRegisters = {}
    for node in inodes:
        key = node.key()
        if key in leafRegisters:
            node.reg = leafRegisters[key]
        else:
            node.reg = leafRegisters[key] = registerMaker(node)