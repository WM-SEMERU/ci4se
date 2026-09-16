def delimit_slug(slug, sep=' '):
    hyphenated_slug = re.sub(CRE_SLUG_DELIMITTER, sep, slug)
    return hyphenated_slug