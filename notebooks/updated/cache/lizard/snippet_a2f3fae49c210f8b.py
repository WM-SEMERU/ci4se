def main():
    t, kf, t0, major, minor, prod, beta = sympy.symbols('t k_f t0 Y Z X beta',
        negative=False)
    for f in funcs:
        args = [t, kf, prod, major, minor]
        if f in (pseudo_rev, binary_rev):
            args.insert(2, kf / beta)
        expr = f(*args, backend='sympy')
        with open(f.__name__ + '.png', 'wb') as ofh:
            sympy.printing.preview(expr, output='png', filename='out.png',
                viewer='BytesIO', outputbuffer=ofh)
        with open(f.__name__ + '_diff.png', 'wb') as ofh:
            sympy.printing.preview(expr.diff(t).subs({t0: 0}).simplify(),
                output='png', filename='out.png', viewer='BytesIO',
                outputbuffer=ofh)