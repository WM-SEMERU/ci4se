def parseProfileLine(fp):
    nextLine = fp.readline()
    if nextLine == None or nextLine == '':
        return None, None
    else:
        pieces = nextLine.strip('\n').split(',')
        return pieces[0], int(pieces[1])