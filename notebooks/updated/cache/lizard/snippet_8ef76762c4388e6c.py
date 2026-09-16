def main():
    notebook = {'cells': [{'cell_type': 'markdown', 'metadata': {},
        'source': ["""# cvloop functions

""",
        'This notebook shows an overview over all cvloop ',
        'functions provided in the [`cvloop.functions` module](',
        'https://github.com/shoeffner/cvloop/blob/',
        'develop/cvloop/functions.py).']}], 'nbformat': 4, 'nbformat_minor':
        1, 'metadata': {'language_info': {'codemirror_mode': {'name':
        'ipython', 'version': 3}, 'file_extension': '.py', 'mimetype':
        'text/x-python', 'name': 'python', 'nbconvert_exporter': 'python',
        'pygments_lexer': 'ipython3', 'version': '3.5.1+'}}}
    classes = list_classes('cvloop.functions')
    functions = list_functions('cvloop.functions')
    line_numbers_cls = get_linenumbers(classes, cvloop.functions, 'class {}:\n'
        )
    line_numbers = get_linenumbers(functions, cvloop.functions)
    for cls in classes:
        line_number = line_numbers_cls[cls]
        notebook['cells'].append(create_description_cell(cls, line_number))
        notebook['cells'].append(create_code_cell(cls, isclass=True))
    for func in functions:
        line_number = line_numbers[func]
        notebook['cells'].append(create_description_cell(func, line_number))
        notebook['cells'].append(create_code_cell(func))
    with open(sys.argv[1], 'w') as nfile:
        json.dump(notebook, nfile, indent=4)