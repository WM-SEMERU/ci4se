def run(self, path, **meta):
    with open(os.devnull, 'w') as devnull:
        sys.stdout = devnull
        if SortImports(path, check=True).incorrectly_sorted:
            return [{'lnum': 0, 'col': 0, 'text':
                'Incorrectly sorted imports.', 'type': 'ISORT'}]
        else:
            return []