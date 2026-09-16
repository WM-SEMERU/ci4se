def print_paired_paths(nb_file, fmt):
    notebook = readf(nb_file, fmt)
    formats = notebook.metadata.get('jupytext', {}).get('formats')
    if formats:
        for path, _ in paired_paths(nb_file, fmt, formats):
            if path != nb_file:
                sys.stdout.write(path + '\n')