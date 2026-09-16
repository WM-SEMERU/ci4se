def _get_bit(self, n, hash_bytes):
    if hash_bytes[n // 8] >> int(8 - (n % 8 + 1)) & 1 == 1:
        return True
    return False