def setup_network_agents(self):
    for i in self.env.G.nodes():
        self.env.G.node[i]['agent'] = self.agent_type(environment=self.env,
            agent_id=i, state=deepcopy(self.initial_states[i]))