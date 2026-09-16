def _remove_media(self, directory, files=None):
    if not self._connectToFlickr():
        logger.error("%s - Couldn't connect to flickr")
        return False
    db = self._loadDB(directory)
    if not files:
        files = db.keys()
    if isinstance(files, basestring):
        files = [files]
    for fn in files:
        print('%s - Deleting from flickr [local copy intact]' % fn)
        try:
            pid = db[fn]['photoid']
        except:
            logger.debug('%s - Was never in flickr DB' % fn)
            continue
        resp = self.flickr.photos_delete(photo_id=pid, format='etree')
        if resp.attrib['stat'] != 'ok':
            print('%s - flickr: delete failed with status: %s', resp.attrib
                ['stat'])
            return False
        else:
            logger.debug('Removing %s from flickr DB' % fn)
            del db[fn]
            self._saveDB(directory, db)
    return True