def parse_FreqDist_interChr(self, f):
    parsed_data = dict()
    firstline = True
    for l in f['f']:
        if firstline:
            firstline = False
            interChr = float(re.sub('\\)', '', l.split(':')[1]))
        else:
            break
    parsed_data['interChr'] = interChr
    return parsed_data