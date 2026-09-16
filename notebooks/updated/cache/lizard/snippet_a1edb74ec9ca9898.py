def _replace(self, data, replacements):
    for find, repl in replacements:
        data = data.replace(find, repl)
    return data