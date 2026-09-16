def get_agents(self, addr=True, agent_cls=None, include_manager=False):
    agents = list(self.agents.dict.values())
    if hasattr(self, 'manager') and self.manager is not None:
        if not include_manager:
            agents = [a for a in agents if a.addr.rsplit('/', 1)[1] != '0']
    if agent_cls is not None:
        agents = [a for a in agents if type(a) is agent_cls]
    if addr:
        agents = [agent.addr for agent in agents]
    return agents