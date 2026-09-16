def setup_icons(self):
    folder_icon = get_icon('glyphicons_144_folder_open.png', asicon=True)
    self.asset_open_pb.setIcon(folder_icon)
    self.shot_open_pb.setIcon(folder_icon)
    floppy_icon = get_icon('glyphicons_446_floppy_save.png', asicon=True)
    self.asset_save_pb.setIcon(floppy_icon)
    self.shot_save_pb.setIcon(floppy_icon)