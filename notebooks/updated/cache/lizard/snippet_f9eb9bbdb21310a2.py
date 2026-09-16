def all_agents(stmts):
    agents = []
    for stmt in stmts:
        for agent in stmt.agent_list():
            if agent is not None and agent.db_refs.get('TEXT') is not None:
                agents.append(agent)
    return agents