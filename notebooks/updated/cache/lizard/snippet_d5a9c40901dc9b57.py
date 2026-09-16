def constant_action(self, text, loc, const):
    exshared.setpos(loc, text)
    if DEBUG > 0:
        print('CONST:', const)
        if DEBUG == 2:
            self.symtab.display()
        if DEBUG > 2:
            return
    return self.symtab.insert_constant(const[0], const[1])