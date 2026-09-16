def p_block(self, p):
    n = len(p)
    if n == 4:
        p[0] = ['block', p[1], p[2], p[3]]
    elif n == 3:
        p[0] = ['block', p[1], [], p[2]]
    else:
        p[0] = ['block', p[1], [], p[1]]
    if self.options.get('lowercasenames'):
        for tag in (1, 3):
            p[0][tag] = p[0][tag].lower()