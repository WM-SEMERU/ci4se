def get_obj(self, name):
    val = self.get(name)
    if not val:
        return None
    if name.find('queue') >= 0:
        obj = boto.lookup('sqs', val)
        if obj:
            obj.set_message_class(ServiceMessage)
    elif name.find('bucket') >= 0:
        obj = boto.lookup('s3', val)
    elif name.find('domain') >= 0:
        obj = boto.lookup('sdb', val)
    else:
        obj = None
    return obj