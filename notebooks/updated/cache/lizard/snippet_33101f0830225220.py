def last_modified(self):
    last_modified = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(
        time.time()))
    return last_modified