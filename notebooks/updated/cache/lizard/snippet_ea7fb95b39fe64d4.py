def delete_scan(self, scan_id):
    if self.get_status(scan_id) == ScanStatus.RUNNING:
        return False
    self.scans_table.pop(scan_id)
    if len(self.scans_table) == 0:
        del self.data_manager
        self.data_manager = None
    return True