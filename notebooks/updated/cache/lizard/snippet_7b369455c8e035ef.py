def clean_meta(rst_content):
    rst = rst_content.split('\n')
    for i, line in enumerate(rst):
        if line.startswith('#'):
            continue
        break
    return '\n'.join(rst[i:])