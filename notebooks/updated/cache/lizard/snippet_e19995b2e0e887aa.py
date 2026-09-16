def copy_path_to_clipboard(i):
    import os
    p = os.getcwd()
    if i.get('add_quotes', '') == 'yes':
        p = '"' + p + '"'
    rx = copy_to_clipboard({'string': p})
    return {'return': 0}