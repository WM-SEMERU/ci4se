def removeText(self, text):
    removedBlock = None
    blocks = self.blocks
    for i in range(len(blocks)):
        block = blocks[i]
        if issubclass(block.__class__, AdvancedTag):
            continue
        if text in block:
            removedBlock = block[:]
            blocks[i] = block.replace(text, '')
            break
    self.text = ''.join([thisBlock for thisBlock in blocks if not
        issubclass(thisBlock.__class__, AdvancedTag)])
    return removedBlock