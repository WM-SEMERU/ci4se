def today(boo):
    tod = datetime.strptime(datetime.today().date().isoformat().replace('-',
        ' '), '%Y %m %d')
    if boo:
        return int(str(tod).replace('-', '')[:8])
    else:
        return str(tod)[:10]