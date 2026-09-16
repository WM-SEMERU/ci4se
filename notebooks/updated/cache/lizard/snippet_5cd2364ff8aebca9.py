def parse_cmu(cmufh):
    pronunciations = list()
    for line in cmufh:
        line = line.strip().decode('utf-8')
        if line.startswith(';'):
            continue
        word, phones = line.split(' ', 1)
        pronunciations.append((word.split('(', 1)[0].lower(), phones))
    return pronunciations