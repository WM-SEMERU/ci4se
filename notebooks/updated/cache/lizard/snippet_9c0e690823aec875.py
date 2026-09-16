def cmd_hasher(f, algorithm):
    data = f.read()
    if not data:
        print('Empty file or string!')
        return 1
    if algorithm:
        print(hasher(data, algorithm)[algorithm], f.name)
    else:
        for algo, result in hasher(data).items():
            print('{:<12} {} {}'.format(algo, result, f.name))