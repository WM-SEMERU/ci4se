def extract_statement_from_query_result(self, res):
    agent_start, agent_end, affected_start, affected_end = res
    agent_start = int(agent_start)
    agent_end = int(agent_end)
    affected_start = int(affected_start)
    affected_end = int(affected_end)
    agent = self.text[agent_start:agent_end]
    affected = self.text[affected_start:affected_end]
    agent = agent.lstrip().rstrip()
    affected = affected.lstrip().rstrip()
    subj = Agent(agent, db_refs={'TEXT': agent})
    obj = Agent(affected, db_refs={'TEXT': affected})
    statement = Influence(subj=subj, obj=obj)
    self.statements.append(statement)