def get_file_path(dotted_path, extension='json'):
    if os.sep in dotted_path or '/' in dotted_path:
        return dotted_path
    parts = dotted_path.split('.')
    if parts[0] == 'chatterbot':
        parts.pop(0)
        parts[0] = DATA_DIRECTORY
    corpus_path = os.path.join(*parts)
    if os.path.exists(corpus_path + '.{}'.format(extension)):
        corpus_path += '.{}'.format(extension)
    return corpus_path