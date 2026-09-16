def upload(self, filename, number_of_hosts):
    return self.multiupload(filename, self.random_hosts(number_of_hosts))