def snap(self, path=None):
    if path is None:
        path = '/tmp'
    else:
        path = path.rstrip('/')
    day_dir = datetime.datetime.now().strftime('%d%m%Y')
    hour_dir = datetime.datetime.now().strftime('%H%M')
    ensure_snapshot_dir(path + '/' + self.cam_id + '/' + day_dir + '/' +
        hour_dir)
    f_path = '{0}/{1}/{2}/{3}/{4}.jpg'.format(path, self.cam_id, day_dir,
        hour_dir, datetime.datetime.now().strftime('%S'))
    urllib.urlretrieve('http://{0}/snapshot.cgi?user={1}&pwd={2}'.format(
        self.address, self.user, self.pswd), f_path)