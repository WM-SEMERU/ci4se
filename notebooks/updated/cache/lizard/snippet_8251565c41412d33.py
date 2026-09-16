def is_safe(self):
    self.log('Checking if this container is safe')
    for entry in self.entries:
        if not self.is_entry_safe(entry):
            self.log(["This container is not safe: found unsafe entry '%s'",
                entry])
            return False
    self.log('This container is safe')
    return True