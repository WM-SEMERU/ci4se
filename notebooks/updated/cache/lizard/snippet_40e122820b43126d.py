def setup_icons(self):
    folder_icon = get_icon('glyphicons_144_folder_open.png', asicon=True)
    self.asset_open_path_tb.setIcon(folder_icon)
    self.shot_open_path_tb.setIcon(folder_icon)
    current_icon = get_icon('glyphicons_181_download_alt.png', asicon=True)
    self.current_pb.setIcon(current_icon)
    refresh_icon = get_icon('refresh.png', asicon=True)
    self.refresh_tb.setIcon(refresh_icon)