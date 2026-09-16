def get_description_from_docstring(cls, obj):
    doc = obj.__doc__ or ''
    p = doc.find('\n')
    if p == -1:
        return doc, []
    else:
        description = doc[:p]
        details = textwrap.dedent(doc[p + 1:]).splitlines()
        while details and not details[0].strip():
            details = details[1:]
        while details and not details[-1].strip():
            details.pop()
        recording = True
        details_without_params = []
        for detail_line in details:
            if ':param' in detail_line:
                recording = False
            if not detail_line.strip():
                recording = True
            if recording:
                details_without_params.append(detail_line)
        return description, details_without_params