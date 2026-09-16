def _clean_filepath(self, filepath):
    if os.path.isdir(filepath) and os.path.isfile(os.path.join(filepath,
        '__init__.py')):
        filepath = os.path.join(filepath, '__init__.py')
    if not filepath.endswith('.py') and os.path.isfile(filepath + '.py'):
        filepath += '.py'
    return filepath