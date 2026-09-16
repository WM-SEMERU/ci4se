def gen_sdiv(src1, src2, dst):
    assert src1.size == src2.size
    return ReilBuilder.build(ReilMnemonic.SDIV, src1, src2, dst)