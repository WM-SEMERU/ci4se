def GetVersion():
    with open(os.path.join('googleads', 'common.py')) as versions_file:
        source = versions_file.read()
    return re.search("\\nVERSION = '(.*?)'", source).group(1)