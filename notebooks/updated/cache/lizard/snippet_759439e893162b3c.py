def has_xor(self):

    def _has_xor(expr):
        return isinstance(expr, pyvex.IRExpr.Binop) and expr.op.startswith(
            'Iop_Xor')
    found_xor = False
    for block in self._function.blocks:
        if block.size == 0:
            continue
        for stmt in block.vex.statements:
            if isinstance(stmt, pyvex.IRStmt.Put):
                found_xor = found_xor or _has_xor(stmt.data)
            elif isinstance(stmt, pyvex.IRStmt.WrTmp):
                found_xor = found_xor or _has_xor(stmt.data)
        if found_xor:
            break
    if found_xor:
        return {CodeTags.HAS_XOR}
    return None