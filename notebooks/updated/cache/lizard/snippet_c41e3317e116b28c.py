def _build_hash_magic(self, subtitle_id):
    media_magic = self.HASH_MAGIC_CONST ^ subtitle_id
    hash_magic = media_magic ^ media_magic >> 3 ^ media_magic * 32
    return str(hash_magic)