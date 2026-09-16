def _assemble_complex(stmt):
    member_strs = [_assemble_agent_str(m) for m in stmt.members]
    stmt_str = member_strs[0] + ' binds ' + _join_list(member_strs[1:])
    return _make_sentence(stmt_str)