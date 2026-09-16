def get_subject(self, text):
    first_line = text.splitlines(True)[0]
    if first_line.startswith('SUBJECT:'):
        subject = first_line[len('SUBJECT:'):]
    else:
        subject = first_line
    return subject.strip()