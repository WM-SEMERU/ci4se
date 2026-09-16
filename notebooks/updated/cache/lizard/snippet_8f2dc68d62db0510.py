def add_preset(self, name=None, desc=None, note=None, opts=SoSOptions()):
    presets_path = self.presets_path
    if not name:
        raise ValueError('Preset name cannot be empty')
    if name in self.presets.keys():
        raise ValueError("A preset with name '%s' already exists" % name)
    preset = PresetDefaults(name=name, desc=desc, note=note, opts=opts)
    preset.builtin = False
    self.presets[preset.name] = preset
    preset.write(presets_path)