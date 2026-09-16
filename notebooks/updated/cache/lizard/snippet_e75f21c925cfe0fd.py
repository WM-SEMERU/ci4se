def get_edit_filetypes():
    if os.name == 'nt':
        supported_exts = []
    else:
        try:
            supported_exts = _get_pygments_extensions()
        except Exception:
            supported_exts = []
    favorite_exts = ['.py', '.R', '.jl', '.ipynb', '.md', '.pyw', '.pyx',
        '.c', '.cpp', '.json', '.dat', '.csv', '.tsv', '.txt', '.ini',
        '.html', '.js', '.h', '.bat']
    other_exts = [ext for ext in supported_exts if ext not in favorite_exts]
    all_exts = tuple(favorite_exts + other_exts)
    text_filetypes = _('Supported text files'), all_exts
    return [text_filetypes] + EDIT_FILETYPES