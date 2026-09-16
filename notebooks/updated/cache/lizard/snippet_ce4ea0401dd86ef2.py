def root_indices(sec_list):
    roots = []
    for i, section in enumerate(sec_list):
        sref = h.SectionRef(sec=section)
        if sref.has_parent() < 0.9:
            roots.append(i)
    return roots