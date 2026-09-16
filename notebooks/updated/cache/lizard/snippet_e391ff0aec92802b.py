def main():
    dir_path = './'
    if '-WD' in sys.argv:
        ind = sys.argv.index('-WD')
        dir_path = sys.argv[ind + 1]
    if '-h' in sys.argv:
        print(main.__doc__)
        sys.exit()
    if '-f' in sys.argv:
        ind = sys.argv.index('-f')
        magic_file = dir_path + '/' + sys.argv[ind + 1]
    else:
        print(main.__doc__)
        sys.exit()
    if '-key' in sys.argv:
        ind = sys.argv.index('-key')
        grab_key = sys.argv[ind + 1]
    else:
        print(main.__doc__)
        sys.exit()
    Data, file_type = pmag.magic_read(magic_file)
    if len(Data) > 0:
        for rec in Data:
            print(rec[grab_key])
    else:
        print('bad file name')