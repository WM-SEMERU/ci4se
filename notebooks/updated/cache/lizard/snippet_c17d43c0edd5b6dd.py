def cache_all(self):
    respond = input(
        'By default, cppman fetches pages on-the-fly if corresponding page is not found in the cache. The "cache-all" option is only useful if you want to view man pages offline. Caching all contents will take several minutes, do you want to continue [y/N]? '
        )
    if not (respond and 'yes'.startswith(respond.lower())):
        raise KeyboardInterrupt
    try:
        os.makedirs(environ.cache_dir)
    except:
        pass
    self.success_count = 0
    self.failure_count = 0
    if not os.path.exists(environ.index_db):
        raise RuntimeError("can't find index.db")
    conn = sqlite3.connect(environ.index_db)
    cursor = conn.cursor()
    source = environ.config.source
    print('Caching manpages from %s ...' % source)
    data = cursor.execute('SELECT * FROM "%s"' % source).fetchall()
    for name, url, _ in data:
        print('Caching %s ...' % name)
        retries = 3
        while retries > 0:
            try:
                self.cache_man_page(source, url, name)
            except Exception:
                print('Retrying ...')
                retries -= 1
            else:
                self.success_count += 1
                break
        else:
            print('Error caching %s ...' % name)
            self.failure_count += 1
    conn.close()
    print('\n%d manual pages cached successfully.' % self.success_count)
    print('%d manual pages failed to cache.' % self.failure_count)
    self.update_mandb(False)