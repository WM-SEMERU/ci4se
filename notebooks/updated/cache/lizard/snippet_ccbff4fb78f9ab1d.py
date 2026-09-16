def get_disks(self):
    disks = [disk for disk in self.xml.iter('disk')]
    disk_objs = []
    for disk in disks:
        source = disk.find('source')
        if source is None:
            continue
        path = source.attrib['file']
        diskobj = self.domain.connect().storageVolLookupByPath(path)
        disk_objs.append(diskobj)
    return [Volume(d, StoragePool(d.storagePoolLookupByVolume())) for d in
        disk_objs]