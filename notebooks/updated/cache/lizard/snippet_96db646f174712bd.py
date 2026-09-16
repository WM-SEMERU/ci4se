def Disks(self):
    if not self.disks:
        self.disks = clc.v2.Disks(server=self, disks_lst=self.data[
            'details']['disks'], session=self.session)
    return self.disks