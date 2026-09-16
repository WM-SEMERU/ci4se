def _make_tempy_tag(self, tag, attrs, void):
    tempy_tag_cls = getattr(self.tempy_tags, tag.title(), None)
    if not tempy_tag_cls:
        unknow_maker = [self.unknown_tag_maker, self.unknown_tag_maker.Void][
            void]
        tempy_tag_cls = unknow_maker[tag]
    attrs = {Tag._TO_SPECIALS.get(k, k): (v or True) for k, v in attrs}
    tempy_tag = tempy_tag_cls(**attrs)
    if not self.current_tag:
        self.result.append(tempy_tag)
        if not void:
            self.current_tag = tempy_tag
    elif not tempy_tag._void:
        self.current_tag(tempy_tag)
        self.current_tag = self.current_tag.childs[-1]