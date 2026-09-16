def extract_object_names_from_docs(filename):
    text = split_code_and_text_blocks(filename)[1]
    text = '\n'.join(t[1] for t in text if t[0] == 'text')
    regex = re.compile(
        ':(?:func(?:tion)?|meth(?:od)?|attr(?:ibute)?|obj(?:ect)?|class):`(\\S*)`'
        )
    return [(x, x) for x in re.findall(regex, text)]