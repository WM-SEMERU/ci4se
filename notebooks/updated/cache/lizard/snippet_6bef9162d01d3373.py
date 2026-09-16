def close(self):
    if self.tabix_file and not self.tabix_file.closed:
        self.tabix_file.close()
    if self.stream:
        self.stream.close()