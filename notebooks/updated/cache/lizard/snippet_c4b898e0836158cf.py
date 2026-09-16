def score_segmentation(segmentation, table):
    stroke_nr = sum(1 for symbol in segmentation for stroke in symbol)
    score = 1
    for i in range(stroke_nr):
        for j in range(i + 1, stroke_nr):
            qval = q(segmentation, i, j)
            if qval:
                score *= table[i][j]
            else:
                score *= table[j][i]
    return score