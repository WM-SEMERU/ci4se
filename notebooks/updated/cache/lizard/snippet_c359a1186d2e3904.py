def get_exclusions(path):
    if not os.path.isdir(path):
        return None
    dockerignore_file = os.path.join(path, '.dockerignore')
    if not os.path.isfile(dockerignore_file):
        return None
    with open(dockerignore_file, 'rb') as dif:
        return list(preprocess_matches(dif.readlines()))