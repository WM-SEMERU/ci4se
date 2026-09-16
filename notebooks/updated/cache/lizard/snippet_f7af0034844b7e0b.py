def to_glyphs_family_user_data_from_designspace(self):
    target_user_data = self.font.userData
    for key, value in self.designspace.lib.items():
        if (key == UFO2FT_FEATURE_WRITERS_KEY and value ==
            DEFAULT_FEATURE_WRITERS):
            continue
        if _user_data_has_no_special_meaning(key):
            target_user_data[key] = value