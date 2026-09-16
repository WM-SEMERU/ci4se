def marshall(self, registry):
    blocks = []
    for i in registry.get_all():
        blocks.append(self.marshall_collector(i))
    blocks = sorted(blocks)
    blocks.append('')
    return self.__class__.LINE_SEPARATOR_FMT.join(blocks)