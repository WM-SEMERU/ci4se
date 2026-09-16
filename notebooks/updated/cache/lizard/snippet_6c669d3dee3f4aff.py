def uuid(self):
    uuid_file = '/sys/block/%s/dm/uuid' % os.path.basename(os.path.realpath
        (self.volume_path()))
    lv_uuid = open(uuid_file).read().strip()
    if lv_uuid.startswith('LVM-') is True:
        return lv_uuid[4:]
    return lv_uuid