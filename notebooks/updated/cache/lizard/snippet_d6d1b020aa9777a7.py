def find_volume(self, name):
    try:
        return Volume(self.virsp.storageVolLookupByName(name), self)
    except libvirtError:
        return None