def create_node(self, network, participant):
    if network.role == 'practice' or network.role == 'catch':
        return RogersAgentFounder(network=network, participant=participant)
    elif network.size(type=Agent) < network.generation_size:
        return RogersAgentFounder(network=network, participant=participant)
    else:
        return RogersAgent(network=network, participant=participant)