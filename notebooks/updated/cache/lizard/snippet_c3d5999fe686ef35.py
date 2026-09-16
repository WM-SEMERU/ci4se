def git_hash(blob):
    head = str('blob ' + str(len(blob)) + '\x00').encode('utf-8')
    return sha1(head + blob).hexdigest()