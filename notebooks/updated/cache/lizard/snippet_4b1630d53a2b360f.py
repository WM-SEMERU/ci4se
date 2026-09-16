def get_credentials(self, scan_id, target):
    if target:
        for item in self.scans_table[scan_id]['targets']:
            if target == item[0]:
                return item[2]