def all_on_off(self, power):
    send_msg = self.create_send_message(
        'F0 7F 00 7F 00 00 @kk 05 02 02 00 00 F1 22 00 00 @pr 00 00 01',
        None, None, power)
    self.send_data(send_msg)
    self.get_response_message()