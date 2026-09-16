def _assemble_modification(stmt):
    sub_str = _assemble_agent_str(stmt.sub)
    if stmt.enz is not None:
        enz_str = _assemble_agent_str(stmt.enz)
        if _get_is_direct(stmt):
            mod_str = ' ' + _mod_process_verb(stmt) + ' '
        else:
            mod_str = ' leads to the ' + _mod_process_noun(stmt) + ' of '
        stmt_str = enz_str + mod_str + sub_str
    else:
        stmt_str = sub_str + ' is ' + _mod_state_stmt(stmt)
    if stmt.residue is not None:
        if stmt.position is None:
            mod_str = 'on ' + ist.amino_acids[stmt.residue]['full_name']
        else:
            mod_str = 'on ' + stmt.residue + stmt.position
    else:
        mod_str = ''
    stmt_str += ' ' + mod_str
    return _make_sentence(stmt_str)