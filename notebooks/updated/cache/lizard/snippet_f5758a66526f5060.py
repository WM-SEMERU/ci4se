def write(self, destination, filename, content):
    if not os.path.exists(destination):
        try:
            os.makedirs(destination)
        except:
            pass
    filepath = '%s/%s' % (destination, filename)
    f = open(filepath, 'w+')
    f.write(content)
    f.close()