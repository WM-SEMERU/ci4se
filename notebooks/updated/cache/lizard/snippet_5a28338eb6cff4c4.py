def ungap_sequences(records, gap_chars=GAP_TABLE):
    logging.info(
        'Applying _ungap_sequences generator: removing all gap characters')
    for record in records:
        yield ungap_all(record, gap_chars)