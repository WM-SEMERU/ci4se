def gen_div(src1, src2, dst):
    assert src1.size == src2.size
    return ReilBuilder.build(ReilMnemonic.DIV, src1, src2, dst)