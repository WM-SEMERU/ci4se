def check_overlap(pos, ins, thresh):
    ins_pos = ins[0]
    ins_len = ins[2]
    ol = overlap(ins_pos, pos)
    feat_len = pos[1] - pos[0] + 1
    if float(ol) / float(feat_len) >= thresh:
        return True
    return False