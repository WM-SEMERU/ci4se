def ingest(self, co, classname=None, code_objects={}, show_asm=None):
    tokens, customize = scan.Scanner21.ingest(self, co, classname,
        code_objects, show_asm)
    for t in tokens:
        if t.op == self.opc.UNPACK_LIST:
            t.kind = 'UNPACK_LIST_%d' % t.attr
        pass
    return tokens, customize