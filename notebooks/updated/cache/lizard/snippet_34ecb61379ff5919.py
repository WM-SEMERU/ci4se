def get_via_name_list(src, name_parts):
    if len(name_parts) > 1:
        for part in name_parts[:-1]:
            if part not in src:
                return None
            src = src[part]
    return src.get(name_parts[-1])