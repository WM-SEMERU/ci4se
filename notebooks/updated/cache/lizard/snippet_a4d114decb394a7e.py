def display_stats(self):
    for i, one_stage in enumerate(STAGE_NAME):
        second_in_stage = self.annot.time_in_stage(one_stage)
        time_in_stage = str(timedelta(seconds=second_in_stage))
        label = self.idx_stage_stats.itemAt(i, QFormLayout.FieldRole).widget()
        label.setText(time_in_stage)
    for i, one_qual in enumerate(QUALIFIERS):
        second_in_qual = self.annot.time_in_stage(one_qual, attr='quality')
        time_in_qual = str(timedelta(seconds=second_in_qual))
        label = self.idx_qual_stats.itemAt(i, QFormLayout.FieldRole).widget()
        label.setText(time_in_qual)