def get_db(db, ip='localhost', port=27017, user=None, password=None):
    if platform.system().lower() == 'darwin':
        connect = False
    else:
        connect = True
    if user and password:
        import urllib
        pwd = urllib.quote_plus(password)
        uri = 'mongodb://{}:{}@{}:{}'.format(user, pwd, ip, port)
        conn = MongoClient(uri, connect=connect)
    else:
        conn = MongoClient(ip, port, connect=connect)
    return conn[db]