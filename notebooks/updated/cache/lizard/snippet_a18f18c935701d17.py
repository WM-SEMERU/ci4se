def count_word(arg):
    conn = sqlite3.connect(os.path.join(DEFAULT_PATH, 'word.db'))
    curs = conn.cursor()
    if arg[0].isdigit():
        if len(arg) == 1:
            curs.execute('SELECT count(*) FROM Word WHERE pr ==  %d' % int(
                arg[0]))
        elif len(arg) == 2 and arg[1] == '+':
            curs.execute('SELECT count(*) FROM Word WHERE pr >=  %d' % int(
                arg[0]))
        elif len(arg) == 3 and arg[1] == '-':
            curs.execute(
                'SELECT count(*) FROM Word WHERE pr >=  %d AND pr<=  % d' %
                (int(arg[0]), int(arg[2])))
    elif arg[0].isalpha():
        if arg == 'all':
            curs.execute('SELECT count(*) FROM Word')
        elif len(arg) == 1:
            curs.execute('SELECT count(*) FROM Word WHERE aset == "%s"' %
                arg.upper())
    res = curs.fetchall()
    print(res[0][0])
    curs.close()
    conn.close()