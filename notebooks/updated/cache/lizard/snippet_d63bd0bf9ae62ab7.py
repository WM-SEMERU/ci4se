def update_execution_state_kernel(self):
    client = self.get_current_client()
    if client is not None:
        executing = client.stop_button.isEnabled()
        self.interrupt_action.setEnabled(executing)