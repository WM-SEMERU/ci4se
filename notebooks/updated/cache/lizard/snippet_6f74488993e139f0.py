def _calendar_classes_for_occurrence(self, occurrence):
    classes = [slugify(occurrence.event.polymorphic_ctype.name)]
    if occurrence.is_all_day:
        classes.append('is-all-day')
    if occurrence.is_protected_from_regeneration:
        classes.append('is-user-modified')
    if occurrence.is_cancelled:
        classes.append('is-cancelled')
    if not occurrence.event.show_in_calendar:
        classes.append('do-not-show-in-calendar')
    classes = [('fcc-%s' % class_) for class_ in classes]
    return classes