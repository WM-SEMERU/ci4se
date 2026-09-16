def notebook_to_md(notebook):
    tmp_file = tempfile.NamedTemporaryFile(delete=False)
    tmp_file.write(ipynb_writes(notebook).encode('utf-8'))
    tmp_file.close()
    pandoc(
        '--from ipynb --to markdown -s --atx-headers --wrap=preserve --preserve-tabs'
        , tmp_file.name, tmp_file.name)
    with open(tmp_file.name, encoding='utf-8') as opened_file:
        text = opened_file.read()
    os.unlink(tmp_file.name)
    return '\n'.join(text.splitlines())