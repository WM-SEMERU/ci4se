def getErrorCorrectMapping(cell_barcodes, whitelist, threshold=1):
    true_to_false = collections.defaultdict(set)
    whitelist = set([str(x).encode('utf-8') for x in whitelist])
    for cell_barcode in cell_barcodes:
        match = None
        barcode_in_bytes = str(cell_barcode).encode('utf-8')
        for white_cell in whitelist:
            if barcode_in_bytes in whitelist:
                continue
            if edit_distance(barcode_in_bytes, white_cell) <= threshold:
                if match is not None:
                    match = None
                    break
                else:
                    match = white_cell.decode('utf-8')
        if match is not None:
            true_to_false[match].add(cell_barcode)
    return true_to_false