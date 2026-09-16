def get_files():
    files = dict()
    for k, v in request.files.items():
        content_type = request.files[k
            ].content_type or 'application/octet-stream'
        val = json_safe(v.read(), content_type)
        if files.get(k):
            if not isinstance(files[k], list):
                files[k] = [files[k]]
            files[k].append(val)
        else:
            files[k] = val
    return files