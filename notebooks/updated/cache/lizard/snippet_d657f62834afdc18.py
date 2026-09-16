def reduce(self, body):
    i = 0
    while i < len(body):
        stmnt = body[i]
        if self.visit(stmnt):
            body.pop(i)
        else:
            i += 1