def contrib_xref(contrib_tag, ref_type):
    aff_tags = []
    for child_tag in contrib_tag:
        if (child_tag and child_tag.name and child_tag.name == 'xref' and
            child_tag.get('ref-type') and child_tag.get('ref-type') == ref_type
            ):
            aff_tags.append(child_tag)
    return aff_tags