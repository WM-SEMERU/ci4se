def enter_scope(self, funcname):
    old_mangle = self.mangle
    self.mangle = '%s%s%s' % (self.mangle, global_.MANGLE_CHR, funcname)
    self.table.append(SymbolTable.Scope(self.mangle, parent_mangle=old_mangle))
    global_.META_LOOPS.append(global_.LOOPS)
    global_.LOOPS = []