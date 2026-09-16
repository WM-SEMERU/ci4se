def get_simple_split(branchfile):
    index = branchfile.find('/')
    if index == -1:
        return None, None
    branch, file = branchfile.split('/', 1)
    return branch, file