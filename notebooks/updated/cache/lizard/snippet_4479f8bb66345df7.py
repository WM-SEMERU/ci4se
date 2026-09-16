def get_python_files(files):
    python_files = []
    for file_name in files:
        if file_name.endswith('.py'):
            python_files.append(file_name)
    return python_files