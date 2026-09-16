def getsuffix(subject):
    index = subject.rfind('.')
    if index > subject.replace('\\', '/').rfind('/'):
        return subject[index + 1:]
    return None