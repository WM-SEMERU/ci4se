def sodium_memcmp(inp1, inp2):
    ensure(isinstance(inp1, bytes), raising=exc.TypeError)
    ensure(isinstance(inp2, bytes), raising=exc.TypeError)
    ln = max(len(inp1), len(inp2))
    buf1 = ffi.new('char []', ln)
    buf2 = ffi.new('char []', ln)
    ffi.memmove(buf1, inp1, len(inp1))
    ffi.memmove(buf2, inp2, len(inp2))
    eqL = len(inp1) == len(inp2)
    eqC = lib.sodium_memcmp(buf1, buf2, ln) == 0
    return eqL and eqC