def get_records_with_attachments(attachment_table, rel_object_field=
    'REL_OBJECTID'):
    if arcpyFound == False:
        raise Exception('ArcPy is required to use this function')
    OIDs = []
    with arcpy.da.SearchCursor(attachment_table, [rel_object_field]) as rows:
        for row in rows:
            if not str(row[0]) in OIDs:
                OIDs.append('%s' % str(row[0]))
            del row
    del rows
    return OIDs