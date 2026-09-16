def run(self):
    if self.debug:
        print('Starting ' + self.name)
    if isinstance(self.function, str):
        globals()[self.function](*self.args, **self.kwargs)
    else:
        self.function(*self.args, **self.kwargs)
    if self.debug:
        print('Exiting ' + self.name)