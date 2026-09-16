def make_file_list(upload_path):
    newlist = []
    for el in sorted(os.listdir(upload_path)):
        if ' ' in el:
            raise Exception('Error: Spaces are not allowed in file names!\n')
        newlist.append(os.path.normpath(upload_path + '/' + el))
    debug.log('InputFiles: %s\n' % newlist)
    return newlist