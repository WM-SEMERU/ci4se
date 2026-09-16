def hash_starts_numeric(records):
    for record in records:
        seq_hash = hashlib.sha1(str(record.seq)).hexdigest()
        if seq_hash[0].isdigit():
            yield record