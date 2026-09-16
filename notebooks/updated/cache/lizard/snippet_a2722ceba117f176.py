def replace_with(self, other):
    match_ids_to_delete = list(self.update_matches(other))
    TextLogErrorMatch.objects.filter(id__in=match_ids_to_delete).delete()
    self.best_for_errors.update(best_classification=other)
    self.delete()