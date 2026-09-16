def split_pieces(piece_list, segments, num):
    piece_groups = []
    pieces = list(piece_list)
    while pieces:
        for i in range(segments):
            p = pieces[i::segments][:num]
            if not p:
                break
            piece_groups.append(p)
        pieces = pieces[num * segments:]
    return piece_groups