def use_in(ContentHandler):

    def startStream(self, parent, attrs, __orig_startStream=ContentHandler.
        startStream):
        if parent.tagName == ligolw.Array.tagName:
            return ArrayStream(attrs).config(parent)
        return __orig_startStream(self, parent, attrs)

    def startArray(self, parent, attrs):
        return Array(attrs)
    ContentHandler.startStream = startStream
    ContentHandler.startArray = startArray
    return ContentHandler