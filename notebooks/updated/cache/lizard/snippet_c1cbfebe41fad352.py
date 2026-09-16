def git_tag2eups_tag(git_tag):
    eups_tag = git_tag
    if re.match('\\d', eups_tag):
        eups_tag = 'v{eups_tag}'.format(eups_tag=eups_tag)
    eups_tag = eups_tag.translate(str.maketrans('.-', '__'))
    return eups_tag