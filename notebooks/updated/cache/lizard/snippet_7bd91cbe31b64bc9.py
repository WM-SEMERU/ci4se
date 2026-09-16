def trt2i(self):
    trts = sorted(set(src_group.trt for sm in self.source_models for
        src_group in sm.src_groups))
    return {trt: i for i, trt in enumerate(trts)}