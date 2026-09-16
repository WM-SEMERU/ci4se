def update_eff_ruptures(self, count_ruptures):
    for smodel in self.source_models:
        for sg in smodel.src_groups:
            sg.eff_ruptures = count_ruptures(sg.id) if callable(count_ruptures
                ) else count_ruptures.get(sg.id, 0)