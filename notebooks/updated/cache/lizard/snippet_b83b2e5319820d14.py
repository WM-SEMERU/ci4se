def set_subprocess_arguments(self, subprocess_arguments):
    self.subprocess_arguments = subprocess_arguments
    self.log(['Subprocess arguments: %s', subprocess_arguments])