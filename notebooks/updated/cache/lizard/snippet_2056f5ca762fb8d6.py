def poll_output(self):
    if self.block:
        return self.output
    new_list = self.output[self.old_output_size:]
    self.old_output_size += len(new_list)
    return new_list