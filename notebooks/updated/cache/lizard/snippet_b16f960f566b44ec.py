def is_tomodir(subdirectories):
    required = 'exe', 'config', 'rho', 'mod', 'inv'
    is_tomodir = True
    for subdir in required:
        if subdir not in subdirectories:
            is_tomodir = False
    return is_tomodir