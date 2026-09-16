def _get_files_modified():
    cmd = 'git diff-index --cached --name-only --diff-filter=ACMRTUXB HEAD'
    _, files_modified, _ = run(cmd)
    extensions = [re.escape(ext) for ext in list(SUPPORTED_FILES) + ['.rst']]
    test = '(?:{0})$'.format('|'.join(extensions))
    return list(filter(lambda f: re.search(test, f), files_modified))