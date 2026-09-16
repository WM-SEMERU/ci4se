def convert_to_mosek_matrix(sdp):
    barci = []
    barcj = []
    barcval = []
    barai = []
    baraj = []
    baraval = []
    for k in range(sdp.n_vars):
        barai.append([])
        baraj.append([])
        baraval.append([])
    row_offsets = [0]
    block_offsets = [0]
    cumulative_sum = 0
    cumulative_square_sum = 0
    for block_size in sdp.block_struct:
        cumulative_sum += block_size
        cumulative_square_sum += block_size ** 2
        row_offsets.append(cumulative_square_sum)
        block_offsets.append(cumulative_sum)
    for row in range(len(sdp.F.rows)):
        if len(sdp.F.rows[row]) > 0:
            col_index = 0
            for k in sdp.F.rows[row]:
                value = sdp.F.data[row][col_index]
                i, j = convert_to_mosek_index(sdp.block_struct, row_offsets,
                    block_offsets, row)
                if k > 0:
                    barai[k - 1].append(i)
                    baraj[k - 1].append(j)
                    baraval[k - 1].append(-value)
                else:
                    barci.append(i)
                    barcj.append(j)
                    barcval.append(value)
                col_index += 1
    return barci, barcj, barcval, barai, baraj, baraval