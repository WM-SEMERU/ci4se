def sort_by_name(self):
    super(JSSObjectList, self).sort(key=lambda k: k.name)