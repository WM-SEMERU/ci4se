def log(message, type):
    (sys.stdout if type == 'notice' else sys.stderr).write(message + '\n')