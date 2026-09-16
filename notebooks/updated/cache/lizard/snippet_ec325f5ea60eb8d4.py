def _core_properties_part(self):
    try:
        return self.part_related_by(RT.CORE_PROPERTIES)
    except KeyError:
        core_properties_part = CorePropertiesPart.default(self)
        self.relate_to(core_properties_part, RT.CORE_PROPERTIES)
        return core_properties_part