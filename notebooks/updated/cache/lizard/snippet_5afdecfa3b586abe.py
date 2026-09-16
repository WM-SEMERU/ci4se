def total_input_satoshis(self):
    just_inputs = [x['input'] for x in self.ins]
    return sum([x['amount'] for x in just_inputs])