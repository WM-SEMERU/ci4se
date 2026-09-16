def get_time_slide_id(xmldoc, time_slide, create_new=None, superset_ok=
    False, nonunique_ok=False):
    try:
        tisitable = lsctables.TimeSlideTable.get_table(xmldoc)
    except ValueError:
        if create_new is None:
            raise
        tisitable = lsctables.New(lsctables.TimeSlideTable)
        xmldoc.childNodes[0].appendChild(tisitable)
    tisitable.sync_next_id()
    return tisitable.get_time_slide_id(time_slide, create_new=create_new,
        superset_ok=superset_ok, nonunique_ok=nonunique_ok)