def to_glyphs_kerning(self):
    for master_id, source in self._sources.items():
        for (left, right), value in source.font.kerning.items():
            left_match = UFO_KERN_GROUP_PATTERN.match(left)
            right_match = UFO_KERN_GROUP_PATTERN.match(right)
            if left_match:
                left = '@MMK_L_{}'.format(left_match.group(2))
            if right_match:
                right = '@MMK_R_{}'.format(right_match.group(2))
            self.font.setKerningForPair(master_id, left, right, value)