def stack_call(self, *args):
    self.pipelined_args.append(args)
    self.number_of_stacked_calls = self.number_of_stacked_calls + 1