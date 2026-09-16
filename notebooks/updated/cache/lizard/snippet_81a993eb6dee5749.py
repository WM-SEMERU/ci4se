def _cell_output(cell):
    outputs = cell.get('outputs', [])
    stdout = '\n'.join(_ensure_string(output.get('text', '')) for output in
        outputs).rstrip()
    text_outputs = []
    for output in outputs:
        out = output.get('data', {}).get('text/plain', [])
        out = _ensure_string(out)
        if out.startswith('<matplotlib'):
            continue
        text_outputs.append(out)
    return stdout + '\n'.join(text_outputs).rstrip()