def mutations_batcher(self, flush_count=FLUSH_COUNT, max_row_bytes=
    MAX_ROW_BYTES):
    return MutationsBatcher(self, flush_count, max_row_bytes)