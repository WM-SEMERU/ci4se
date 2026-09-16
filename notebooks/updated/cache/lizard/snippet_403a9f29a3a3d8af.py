def get_agents(self):
    agents_dict = self.get_term_agents()
    agents = [a for a in agents_dict.values() if a is not None]
    return agents