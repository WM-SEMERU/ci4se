def writefile(filename, content):
    with open(path_expand(filename), 'w') as outfile:
        outfile.write(content)