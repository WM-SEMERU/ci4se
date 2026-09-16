def interrupt_kernel(self):
    client = self.get_current_client()
    if client is not None:
        self.switch_to_plugin()
        client.stop_button_click_handler()