def spawn_agent(self, agent_definition, location):
    self._should_write_to_command_buffer = True
    self._add_agents(agent_definition)
    command_to_send = SpawnAgentCommand(location, agent_definition.name,
        agent_definition.type)
    self._commands.add_command(command_to_send)