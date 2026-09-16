def _assemble_active_form(self, stmt):
    act_agent = Agent(stmt.agent.name, db_refs=stmt.agent.db_refs)
    act_agent.activity = ActivityCondition(stmt.activity, True)
    activates = stmt.is_active
    relation = get_causal_edge(stmt, activates)
    self._add_nodes_edges(stmt.agent, act_agent, relation, stmt.evidence)