def find_block_end(row, line_list, sentinal, direction=1):
    import re
    row_ = row
    line_ = line_list[row_]
    flag1 = row_ == 0 or row_ == len(line_list) - 1
    flag2 = re.match(sentinal, line_)
    if not (flag1 or flag2):
        while True:
            if row_ == 0 or row_ == len(line_list) - 1:
                break
            line_ = line_list[row_]
            if re.match(sentinal, line_):
                break
            row_ += direction
    return row_