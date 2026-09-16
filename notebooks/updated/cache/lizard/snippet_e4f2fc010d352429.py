def comicDownloaded(self, comic, filename, text=None):
    imageUrl = self.getUrlFromFilename(filename)
    size = None
    if self.allowdownscale:
        size = getDimensionForImage(filename, MaxImageSize)
    title = '%s - %s' % (comic.name, os.path.basename(filename))
    pageUrl = comic.referrer
    description = '<img src="%s"' % imageUrl
    if size:
        description += ' width="%d" height="%d"' % size
    description += '/>'
    if text:
        description += '<br/>%s' % text
    description += '<br/><a href="%s">View Comic Online</a>' % pageUrl
    args = title, imageUrl, description, util.rfc822date(time.time())
    if self.newfile:
        self.newfile = False
        self.rss.addItem(*args)
    else:
        self.rss.addItem(*args, append=False)