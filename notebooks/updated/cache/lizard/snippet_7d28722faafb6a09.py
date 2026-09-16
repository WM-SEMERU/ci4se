def list_replace(subject_list, replacement, string):
    for s in subject_list:
        string = string.replace(s, replacement)
    return string