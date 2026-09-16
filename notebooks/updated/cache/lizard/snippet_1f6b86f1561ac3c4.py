def try_remove(self):
    if self.islink():
        self.unlink()
    elif self.isfile():
        self.remove()
    elif self.isdir():
        self.empty_directory()
        if self.isdir():
            self.rmdir()
    else:
        return False
    return True