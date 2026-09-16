def checkifDownloadExist(self, username, password, download, name):
    try:
        request = urllib2.Request(download)
        base64string = base64.encodestring('%s:%s' % (username, password)
            ).replace('\n', '')
        request.add_header('Authorization', 'Basic %s' % base64string)
        result = urllib2.urlopen(request)
        try:
            f = open(self.zip_dir + '/' + name + '.tgz', 'wb')
            f.close()
            return True
        except urllib2.HTTPError:
            return False
    except urllib2.HTTPError:
        return False