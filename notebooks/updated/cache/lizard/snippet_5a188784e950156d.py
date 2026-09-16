def _build_stack(self):
    return self._stack_from_spec(ansible_mitogen.transport_config.
        PlayContextSpec(connection=self, play_context=self._play_context,
        transport=self.transport, inventory_name=self.inventory_hostname))