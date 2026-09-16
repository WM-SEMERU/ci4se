def create(self):
    if os.path.isfile(self.path):
        if not os.path.exists(self.path):
            with open(self.path, 'w') as fileobj:
                fileobj.write('')
    else:
        os.makedirs(self.path)