def acquire(self):
    pid_file = os.open(self.pid_filename, os.O_CREAT | os.O_EXCL | os.O_RDWR)
    os.write(pid_file, str(os.getpid()).encode('utf-8'))
    os.close(pid_file)
    if hasattr(os, 'symlink') and platform.system() != 'Windows':
        os.symlink(self.pid_filename, self.lock_filename)
    else:
        self.lock_filename = self.pid_filename