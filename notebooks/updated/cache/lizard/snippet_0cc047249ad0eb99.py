def relative_path(reference_path, input_path):
    start_path = os.path.dirname(reference_path)
    try:
        relative_path = os.path.relpath(input_path, start_path)
    except ValueError:
        relative_path = input_path
    return relative_path