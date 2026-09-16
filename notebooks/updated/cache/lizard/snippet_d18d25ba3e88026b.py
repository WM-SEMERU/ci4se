def verify_space_available(self, search_pattern='(\\d+) \\w+ free'):
    if self.direction == 'put':
        space_avail = self.remote_space_available(search_pattern=search_pattern
            )
    elif self.direction == 'get':
        space_avail = self.local_space_available()
    if space_avail > self.file_size:
        return True
    return False