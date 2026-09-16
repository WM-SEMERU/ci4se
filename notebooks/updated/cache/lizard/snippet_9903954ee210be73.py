def save_to_file(filename, content):
    import os.path
    path = os.path.abspath(filename)
    with open(path, 'w') as text_file:
        text_file.write('{}'.format(content))