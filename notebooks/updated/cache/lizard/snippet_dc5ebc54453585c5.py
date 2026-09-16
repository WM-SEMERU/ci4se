def resolve_path(file_path, calling_function):
    if not file_path:
        resolved = os.path.join(os.getcwd(), calling_function)
    elif file_path.count(os.sep) == 0:
        resolved = os.path.join(os.getcwd(), file_path)
    else:
        resolved = file_path
    if not resolved.endswith('.csv'):
        resolved = resolved + '.csv'
    return resolved