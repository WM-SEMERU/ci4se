def unreserve_resources(role):
    state = dcos_agents_state()
    if not state or 'slaves' not in state.keys():
        return False
    all_success = True
    for agent in state['slaves']:
        if not unreserve_resource(agent, role):
            all_success = False
    return all_success