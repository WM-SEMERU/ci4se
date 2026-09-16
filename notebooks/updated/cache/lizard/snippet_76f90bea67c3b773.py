def send_pgrp(cls, sock, pgrp):
    assert isinstance(pgrp, IntegerForPid) and pgrp < 0
    encoded_int = cls.encode_int(pgrp)
    cls.write_chunk(sock, ChunkType.PGRP, encoded_int)