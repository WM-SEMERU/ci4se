def list_corpus_files(dotted_path):
    corpus_path = get_file_path(dotted_path, extension=CORPUS_EXTENSION)
    paths = []
    if os.path.isdir(corpus_path):
        paths = glob.glob(corpus_path + '/**/*.' + CORPUS_EXTENSION,
            recursive=True)
    else:
        paths.append(corpus_path)
    paths.sort()
    return paths