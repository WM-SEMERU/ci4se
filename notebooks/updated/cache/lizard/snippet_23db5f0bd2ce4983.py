def _assemble_translocation(stmt):
    agent_str = _assemble_agent_str(stmt.agent)
    stmt_str = agent_str + ' translocates'
    if stmt.from_location is not None:
        stmt_str += ' from the ' + stmt.from_location
    if stmt.to_location is not None:
        stmt_str += ' to the ' + stmt.to_location
    return _make_sentence(stmt_str)