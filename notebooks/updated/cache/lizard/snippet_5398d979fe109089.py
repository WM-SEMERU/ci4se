def to_glyphs_master_user_data(self, ufo, master):
    target_user_data = master.userData
    for key, value in ufo.lib.items():
        if _user_data_has_no_special_meaning(key):
            target_user_data[key] = value
    if ufo.data.fileNames:
        from glyphsLib.types import BinaryData
        ufo_data = {}
        for os_filename in ufo.data.fileNames:
            filename = posixpath.join(*os_filename.split(os.path.sep))
            ufo_data[filename] = BinaryData(ufo.data[os_filename])
        master.userData[UFO_DATA_KEY] = ufo_data