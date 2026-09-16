def get_long_docs(*filenames):
    docs = []
    for filename in filenames:
        with open(filename, 'r') as f:
            docs.append(f.read())
    return '\n\n'.join(docs)