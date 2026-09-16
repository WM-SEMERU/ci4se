def p_line_label_asm(p):
    p[0] = p[2]
    __DEBUG__("Declaring '%s%s' (value %04Xh) in %i" % (NAMESPACE, p[1],
        MEMORY.org, p.lineno(1)))
    MEMORY.declare_label(p[1], p.lineno(1))