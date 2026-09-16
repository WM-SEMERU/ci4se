def process_f2pydoc(f2pydoc):
    docparts = re.split('\n--', f2pydoc)
    if len(docparts) == 4:
        doc_has_optionals = True
    elif len(docparts) == 3:
        doc_has_optionals = False
    else:
        print('-- uninterpretable f2py documentation --')
        return f2pydoc
    docparts[0] = re.sub('[\\[(,]\\w+_d\\d', '', docparts[0])
    if doc_has_optionals:
        returnarray_dims = re.findall('[\\[(,](\\w+_d\\d)', docparts[3])
        for arg in returnarray_dims:
            searchpattern = arg + ' : input.*\n.*Default: (.*)\n'
            match = re.search(searchpattern, docparts[2])
            if match:
                default = match.group(1)
                docparts[3] = re.sub(arg, default, docparts[3])
                docparts[2] = re.sub(searchpattern, '', docparts[2])
    if doc_has_optionals:
        searchpattern = '\\w+_d\\d : input.*\n.*Default: (.*)\n'
        docparts[2] = re.sub(searchpattern, '', docparts[2])
    processed_signature = '\n--'.join(docparts)
    return processed_signature