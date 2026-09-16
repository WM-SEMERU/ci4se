def find_ss_regions(dssp_residues, loop_assignments=(' ', 'B', 'S', 'T')):
    loops = loop_assignments
    previous_ele = None
    fragment = []
    fragments = []
    for ele in dssp_residues:
        if previous_ele is None:
            fragment.append(ele)
        elif ele[2] != previous_ele[2]:
            fragments.append(fragment)
            fragment = [ele]
        elif previous_ele[1] in loops:
            if ele[1] in loops:
                fragment.append(ele)
            else:
                fragments.append(fragment)
                fragment = [ele]
        elif ele[1] == previous_ele[1]:
            fragment.append(ele)
        else:
            fragments.append(fragment)
            fragment = [ele]
        previous_ele = ele
    fragments.append(fragment)
    return fragments