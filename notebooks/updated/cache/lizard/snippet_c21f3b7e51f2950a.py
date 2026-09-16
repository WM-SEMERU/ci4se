def output_callback(self, out, process_status):
    self.final_status.append(process_status)
    self.final_output.append(out)