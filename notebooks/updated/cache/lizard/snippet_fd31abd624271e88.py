def on_unaryop(self, node):
    return op2func(node.op)(self.run(node.operand))