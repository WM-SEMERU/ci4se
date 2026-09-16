def clean_cornell_movies(filename='cornell_movie_dialogs_corpus.zip',
    subdir='cornell movie-dialogs corpus'):
    fullpath_zipfile = find_filepath(filename)
    dirname = os.path.basename(filename)
    subdir = 'cornell movie-dialogs corpus'
    if fullpath_zipfile.lower().endswith('.zip'):
        retval = unzip(fullpath_zipfile)
        dirname = dirname[:-4]
    fullpath_movie_lines = os.path.join(BIGDATA_PATH, dirname, subdir,
        'movie_lines.txt')
    dialog = pd.read_csv(fullpath_movie_lines, sep='\\+\\+\\+\\$\\+\\+\\+',
        engine='python', header=None, index_col=0)
    dialog.columns = 'user movie person utterance'.split()
    dialog.index.name = 'line'
    dialog.index = [int(s.strip()[1:]) for s in dialog.index.values]
    dialog.sort_index(inplace=True)
    for col in dialog.columns:
        dialog[col] = dialog[col].str.strip()
    return dialog