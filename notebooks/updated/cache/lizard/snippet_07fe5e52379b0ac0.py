def by(self, technology):
    if technology == PluginTechnology.LV2 or str(technology).upper(
        ) == PluginTechnology.LV2.value.upper():
        return self.lv2_builder.all
    else:
        return []