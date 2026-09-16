def get_gradebook_column_summary(self, gradebook_column_id):
    gradebook_column = self.get_gradebook_column(gradebook_column_id)
    summary_map = gradebook_column._my_map
    summary_map['gradebookColumnId'] = str(gradebook_column.ident)
    return GradebookColumnSummary(osid_object_map=summary_map, runtime=self
        ._runtime, proxy=self._proxy)