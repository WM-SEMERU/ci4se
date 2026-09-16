def _assemble_association(stmt):
    member_strs = [_assemble_agent_str(m.concept) for m in stmt.members]
    stmt_str = member_strs[0] + ' is associated with ' + _join_list(member_strs
        [1:])
    return _make_sentence(stmt_str)