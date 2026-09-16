def _AddUnicodeMethod(unused_message_descriptor, cls):

    def __unicode__(self):
        return text_format.MessageToString(self, as_utf8=True).decode('utf-8')
    cls.__unicode__ = __unicode__