def get_num_ruptures(self):
    return {grp.id: sum(src.num_ruptures for src in grp) for grp in self.
        src_groups}