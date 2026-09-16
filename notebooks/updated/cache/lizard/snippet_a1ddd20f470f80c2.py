def write_data(self):
    self.output_file.write(self.downloaded_file_buffer)
    self.output_file.close()
    self.finished_flag = True