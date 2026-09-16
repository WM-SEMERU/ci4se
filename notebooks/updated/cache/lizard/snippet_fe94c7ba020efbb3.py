def RegisterTextKey(cls, key, atomid):

    def getter(tags, key):
        return tags[atomid]

    def setter(tags, key, value):
        tags[atomid] = value

    def deleter(tags, key):
        del tags[atomid]
    cls.RegisterKey(key, getter, setter, deleter)