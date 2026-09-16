def file(operation, path):
    operation = operation.lower()
    if operation == 'exists':
        return bool(os.path.isfile(path))
    if operation == 'read':
        with open(path, 'r') as f:
            return [line.strip() for line in f]
    elif operation == 'delete':
        os.remove(path)
    elif operation == 'create':
        open(path, 'w').close()
    elif operation == 'clear':
        open(path, 'w').close()
    else:
        raise ValueError('Invalid operation provided.')