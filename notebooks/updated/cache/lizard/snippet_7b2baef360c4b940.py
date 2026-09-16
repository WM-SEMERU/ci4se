def valid_file(cls, filename):
    return not os.path.isdir(filename) and os.path.basename(filename
        ).startswith('Session ') and filename.endswith('.mqo')