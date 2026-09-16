def subjects(subjects=None, recursive=False, include_tables=False, lang=
    DEFAULT_LANGUAGE):
    request = Request('subjects', *subjects, recursive=recursive,
        includeTables=include_tables, lang=lang)
    return (Subject(subject, lang=lang) for subject in request.json)